import { config } from "./config.js";
import { utils } from "./utils.js";
import { slideShow } from "./slideshow.js";

( function() {
	 
  class bka {
    currentView = null;
    views = []; // [{ id:0, dom: null, name: '', slideId: 0 }, …]  slideId allow to retrieve the last slide viewed before leaving the view
    viewName = null;

    currentSlideId = 0;
    currentSlidesFile = null;
    slideHasError = false;
    slidesVisible = null;
    slides = [];
    slidesToc = null;
    slideMeter = null;

    currentBlog = null;

    isMouseDown = false;
    mouseDownTime = null;

    constructor() {
      document
        .querySelectorAll(config.viewsCssSelector)
        .forEach((v, i) =>
          this.views.push({ id: i, name: v.id, dom: v, slideId: 0 })
        );
      this.currentView = this.views[0];

      document.getElementById("blogRepoLink").href = config.blogRepo;
      this.currentBlog = document.getElementById("blogItem");
      this.viewName = document.getElementById("viewName");
      this.slidesToc = document.querySelector(".slidesListBox");
      this.slideMeter = document.getElementById("slideMeter");

      utils.downloadJsonFile(config.topicsFile, null, this.extractTopics);
      this.renderViewsList();
      if (slideShow) slideShow.init();
    }

    renderViewsList() {
      let viewsListBox = document.querySelector(".viewsListBox");

      [...document.querySelectorAll(".view")].forEach((v, i) => {
        [...v.querySelectorAll("h1")].map((x) => {
          let div = document.createElement("div");
          div.innerText = `${("0" + (1+i)).slice(-2)}. ${x.innerText}`;
          viewsListBox.appendChild(div);
        });
      });
    }

    renderSlidesListBox() {
      this.slidesToc.innerHTML = null;
      [...document.querySelectorAll(".slide")].forEach((s, i) => {
        [...s.querySelectorAll("h1")].map((x) => {
          let div = document.createElement("div");
          div.innerText = `${("0" + (1+i)).slice(-2)}. ${x.innerText}`;
          this.slidesToc.appendChild(div);
        });
      });
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
      if (this.currentSlidesFile != this.currentView.name) {
        this.createSlidesInDom(this.currentSlidesFile);
        this.currentSlideId = this.currentView.slideId;
        return;
      }

      // Press [←] while on first slide: hide
      if (this.currentSlideId == 0 && direction == -1) {
        this.toggleSlidesVisibility(false);
        return;
      }
      // Press [→] while slides are not visible: show
      else if (
        !this.slidesVisible &&
        this.currentSlideId == 0 &&
        direction == +1
      ) {
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
    async downloadViewSlides(folder, slideFile) {
      try {
        let relativePath = `${folder}/${slideFile}.md`;
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
          htmlSlides = html.split("<hr />");
        }

        // Configure slide meter [min-value-max]
        this.slideMeter.value = 0;
        this.slideMeter.max = this.slideHasError ? 0 : htmlSlides.length;

        return htmlSlides;
      } catch (e) {
        console.log(`Error in downloadViewSlides(${slideFile})`, e);
      }
    }
    createSlidesInDom() {
      this.deleteExistingSlides();

      this.currentSlidesFile = this.currentView.name;

      this.downloadViewSlides(config.slidesFolder, this.currentSlidesFile).then(
        (htmlSlides) => {
          this.appendSlides(htmlSlides);
          this.slides = document.querySelectorAll(".slide");
          this.toggleSlidesVisibility(true);
          this.renderCurrentSlide();
          PR.prettyPrint();
        }
      );
    }
    appendSlides(slides) {
      slides.forEach((html, i) => {
        const slide = document.createElement("div");
        slide.innerHTML = `<div>${slides[i]}</div>`;
        slide.id = `p${i + 1}`;
        slide.className = "slide";
        document.querySelector("#main").appendChild(slide);
      });
    }
    markdownToHtml(data, useExtensions = true) {
      // Transform md → html
      // useExtensions allow to avoid to trasnform files like help wich can include extensions syntax themselves (so not to render)
      const extensions = useExtensions
        ? {
            extensions: ["BkaShowDownExtension"],
          }
        : null;
      var converter = new showdown.Converter(extensions);
      return converter.makeHtml(data);
    }
    renderCurrentSlide() {
      this.slideMeter.value = this.currentSlideId + 1;
      this.renderViewname();
      this.slides.forEach((s, i) =>
        this.slidesVisible && i == this.currentSlideId
          ? s.classList.add("current")
          : s.classList.remove("current")
      );
      setTableOfContentVisibility(".slide.current", "#slide_toc");
    }

    renderViewname() {
      const slideTitle = this.currentView.name.toUpperCase().replace("_", " ");
      const slideNav = this.slideHasError
        ? "⚠️"
        : ` <sup><small>${this.slideMeter.value}/${this.slides.length}</small></sup>`;
      this.viewName.children[0].innerHTML = `${slideTitle} ${slideNav}`;
      this.renderSlidesListBox();
    }

    toggleSlidesVisibility(forceVisibility) {
      this.HideBlog();

      if (forceVisibility != undefined) this.slidesVisible = forceVisibility;
      else this.slidesVisible = !this.slidesVisible;

      this.slidesVisible
        ? this.viewName.classList.add("visible")
        : this.viewName.classList.remove("visible");

      this.renderCurrentSlide();      
    }

    deleteExistingSlides() {
      if (this.slides.length > 0) this.slides.forEach((s) => s.remove());

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

              let elem = bka.createTopic(link, classes, description);
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
                    tagContent = tagContent.replace(
                      `$${stringToExtract}`,
                      found
                    );
                    tagAnchor.innerHTML = tagContent;
                  } else {
                    tagAnchor.innerHTML += found;
                  }
                  tagAnchor.href = link;
                  tagAnchor.target = "_blank";
                  tagAnchor.className = "topicLink";
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

    HideBlog() {
      this.currentBlog.classList.remove("active");
      setTableOfContentVisibility(".stickyBlog.active", "#slide_toc");
    }

    async ShowBlog(target) {
      try {
        this.currentBlog.classList.toggle("active");
        let response = await fetch(target.href);
        let markdown = await response.text();

        let blogFile = target.getAttribute("blog_file");  
        let blogTitle = blogFile.replace(/(_|\.md)/g, " ");
        let blogDate = "";
        let date = blogFile.match(
          /(?<year>\d{4})-?(?<month>\d{2})-?(?<day>\d{2})-?/
        );
        if (date) {
          blogDate = `${date.groups["day"]}.${date.groups["month"]}.${date.groups["year"]}`;
          blogTitle = blogTitle.replace(date[0], "").toUpperCase();
        }

        const preMarkdown = `<p><a href='${target.tag}' class='blogLinkEdit' title='edit blog' target='_blank'>${blogTitle}<sub class='fs-medium'>  ${blogDate}</sub></a></p>`;
        let html = this.markdownToHtml(`${preMarkdown}${markdown}`);
        this.currentBlog.innerHTML = html;
        setTableOfContentVisibility(
          ".stickyBlog.active",
          "#slide_toc",
          "h1, h2, h3"
        );
      } catch (e) {
        console.log("Error in ShowBlog ", e);
      }
    }
    
    showDownloadedBlogs(filesList) {
      const blogContainer = document.getElementById("blog_items");
      filesList.map((x) => {
        if (x["name"] != 'assets') {            
          let liElement = document.createElement("li");
          let aElement = document.createElement("a");
          
          let date = x["name"].match(/(?<year>\d{4})-?(?<month>\d{2})-?(?<day>\d{2})-?/);
          if (date) {
           let blogDate = `${date.groups["day"]}.${date.groups["month"]}.${date.groups["year"]}  `;            
            let small = document.createElement("small");
            small.innerText = blogDate;
            aElement.appendChild(small);
          }
          
          let blogTitleElement = document.createElement("span");          
          let blogTitle = x["name"].replace(".md", "").replace(/\d{4}-\d\d-\d\d-/, "").replace(/[-_]/g,' ');
          blogTitleElement.innerText = utils.capitalize(blogTitle);
          aElement.appendChild(blogTitleElement);
          aElement.classList = "blogLink"; // To drive the click to ShowBlog( clicked_link )
          aElement.href = x["download_url"];
          aElement.tag = x["html_url"];
          aElement.setAttribute("blog_file", x["name"]);
          
          liElement.appendChild(aElement);
          blogContainer.appendChild(liElement);
        }
      });
    }
   
  }


  function initViews() {
    view_tools_init();
  }

  function initApplication(options, mainContent) {

    document.getElementById("mainContent").innerHTML = mainContent;

    let app = new bka();
    utils.init(app);

    document.addEventListener("mousedown", function (e) {
      app.onMouseDown(e);
    });
    document.addEventListener("mouseup", function (e) {
      app.onMouseUp(e);
    });
    document.addEventListener("keydown", function (e) {
      if (
        utils.alarmVisible ||
        utils.isModalVisible() ||
        e.target.type == "text" ||
        e.target.type == "textarea"
      )
        return; // we need all the keys to enter alarm msg. Exit if on a form input)

      app.onViewKeydown(e);
      if (!e.defaultPrevented) app.onSlideKeydown(e);
    });
    document.addEventListener("click", function (e) {
      
      if (e.target.matches(".slideShowSlidePrev") && slideShow) {
        slideShow.plusSlides(e.target.parentNode.id, -1);
        return;
      } else if (e.target.matches(".slideShowSlideNext") && slideShow) {
        slideShow.plusSlides(e.target.parentNode.id, 1);
        return;
      } else if (e.target.matches(".slideShowDot")) {
        slideShow.currentSlide(e.target.parentNode.parentNode.id, e.target.getAttribute('data-dotSpan'));        
      }
      else if (e.target.parentNode.matches(".blogLink") || e.target.matches(".blogLink")) {
        // Click a blog link
        e.preventDefault();
        
        if (e.target.parentNode.matches(".blogLink"))
          app.ShowBlog(e.target.parentNode);      
        else
          app.ShowBlog(e.target);      
      }             
      else if (e.target.matches(".copy")) {
        utils.copyToClipboard(e.target.innerText);
      } else if (
        e.target.matches(`${config.viewsCssSelector}.active`) ||
        e.target.parentNode.matches(
          `${config.viewsCssSelector}.active, .topics`
        )
      ) {
        // Click on empty element => close opened windows (alarm, blog)
        app.HideBlog();
        if (utils.alarmVisible) utils.alarmOpenClose();
      } else if (e.target.matches("#help")) {
        if (utils.isModalVisible()) utils.modalClose();
        else {
          // show help
          utils.downloadTextFile(
            "help.md",
            null,
            function (options, helpContent) {
              const helpContainer = document.createElement("div");
              helpContainer.classList = "bkahelp";
              helpContainer.innerHTML = app.markdownToHtml(helpContent, false);
              utils.modalShow("HELP", helpContainer);
            }
          );
        }
      } else if (e.target.className == "modalContainer visible") {
        // click on the modalContainer to close it
        utils.modalClose();
      } else if (
        e.target.matches("#clock") ||
        e.target.matches("#alarm") ||
        (utils.alarmVisible && e.target.className == "active view")
      ) {
        utils.alarmOpenClose();
      } else if (e.target.matches(".alarmItem")) {
        // alarm already set ? → Cancel it
        if (e.target.classList.contains("alarm-active")) {
          utils.alarmSet(0);
          return;
        }

        // set alarm
        const alarmSelected = document.querySelector(".alarmMessage");
        const alarmReason = alarmSelected.value || "";
        const alarmDurationMin = e.target.getAttribute("data-duration");
        e.target.classList.toggle("alarm-active");
        utils.alarmOpenClose();
        utils.snackbar(`Alarm in ${alarmDurationMin} min<br/>${alarmReason}`);
        utils.speak(`Alarm in ${alarmDurationMin} min`);
        utils.alarmSet(alarmDurationMin, alarmReason);
      }
    });

    initViews();
    
    if (showdown) showdown.setFlavor("github");
    if (slideShow) slideShow.showSlides();

    utils.fetchMasonry(".topics", config.masonryColumns);
    utils.fetchGithubRepo(config.blogRepoApi, app.showDownloadedBlogs);
  }
  


  document.addEventListener("DOMContentLoaded", function () {
    utils.downloadTextFile("index-main.html", null, initApplication);
  });

})();