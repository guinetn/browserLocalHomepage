import { config } from "./config.js";
import { utils } from "./utils.js";
import { Blog } from "./blog.js";
import { slideShow } from "./slideshow.js";

export class App extends Blog {
  // Pointer to current book object in books[]
  currentBook = null;
  // Contains DOM elements matching the config.booksCssSelector '.book'
  // Defined in config.booksFile (assets/books.html)
  books = []; // A list of books find in books.html (all div with class='book') [{ id:0, dom: null, name: '', bookMark: 0 }, …]
  bookDetails = null;

  /*A book object is made of
    { id:0             id
      dom: null        Dom element associated to the book
      name: ''         id of the book in books.html: <div id='blog" class='book'>
      bookMark: 0      ChapterId. Allow to retrieve the last chapter viewed when coming back to the book
    }
  */

  chapters = [];
  currentBookMark = 0; // To run through chapters
  // When [→] is pressed we need to know if the current book chapter has already been loaded because we can
  // navigate through books without load chapters: Load the book's chapters when [→] if names are differents
  chaptersBookName = null;
  chapterHasError = false;
  chaptersVisible = null;
  chapterMeter = null;

  // For automatic selected text copy after some time elaspsed
  isMouseDown = false;
  mouseDownStartTime = null;

  constructor() {
    super(".blogArticleContainer");

    // Get books[]
    document
      .querySelectorAll(config.booksCssSelector)
      .forEach((v, i) =>
        this.books.push({ id: i, name: v.id, dom: v, bookMark: 0 })
      );
    if (this.books.length > 0) this.currentBook = this.books[0];
    else
      console.log(`Books not found with selector ${config.booksCssSelector}`);

    this.bookDetails = document.getElementById("bookDetails");
    this.chapterMeter = document.getElementById("chapterMeter");

    // RENDER topics in books
    utils.downloadJsonFile(config.topicsFile, this, this.extractTopics);
    // RENDER books[]
    this.renderBooksCatalog();

    // Init components
    if (slideShow) slideShow.init();
    // Set the link to manually open the blog items folder on github
    document.getElementById("blogRepoLink").href = config.blogRepo;

    this.loadBlogArticles();
  }

  chaptersChanged(event) {
    // Event happening When a downloaded element (download.code(/html/raw/chapter/md) has been added to the DOM
    let { reason, hash, htmlData, textData } = event.data;

    if (reason != "chapters changed") return;

    const promiseMarker = document.getElementById(hash);

    // For each separator (:::: = <p>::::</p>)
    const regexSeparator = /`<p>${config.chaptersSeparator}:*<\/p>`/gi;
    let chapters = (htmlData ? htmlData : textData).split(regexSeparator);

    chapters.forEach((s, i) => {            
      let div = document.createElement("div");
      if (htmlData) div.innerHTML = s;
      else div.innerText = s;

      /* 
        From the promiseMarker (<div data-type='promised_file'...)
        If previous node is a separator (<p>::::</p>) then it must be a chapter:
          * insert htmlData/textData after the first parent having a class='chapters'
          * removed the promiseMarker
          * removed the <p>::::</p>
        
        <div id="s1" class="chapters">
        <div id="s2" class="chapters">
        <div id="s3" class="chapters">
          <div class="chapter current" data-id="3">
            <div data-type="promised_file" id="YXNz...ZbmcubWQ=">wanting for…/notetaking.md</div><div><h1 id="note-taking">NOTE TAKING</h1>
            ....
            <p>::::</p>
            <div data-type="promised_file" id="YXN...JuaW5nLm1k">wanting for…/learning.md</div>
            <div><h1 id="learning--repeat-review">Learning = repeat, review</h1>
      */
      let prevNode = promiseMarker.previousElementSibling;
      const isolatedSeparatorMode =
        chapters.length > 1 && i < chapters.length - 1;
      if (prevNode &&(isolatedSeparatorMode || prevNode.innerText.substring(0, 4) == config.chaptersSeparator)) {
        // promiseMarker previous node is a separator (<p>::::</p>)
        prevNode = prevNode.parentNode;
        while (prevNode) {
          // Look-up until finding a "chapters"
          if (prevNode.classList.contains("chapters")) {
            div.className = 'page';
            prevNode.insertAdjacentElement("beforeEnd", div);

            // Remove the separator <p>::::</p>
            let pmp = promiseMarker.previousElementSibling;            
            if (pmp.innerText == config.chaptersSeparator)
              promiseMarker.previousElementSibling.remove();
            break;
          }
          prevNode = prevNode.parentNode;
        }
      } else {
        promiseMarker.insertAdjacentElement("afterEnd", div);
      }
    });

    // Remove the promise marker. Nice to debug loading elements placeholders
    promiseMarker.remove();

    this.updateChapters();
  }

  updateChapters() {
    this.chapters = document.querySelectorAll(".page");
    this.chapters.forEach((s, i) => s.setAttribute("data-id", i + 1));

    // Configure chapter meter [min-value-max]
    this.chapterMeter.value = 1;
    this.chapterMeter.max = this.chapterHasError ? 0 : this.chapters.length;

    this.renderChaptersCatalog();
    this.renderBookDetails();
  }

  /* Render books's list
  00. BLOG
  01. Home
  02. Computer Science
  ...*/
  renderBooksCatalog() {
    const source = [...document.querySelectorAll(".book")];
    renderCatalog(source, ".booksCatalog", "data-bookid", "booksCatalogLink", false, 0);
  }

  renderChaptersCatalog() {
    // Called each time a book is changed (has a new fetched child )
    renderCatalog(
      this.chapters,
      ".chaptersCatalog",
      "data-chapterid",
      "chapterCatalogLink",
      true
    );
  }

  showChapter(bookMark) {
    this.changeChapter(bookMark - this.currentBookMark);
  }

  // HeartBeat
  tick() {
    this.checkCopySelectedTextCondition();
  }

  // has mousedown enough duration to make a selected text copy?
  checkCopySelectedTextCondition() {
    if (!this.isMouseDown) return;

    const mouseDownDurationSec = (new Date() - this.mouseDownStartTime) / 1000;
    if (config.mouseDownDurationForCopySec <= mouseDownDurationSec) {
      utils.copyToClipboard(document.getSelection());
      this.mouseDownStartTime = new Date();
    }
  }

  // Manage key events
  keydownEvent(e) {
    this.onBookKeydown(e);
    // if book hasn't catched the event, try with chapter
    if (!e.defaultPrevented) this.onChapterKeydown(e);
  }

  onBookKeydown(e) {
    if (e.shiftKey) return;

    // Keys = shortcuts to books
    let key = e.key.toLowerCase();
    if (!e.ctrlKey && !e.altKey) {
      // 1st Letter of the book
      if ("a" <= key && key <= "z") {
        // user press a key [a-z]: find first book having a name starting with that letter
        let book = this.books.filter(
          (aBook) => aBook.name.slice(0, key.length) == key
        );
        if (book.length == 0) return;
        this.selectBook(book[0].id, e);
      } else if ("0" <= key && key <= "9") {
        // Numpad keys
        this.selectBook(e.key, e);
      }
    }

    // Navigate in books by [+] or [CTRL + →]
    if (e.key == "+" || (e.ctrlKey && e.keyCode == 39) /*right*/) {
      this.selectBook("next", e);
    }
    // Navigate in books by "-" or [CTRL + ←]
    else if (e.key == "-" || (e.ctrlKey && e.keyCode == 37) /*left*/) {
      this.selectBook("prev", e);
    } else if (
      e.ctrlKey ||
      ![...this.books].some((v) => v.name == this.currentBook.name)
    )
      return; // no key match a book name
  }

  // Manage books limits with [←] [→]
  scaleBookId(stepOrIndex) {
    let bookId = parseInt(stepOrIndex, 10);
    if (isNaN(bookId)) {
      if (stepOrIndex == "next") stepOrIndex = 1;
      if (stepOrIndex == "prev") stepOrIndex = -1;
      bookId = this.currentBook.id + stepOrIndex;
    }
    return bookId < 0
      ? this.books.length - 1
      : this.books.length <= bookId
      ? 0
      : bookId;
  }

  selectBookAndOpenChapter(stepOrIndex, openChapter) {
    this.selectBook(stepOrIndex);
    if (openChapter) this.changeChapter(+1);
  }

  // stepOrIndex: prev, next or bookId
  selectBook(stepOrIndex, keyEvent = null) {
    this.currentBook = this.books[this.scaleBookId(stepOrIndex)];
    this.showBook(keyEvent);
  }

  showBook(keyEvent = null) {
    if (keyEvent) keyEvent.preventDefault();
    utils.scrollTo(0);
    // Hide Chapters (chapters are load on [→])
    this.toggleChaptersVisibility(false);
    
    // Show the current book by applying css 'active' class. Remove 'active' from others books
    this.books.forEach((book) =>
      book.name == this.currentBook.name
        ? book.dom.classList.add("active")
        : book.dom.classList.remove("active")
    );
  }

  onChapterKeydown(e) {
    if (e.keyCode == 27 || e.shiftKey) {
      // [ESC] or [SHIFT]	key
      this.toggleChaptersVisibility(false);
      if (this.currentBookMark > 0) this.currentBookMark--; // to come back on the same chapter after [esc]] (as we do [→] to show it again, we don't want chapter+0)
      this.currentBook.bookMark = Math.min(this.currentBookMark + 1, this.chapters.length - 1); // memo the chapter id to retrieve after anothers book navigation and come back
    } else {
      switch (e.keyCode) {
        case 37: // [←] key
          e.preventDefault(); // to have scrollTo() working
          this.changeChapter(-1);
          break;
        case 39: // [→] key
          e.preventDefault();
          this.changeChapter(+1);
          break;
        case 70: // [F]ullscreen key
          if (this.chaptersVisible)
            utils.fullScreen(this.chapters[this.currentBookMark]);
          else utils.fullScreen(this.currentBook.dom);
          break;
      }
    }
  }
  async changeChapter(direction) {    
    // If book has change and dom has chapters of another book, load the current book's chapters
    if (this.chaptersBookName != this.currentBook.name) {
      this.createChaptersInDom(config.chaptersContainer);
      // Restore bookMark from a previous visit of the current book
      this.currentBookMark = this.currentBook.bookMark;
      return;
    }
   
    // Press [→] while chapters are not visible: show chapters
    if (
      !this.chaptersVisible &&
      this.currentBookMark == 0 &&
      direction > 0
    ) {
      this.toggleChaptersVisibility(true);
      utils.scrollTo(0, "auto");
      return;
    }

    this.currentBookMark += direction;
    if (this.chapters.length <= this.currentBookMark) this.currentBookMark = 0;
    else if (this.currentBookMark < 0) this.currentBookMark = this.chapters.length-1;
    this.toggleChaptersVisibility(true);
    utils.scrollTo(0, "auto");

    if (slideShow) slideShow.init();
  }

  async downloadMainChapter(folder, chapterFile) {
    try {
      let relativePath = `${folder}/${chapterFile}`;
      let response = await fetch(relativePath);
      let markdown = await response.text();
      let html = null;
      let htmlChapters = null;
      this.chapterHasError = !response.ok;
      if (this.chapterHasError) {
        htmlChapters = [
          `⚠️ ${response.statusText} (${response.status}): ${relativePath}`,
        ];
      } else {
        html = this.markdownToHtml(markdown);
        // nested download.md(...) must be extracted and promoted to chapter
        htmlChapters = html.split(config.chaptersSeparator); // separator is :::: = <p>::::</p> in markdown
      }

      return htmlChapters;
    } catch (e) {
      console.log(`Error in downloadMainChapter(${chapterFile})`, e);
    }
  }

  createChaptersInDom(chaptersContainer) {
    this.deleteExistingChapters();

    this.chaptersBookName = this.currentBook.name;

    this.downloadMainChapter(
      `${config.chaptersFolder}/${this.chaptersBookName}`,
      `${config.chapterMainFilePrefix}${this.chaptersBookName}.md`
    ).then((htmlChapters) => {
      this.appendChapters(htmlChapters, chaptersContainer);
      this.updateChapters();
      this.toggleChaptersVisibility(true);
      this.renderCurrentChapter();
      PR.prettyPrint();
    });
  }

  appendChapters(chapters, container) {
    chapters.forEach((html, i) => {
      const chapter = document.createElement("div");
      chapter.innerHTML = `<div class='page'>${chapters[i]}</div>`;
      chapter.id = `s${i + 1}`;
      chapter.className = "chapters";
      document.querySelector(container).appendChild(chapter);
    });
  }
  markdownToHtml(data, useExtensions = true) {
    // Transform md → html
    // useExtensions allow to avoid to trasnform files like help wich can include extensions syntax themselves (so not to render)
    const extensions = useExtensions
      ? { extensions: ["BkaShowDownExtension"] }
      : null;
    var converter = new showdown.Converter(extensions);
    return converter.makeHtml(data);
  }
  renderCurrentChapter() {
    this.chapterMeter.value = this.currentBookMark + 1;
    this.renderBookDetails();
    if (slideShow) slideShow.init();
    this.chapters.forEach((s, i) =>
      this.chaptersVisible && i == this.currentBookMark
        ? s.classList.add("current")
        : s.classList.remove("current")
    );
    renderScrollSyncCatalog(".page.current", ".contentCatalog");
  }

  renderBookDetails() {
    const bookTitle = this.currentBook.name.toUpperCase().replace("_", " ");
    const chapterNav = this.chapterHasError
      ? "⚠️"
      : ` <sup><small>${this.chapterMeter.value}/${this.chapters.length}</small></sup>`;
    // Set book title
    this.bookDetails.querySelector(
      "#bookTitlePlaceholder"
    ).innerHTML = `<sup><small>book</small></sup> ${bookTitle} ${chapterNav}`;
  }

  toggleChaptersVisibility(forceVisibility) {
    this.hideBlog();

    if (forceVisibility != undefined) this.chaptersVisible = forceVisibility;
    else this.chaptersVisible = !this.chaptersVisible;

    this.chaptersVisible
      ? this.bookDetails.classList.add("visible")
      : this.bookDetails.classList.remove("visible");

    this.renderCurrentChapter();
  }

  deleteExistingChapters() {
    if (this.chapters.length > 0) this.chapters.forEach((s) => s.remove());
    document.querySelectorAll(".chapters").forEach((s) => s.remove());
    this.chapters = null;
    this.currentBookMark = 0;
  }

  extractTopics(options, topics) {
    const regex = /(?<link>[^\[\(]*)+(\[+(?<classes>[^\]]*)?\]+)*(\(+(?<description>[^\)]*)?\)+)*/;

    for (var topic in topics) {
      const topicType = typeof topics[topic];
      if (topicType == "object" || topicType == "array") {
        const container = document.querySelector(`#${topic}`);
        if (container == undefined) continue;

        const containerAttr = container.getAttribute("data-info");
        if (
          containerAttr == null ||
          (containerAttr != null &&
            containerAttr.toLowerCase().indexOf("-t") < 0)
        ) {
          // Add topic title
          let h3 = document.createElement("h3");
          h3.innerText = topic.toUpperCase().replace("_", " ");
          container.appendChild(h3);
        }

        topics[topic].forEach(function (item) {
          var m = regex.exec(item); // ex: "https://gmail.com[fas fa-envelope](GMAIL)"
          if (m != null) {
            let link = m.groups["link"];
            let classes = m.groups["classes"];
            let description = m.groups["description"];

            let elem = options.createTopic(link, classes, description);
            if (elem != null) container.appendChild(elem);
          } else console.log(`ExtractTopics(): Error in parsing ${item}`);
        });
      }
    }
  }

  simplifyLink(link) {
    /*
      https://developers.google.com/analytics → developers.google.com/analytics
      https://www.nasaspaceflight.com			→ nasaspaceflight.com 
    
      */
    let match = /((?<prot>https?):\/{2}(w{3})?\.?(?<domain>[^/]*)\/?(?<query>.*)?|(?<link>.*))?/.exec(
      link
    );
    if (match != null) {
      if (match.groups["link"] != undefined) return match.groups["link"];
      else return match.groups["domain"];
    }
  }

  createTopicFromApiWithJson(hash, link, classes, description) {
    utils.downloadJsonFile(
      link,
      [hash, classes, description, this],
      function (options, jsonObject) {
        const hash = options[0];
        let cronInterval = null;
        if (typeof description == "array" || typeof description == "object") {
          cronInterval = description[1];
          description = description[0];
        }
        const tag = document.getElementById(hash);
        let tagAnchor = tag.querySelector("a");
        if (!tagAnchor) tagAnchor = document.createElement("a");

        if (jsonObject.error) {
          tagAnchor.innerHTML = `❌ ${description.substring(1)}`;
          tagAnchor.title = jsonObject.error;
          tagAnchor.href = link;
          tagAnchor.classList = "downloadError";
          tagAnchor.target = "_blank";
          tagAnchor.rel = "noopener";
          tag.appendChild(tagAnchor);
          return;
        }

        // Look for variables prefixed by '$'
        // http://ip-api.com/json/[!getjson](my lat/lon: $lat $lon)
        const regex = /(?<=\$)\w*/g;
        let variablesFound = description.match(regex);
        if (variablesFound != null) {
          let tagContent = description;

          variablesFound.forEach((stringToExtract) => {
            options[3].jsonExplorer(
              jsonObject,
              stringToExtract,

              function (found) {
                if (tagContent.indexOf(stringToExtract) >= 0) {
                  tagContent = tagContent.replace(`$${stringToExtract}`, found);
                  tagAnchor.innerHTML = tagContent;
                } else {
                  tagAnchor.innerHTML += found;
                }
                tagAnchor.href = link;
                tagAnchor.target = "_blank";
                tagAnchor.className = "topicLink";
                tagAnchor.rel = "noopener";
                tag.title =
                  link + (cronInterval == null ? "" : `${cronInterval}`);
                tag.appendChild(tagAnchor);
              }
            );
          });
        }
      }
    );
  }

  createTopicFromApiWithText(hash, link, classes, description) {
    utils.downloadTextFile(
      link,
      [hash, classes, description],
      function (options, jsonObject) {
        const hash = options[0];
        const tag = document.getElementById(hash);
        const tagAnchor = document.createElement("a");
        tagAnchor.innerHTML = jsonObject;
        tagAnchor.title = link;
        tagAnchor.href = link;
        tagAnchor.target = "_blank";
        tagAnchor.className = "topicLink";
        tagAnchor.rel = "noopener";
        tag.appendChild(tagAnchor);
      }
    );
  }

  createTopicFromApi(prefix, typeOfCall, link, classes, description) {
    var hash = `api_${utils.getHash(link)}`;
    let apiElement =
      prefix == "block"
        ? document.createElement("div")
        : document.createElement("span");
    apiElement.id = hash;

    switch (typeOfCall) {
      case "json":
        // Look for cron defined by !getjsonxxx   xx… = digit[s]
        // http://ip-api.com/json/[!getjson =lat =lon](my lat/lon: $lat $lon)    single call
        // http://ip-api.com/json/[!getjson60 =lat =lon](my lat/lon: $lat $lon)  call every 60 sec
        let cronInterval = classes.match(/(?<=!getjson)\d+/);
        let enrichedDescription = description;
        if (cronInterval != null) {
          enrichedDescription = [
            description,
            `. Fetch frequency: ${cronInterval[0]} sec`,
          ];
          setInterval(() => {
            this.createTopicFromApiWithJson(
              hash,
              link,
              classes,
              enrichedDescription
            );
          }, cronInterval[0] * 1000);
        }

        this.createTopicFromApiWithJson(
          hash,
          link,
          classes,
          enrichedDescription
        );
        break;

      case "text":
        this.createTopicFromApiWithText(hash, link, classes, description);
        break;
    }
    return apiElement;
  }

  jsonExplorer(jsonObject, stringToExtract, callback) {
    for (var key in jsonObject) {
      const topicType = typeof jsonObject[key];
      if (topicType == "object" || topicType == "array")
        this.jsonExplorer(jsonObject[key], stringToExtract, callback);
      else if (key == stringToExtract) callback(jsonObject[stringToExtract]);
    }
  }

  createTopic(link, classes, description) {
    const prefix =
      (classes || "block").indexOf("inline") >= 0 ? "inline" : "block";

    // link[classes](description)
    // "https://httpbin.org/ip[inline !getjson !tic3 =origin](★ my ip: $origin)",
    // "https://www.ted.com(TEDx)"

    if (classes && classes.indexOf("!getjson") >= 0) {
      return this.createTopicFromApi(
        prefix,
        "json",
        link,
        classes,
        description
      );
    } else if (classes && classes.indexOf("!gettext") >= 0) {
      return this.createTopicFromApi(
        prefix,
        "text",
        link,
        classes,
        description
      );
    }

    const fragment = document.getElementById(`${prefix}LinkTemplate`);
    const instance = document.importNode(fragment.content, true);

    let a = instance.querySelector(".topicLink");
    a.href = link;
    a.title = link;
    if (classes != undefined)
      classes.split(" ").forEach((cl) => a.classList.add(cl)); // classlist doesn't accept spaces...

    if (prefix != "inline")
      a.innerText += description || this.simplifyLink(link) || "???";

    return instance;
  }

  onMouseDown(e) {
    this.mouseDownStartTime = new Date();
    this.isMouseDown = true;
  }
  onMouseUp(e) {
    this.isMouseDown = false;
    this.mouseDownStartTime = null;
  }

  // Manage app's clicks events
  onClick(e) {
    if (this.reloadBlogArticles(e)) return;
    else if (this.slideShowEvents(e)) return;
    else if (this.showBlogArticle(e)) return;
    else if (this.copyAction(e)) return;
    else if (this.emptyClickToClose(e)) return;
    else if (this.openBookFromCatalog(e)) return;
    else if (this.chapterNavigation(e)) return;
    else if (this.showAlarmsPanel(e)) return;
    else this.alarmChosen(e);
  }

  // Refresh blog articles
  reloadBlogArticles(e) {
    if (!e.target.matches(".articlesReloadLink")) return false;

    this.loadBlogArticles();
    return true;
  }

  slideShowEvents(e) {
    // Click slideshow [←] button = Go to Previous Slide
    if (e.target.matches(".slideShowSlidePrev") && slideShow) {
      slideShow.plusSlides(e.target.parentNode.id, -1);
      return true;
    }
    // Click slideshow [→] button = Go to Next Slide
    else if (e.target.matches(".slideShowSlideNext") && slideShow) {
      slideShow.plusSlides(e.target.parentNode.id, 1);
      return true;
    }
    // Click a slideshow dot < o o o o > = Go to the slide with same id
    else if (e.target.matches(".slideShowDot")) {
      slideShow.currentSlide(
        e.target.parentNode.parentNode.id,
        e.target.getAttribute("data-dotspan")
      );
      return true;
    }

    return false;
  }

  // Click a blog article
  showBlogArticle(e) {
    if (
      !(
        e.target.parentNode.matches(".blogArticleLink") ||
        e.target.matches(".blogArticleLink")
      )
    )
      return false;

    // say to next event processing methods that it has been consumed
    e.preventDefault();

    const target = e.target.parentNode.matches(".blogArticleLink")
      ? e.target.parentNode
      : e.target;
    this.showBlog(target);
    return true;
  }

  copyAction(e) {
    if (!e.target.matches(".copy")) return false;

    utils.copyToClipboard(e.target.innerText);
    return true;
  }

  // Click on empty element => close opened windows (alarm, blog)
  emptyClickToClose(e) {
    if (
      !(
        e.target.matches(`${config.booksCssSelector}.active`) ||
        e.target.parentNode.matches(
          `${config.booksCssSelector}.active, .topics`
        )
      )
    )
      return false;
    this.hideBlog();
    if (utils.alarmVisible) utils.alarmOpenClose();

    return true;
  }

  // Click a book on the books catalog
  openBookFromCatalog(e) {
    if (!e.target.matches(".booksCatalogLink")) return false;

    // A Right click (on the book name) open only the book
    // A left click (on the book number) open the book + force chapters loading (normally load on [→])
    const linkWidthAreaToOpenChapters = 35;
    this.selectBookAndOpenChapter(
      e.target.dataset.bookid,
      e.offsetX < linkWidthAreaToOpenChapters
    );
    return false;
  }

  chapterNavigation(e) {
    if (!e.target.matches(".chapterCatalogLink")) return false;
    // Chapters catalog clicked: navigate to clicked chapter
    this.showChapter(e.target.dataset.chapterid);
    return true;
  }

  showAlarmsPanel(e) {
    if (
      !(
        e.target.matches("#clock") ||
        e.target.matches("#alarm") ||
        (utils.alarmVisible && e.target.className == "active book")
      )
    )
      return false;

    utils.alarmOpenClose();
    return true;
  }

  alarmChosen(e) {
    if (!e.target.matches(".alarmItem")) return false;

    // alarm already set ? → Cancel it
    if (e.target.classList.contains("alarm-active")) {
      utils.alarmSet(0);
      return true;
    }

    // set alarm
    const alarmSelected = document.querySelector(".alarmMessage");
    const alarmReason = alarmSelected.value || "";
    const alarmDurationMin = e.target.getAttribute("data-duration");
    e.target.classList.toggle("alarm-active");
    utils.alarmOpenClose();
    utils.snackbarPopup(`Alarm in ${alarmDurationMin} min<br/>${alarmReason}`);
    utils.speak(`Alarm in ${alarmDurationMin} min`);
    utils.alarmSet(alarmDurationMin, alarmReason);

    return true;
  }

  loadBlogArticles() {
    utils.fetchGithubFolder(config.blogRepoApi, this.listBlogArticles);
  }
}
