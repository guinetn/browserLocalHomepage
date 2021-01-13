import { config } from "./config.js";
import { utils } from "./utils.js";
import { Blog } from "./blog.js";
import { slideShow } from "./slideshow.js";

export class Bka extends Blog {
  currentView = null;
  views = []; // [{ id:0, dom: null, name: '', slideId: 0 }, …]  slideId allow to retrieve the last slide viewed before leaving the view
  viewName = null;

  currentSlideId = 0;
  // When [→] is pressed we need to know if the current view slide have been loaded. Load the view slide if names are differents
  currentSlidesFile = null;
  slideHasError = false;
  slidesVisible = null;
  slides = [];
  slidesToc = null;
  slideMeter = null;

  isMouseDown = false;
  mouseDownTime = null;

  constructor() {
    super("blogPlaceHolder");

    document
      .querySelectorAll(config.viewsCssSelector)
      .forEach((v, i) =>
        this.views.push({ id: i, name: v.id, dom: v, slideId: 0 })
      );
    this.currentView = this.views[0];

    // Set the link to manually open the blog items folder on github
    document.getElementById("blogRepoLink").href = config.blogRepo;
    
    this.viewName = document.getElementById("viewName");
    this.slidesToc = document.querySelector(".slidesToc");
    this.slideMeter = document.getElementById("slideMeter");

    utils.downloadJsonFile(config.topicsFile, null, this.extractTopics);
    this.renderViewsList();
    if (slideShow) slideShow.init();
  }

  slidesChanged(event) {
    let { reason, hash, htmlData, textData } = event.data;

    if (reason != "slides changed") return;

    // When a downloaded element has been added to the DOM
    const promiseMarker = document.getElementById(hash);

    // For each separator (:::: = <p>::::</p>)
    let slides = (htmlData ? htmlData : textData).split('<p>::::</p>'); 
    
    slides.reverse().forEach((s, i) => {
      let div = document.createElement("div");
      if (htmlData) div.innerHTML = s;
      else div.innerText = s;

      /* 
          From the promiseMarker (<div data-type='promised_file'...)
          If previous node is a separator (<p>::::</p>) then it must be a slide:
            * insert after the first parent having a class='slides'
            * removed the promiseMarker
            * removed the <p>::::</p>
          
          <div id="s1" class="slides">
          <div id="s2" class="slides">
          <div id="s3" class="slides">
            <div class="slide current" data-id="3">
              <div data-type="promised_file" id="YXNz...ZbmcubWQ=">wanting for…/notetaking.md</div><div><h1 id="note-taking">NOTE TAKING</h1>
              ....
              <p>::::</p>
              <div data-type="promised_file" id="YXN...JuaW5nLm1k">wanting for…/learning.md</div>
              <div><h1 id="learning--repeat-review">Learning = repeat, review</h1>
          */
      let prevNode = promiseMarker.previousElementSibling;
      const isolatedSeparatorMode = (slides.length > 1 && i < slides.length-1);
      if (isolatedSeparatorMode ||
        (prevNode &&
          prevNode.innerText.substring(0, 4) == config.slidesSeparator)
      ) {
        // promiseMarker previous node is a separator (<p>::::</p>)
        //if (prevnode) 
          prevNode = prevNode.parentNode;
        while (prevNode) {
          // Look-up until finding a "slides"
          if (prevNode.classList.contains("slides")) {
            div.className = "slide";
            prevNode.insertAdjacentElement("beforeEnd", div);
            
            // Remove the separator <p>::::</p>
            let pmp = promiseMarker.previousElementSibling;
            if (pmp.innerText==config.slidesSeparator)
              promiseMarker.previousElementSibling.remove();
            break;
          }
          prevNode = prevNode.parentNode;
        }
      } else {
        promiseMarker.insertAdjacentElement("afterEnd", div);
      }
    });
    
    // Remove the promise marker
    promiseMarker.remove();

    this.updateSlides();
  }

  updateSlides() {
    this.slides = document.querySelectorAll(".slide");
    this.slides.forEach((s, i) => s.setAttribute("data-id", i + 1));

    // Configure slide meter [min-value-max]
    this.slideMeter.value = 1;
    this.slideMeter.max = this.slideHasError ? 0 : this.slides.length;

    this.renderSlidesToc();
    this.renderViewName();
  }

  /* Render views's list
  00. BLOG 📂
  01. Home
  02. Computer Science
  ...*/
  renderViewsList() {
    let viewsListBox = document.querySelector(".viewsListBox");

    [...document.querySelectorAll(".view")].forEach((v, i) => {
      [...v.querySelectorAll("h1")].map((x) => {
        let div = document.createElement("div");
        let key = ("0" + i).slice(-2);
        if (i < 10) key = `${key}`;
        div.innerHTML = `${key}. ${x.innerText}`;

        viewsListBox.appendChild(div);
      });
    });
  }

  renderSlidesToc() {
    this.slidesToc.innerHTML = null;

    this.slides.forEach((s, i) => {
      [...s.querySelectorAll("h1")].map((x) => {
        let div = document.createElement("div");
        div.className = "slideTocLink";
        div.setAttribute("data-slideid", i);
        div.innerText = `${("0" + (1 + i)).slice(-2)}. ${x.innerText}`;
        this.slidesToc.appendChild(div);
      });
    });
  }

  showSlide(slideid) {
    this.changeSlide(slideid - this.currentSlideId);
  }

  tick() {
    if (!this.isMouseDown) return;

    const mouseDownDurationSec = (new Date() - this.mouseDownTime) / 1000;
    if (config.mouseDownDurationForCopySec <= mouseDownDurationSec) {
      utils.copyToClipboard(document.getSelection());
      this.mouseDownTime = new Date();
    }
  }

  onViewKeydown(e) {
    if (e.shiftKey) return;

    // Keys = shortcuts to views
    let key = e.key.toLowerCase();
    if (!e.ctrlKey && !e.altKey) {
      // 1st Letter of the view
      if ("a" <= key && key <= "z") {
        // user press a key [a-z]: find first view having a name starting with that letter
        let view = this.views.filter(
          (view) => view.name.slice(0, key.length) == key
        );
        if (view.length == 0) return;
        this.currentView = view[0];
      } else if ("0" <= key && key <= "9") {
        // Numpad keys
        this.currentView = this.views[e.key];
      }
    }

    // Navigate in views by [+] or [CTRL + →]
    if (e.key == "+" || (e.ctrlKey && e.keyCode == 39) /*right*/) {
      this.currentView = this.views[
        this.views.length <= this.currentView.id + 1
          ? 0
          : this.currentView.id + 1
      ];
    }
    // Navigate in views by "-" or [CTRL + ←]
    else if (e.key == "-" || (e.ctrlKey && e.keyCode == 37) /*left*/) {
      this.currentView = this.views[
        this.currentView.id - 1 < 0
          ? this.views.length - 1
          : this.currentView.id - 1
      ];
    } else if (
      e.ctrlKey ||
      ![...this.views].some((v) => v.name == this.currentView.name)
    )
      return; // no key match a view name

    e.preventDefault();
    utils.scrollTo(0);
    // hide slides
    this.toggleSlidesVisibility(false);
    // display view
    this.views.forEach((view) =>
      view.name == this.currentView.name
        ? view.dom.classList.add("active")
        : view.dom.classList.remove("active")
    );
  }

  onSlideKeydown(e) {
    if (e.keyCode == 27 || e.shiftKey) {
      // [ESC] or [shift]	key
      this.toggleSlidesVisibility(false);
      if (this.currentSlideId > 0) this.currentSlideId--; // to come back on the same slide after [esc]] (as we do [→] to show it again, we don't want slide+0)
      this.currentView.slideId = Math.min(
        this.currentSlideId + 1,
        this.slides.length - 1
      ); // memo thz slide id to retrieve after anothers view navigation and come back
    } else {
      switch (e.keyCode) {
        case 37: // [←] key
          e.preventDefault(); // to have scrollTo() working
          this.changeSlide(-1);
          break;
        case 39: // [→] key
          e.preventDefault();
          this.changeSlide(+1);
          break;
        case 70: // [F]ullscreen key
          if (this.slidesVisible)
            utils.fullScreen(this.slides[this.currentSlideId]);
          else utils.fullScreen(this.currentView.dom);
          break;
      }
    }
  }

  async changeSlide(direction) {
    // If view has change and dom has slides of another view, load the current view slides
    if (this.currentSlidesFile != this.currentView.name) {
      this.createSlidesInDom(config.slidesContainer);
      // Restore slideId from a previous visit of the current view
      this.currentSlideId = this.currentView.slideId;
      return;
    }

    // Press [←] while on first slide: hide slides
    if (this.currentSlideId == 0 && direction < 0) {
      this.toggleSlidesVisibility(false);
      return;
    }
    // Press [→] while slides are not visible: show slides
    else if (!this.slidesVisible && this.currentSlideId == 0 && direction > 0) {
      this.toggleSlidesVisibility(true);
      utils.scrollTo(0, "auto");
      return;
    }

    this.currentSlideId += direction;
    if (this.slides.length <= this.currentSlideId) this.currentSlideId = 0;
    else if (this.currentSlideId < 0) this.currentSlideId = 0;
    this.toggleSlidesVisibility(true);
    utils.scrollTo(0, "auto");

    if (slideShow) slideShow.init();
  }

  async downloadMainSlide(folder, slideFile) {
    try {
      let relativePath = `${folder}/${slideFile}`;
      let response = await fetch(relativePath);
      let markdown = await response.text();
      let html = null;
      let htmlSlides = null;
      this.slideHasError = !response.ok;
      if (this.slideHasError) {
        htmlSlides = [
          `⚠️ ${response.statusText} (${response.status}): ${relativePath}`,
        ];
      } else {
        html = this.markdownToHtml(markdown);
        // nested download.md(...) must be extracted and promoted to slide
        htmlSlides = html.split(config.slidesSeparator); // separator is :::: = <p>::::</p> in markdown
      }

      return htmlSlides;
    } catch (e) {
      console.log(`Error in downloadMainSlide(${slideFile})`, e);
    }
  }

  createSlidesInDom(slidesContainer) {
    this.deleteExistingSlides();

    this.currentSlidesFile = this.currentView.name;

    this.downloadMainSlide(
      `${config.slidesFolder}/${this.currentSlidesFile}`,
      `_${this.currentSlidesFile}.md`
    ).then((htmlSlides) => {
      this.appendSlides(htmlSlides, slidesContainer);
      this.updateSlides();
      this.toggleSlidesVisibility(true);
      this.renderCurrentSlide();
      PR.prettyPrint();
    });
  }

  appendSlides(slides, container) {
    slides.forEach((html, i) => {
      const slide = document.createElement("div");
      slide.innerHTML = `<div class='slide'>${slides[i]}</div>`;
      slide.id = `s${i + 1}`;
      slide.className = "slides";
      document.querySelector(container).appendChild(slide);
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
  renderCurrentSlide() {
    this.slideMeter.value = this.currentSlideId + 1;
    this.renderViewName();
    this.slides.forEach((s, i) =>
      this.slidesVisible && i == this.currentSlideId
        ? s.classList.add("current")
        : s.classList.remove("current")
    );
    setTableOfContentVisibility(".slide.current", "#slide_toc");
  }

  renderViewName() {
    const slideTitle = this.currentView.name.toUpperCase().replace("_", " ");
    const slideNav = this.slideHasError
      ? "⚠️"
      : ` <sup><small>${this.slideMeter.value}/${this.slides.length}</small></sup>`;
    this.viewName.children[0].innerHTML = `${slideTitle} ${slideNav}`;
  }

  toggleSlidesVisibility(forceVisibility) {
    this.hideBlog();

    if (forceVisibility != undefined) this.slidesVisible = forceVisibility;
    else this.slidesVisible = !this.slidesVisible;

    this.slidesVisible
      ? this.viewName.classList.add("visible")
      : this.viewName.classList.remove("visible");

    this.renderCurrentSlide();
  }

  deleteExistingSlides() {
    if (this.slides.length > 0) this.slides.forEach((s) => s.remove());
    document.querySelectorAll(".slides").forEach((s) => s.remove());
    this.slides = null;
    this.currentSlideId = 0;
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

            let elem = Bka.createTopic(link, classes, description);
            if (elem != null) container.appendChild(elem);
          } else console.log(`ExtractTopics(): Error in parsing ${item}`);
        });
      }
    }
  }

  static simplifyLink(link) {
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

  static createTopicFromApiWithJson(hash, link, classes, description) {
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
        const tagAnchor = document.createElement("a");

        if (jsonObject.error) {
          tagAnchor.innerHTML += " ❌";
          tagAnchor.title = jsonObject.error;
          tagAnchor.href = link;
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

  static createTopicFromApiWithText(hash, link, classes, description) {
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

  static createTopicFromApi(prefix, typeOfCall, link, classes, description) {
    var hash = `api_${utils.getHash(link)}`;
    let apiElement =
      prefix == "block"
        ? document.createElement("div")
        : document.createElement("span");
    apiElement.id = hash;
    apiElement.className = "topicLink";

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

  static jsonExplorer(jsonObject, stringToExtract, callback) {
    for (var key in jsonObject) {
      const topicType = typeof jsonObject[key];
      if (topicType == "object" || topicType == "array")
        this.jsonExplorer(jsonObject[key], stringToExtract, callback);
      else if (key == stringToExtract) callback(jsonObject[stringToExtract]);
    }
  }

  static createTopic(link, classes, description) {
    const prefix =
      (classes || "block").indexOf("inline") >= 0 ? "inline" : "block";

    // link[classes](description)
    // "https://httpbin.org/ip[inline !getjson !tic3 =origin](my ip: $origin)",
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
      a.innerText = description || this.simplifyLink(link) || "???";

    return instance;
  }

  onMouseDown(e) {
    this.mouseDownTime = new Date();
    this.isMouseDown = true;
  }
  onMouseUp(e) {
    this.isMouseDown = false;
    this.mouseDownTime = null;
  }
}
