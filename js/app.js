( function() {
	
const getTime = () => new Date().toLocaleTimeString();

const config = {
  mouseDownDurationForCopySec: 3,
};
class bka {
  currentView = null;
  views = []; // [{ id:0, dom: null, name: '', slideId: 0 }, …]  slideId allow to retrieve the last slide viewed before leaving the view
  viewName = null;

  currentSlideId = 0;
  currentSlidesFile = null;
  slidesFolder = "";
  slideHasError = false;
  slidesVisible = null;
  slides = [];
  slideMeter = null;

  isMouseDown = false;
  mouseDownTime = null;

  constructor(slidesFolder, viewsSelector) {
    document
      .querySelectorAll(viewsSelector)
      .forEach((v, i) =>
        this.views.push({ id: i, name: v.id, dom: v, slideId: 0 })
      );
    this.currentView = this.views[0];
    this.slidesFolder = slidesFolder;

    this.viewName = document.getElementById("viewName");
    this.slideMeter = document.getElementById("slideMeter");
    utils.downloadJsonFile("assets/topics.json", null, this.extractTopics);
  }

  tick() {
    if (!this.isMouseDown) return;

    const mouseDownDurationSec = (new Date() - this.mouseDownTime) / 1000;
    if (config.mouseDownDurationForCopySec <= mouseDownDurationSec) {
      utils.copyToClipboard(document.getSelection());
      this.mouseDownTime = new Date();
    }
  }

  scrollTo(y = 0) {
    document.documentElement.scrollTo({ top: y, behavior: "smooth" });
  }

  onViewKeydown(e) {
    if (e.shiftKey) return;

    let key = e.key.toLowerCase();

    // Navigate in views by [+] or [CTRL + →]
    if (e.key == "+" || (e.ctrlKey && e.keyCode == 39) /*right*/) {
      this.currentView = this.views[
        this.views.length <= this.currentView.id + 1
          ? 0
          : this.currentView.id + 1
      ];
      key = this.currentView.name.slice(0, 3);
    }
    // Navigate in views by "-" or [CTRL + ←]
    else if (e.key == "-" || (e.ctrlKey && e.keyCode == 37) /*left*/) {
      this.currentView = this.views[
        this.currentView.id - 1 < 0
          ? this.views.length - 1
          : this.currentView.id - 1
      ];
      key = this.currentView.name.slice(0, 3);
    } else if (e.ctrlKey || ![...this.views].some((v) => v.name[0] == key))
      return; // no key match a view name

    e.preventDefault();
    this.scrollTo(0);
    // hide slides
    this.toggleSlidesVisibility(false);
    // display view
    this.views.forEach((view) =>
      view.name.slice(0, key.length) == key
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
          this.changeSlide(-1);
          break;
        case 39: // [→] key
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
      this.scrollTo(0);
      this.toggleSlidesVisibility(true);
      return;
    }

    this.currentSlideId += direction;
    if (this.slides.length <= this.currentSlideId) this.currentSlideId = 0;
    else if (this.currentSlideId < 0) this.currentSlideId = 0;

    this.scrollTo(0);
    this.toggleSlidesVisibility(true);
  }
  async downloadViewSlides(folder, slideFile) {
    try {
      let relativePath = `${folder}/${slideFile}.md`;
      let response = await fetch(relativePath);
      let markdown = await response.text();
      let html = null;
      let htmlSides = null;
      this.slideHasError = !response.ok;
      if (this.slideHasError) {
        htmlSides = [
          `⚠️ ${response.statusText} (${response.status}): ${relativePath}`,
        ];
      } else {
        html = this.markdownToHtml(markdown);
        htmlSides = html.split("<hr />");
      }

      // Configure slide meter [min-value-max]
      this.slideMeter.value = 0;
      this.slideMeter.max = this.slideHasError ? 0 : htmlSides.length;

      return htmlSides;
    } catch (e) {
      console.log(`Error in downloadViewSlides(${slideFile})`, e);
    }
  }
  createSlidesInDom() {
    this.deleteExistingSlides();

    this.currentSlidesFile = this.currentView.name;

    this.downloadViewSlides(this.slidesFolder, this.currentSlidesFile).then(
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
  markdownToHtml(data) {
    // Transform md → html
    var converter = new showdown.Converter({
      extensions: ["BkaShowDownExtension"],
    });
    return converter.makeHtml(data);
  }
  renderCurrentSlide() {
    this.slideMeter.value = this.currentSlideId + 1;
    const slideTitle = `${this.currentView.name}'s slides`;
    const slideNav = this.slideHasError
      ? "⚠️"
      : ` <sup><small>${this.slideMeter.value}/${this.slides.length}</small></sup>`;
    this.viewName.childNodes[0].innerHTML = `${slideTitle} ${slideNav}`;
    this.slides.forEach((s, i) =>
      this.slidesVisible && i == this.currentSlideId
        ? s.classList.add("current")
        : s.classList.remove("current")
    );
    initToc();
  }
  toggleSlidesVisibility(forceVisibility) {
    if (forceVisibility != undefined) this.slidesVisible = forceVisibility;
    else this.slidesVisible = !this.slidesVisible;

    // ViewName animation
    this.viewName.childNodes[0].innerText = `${this.currentView.name}'s slides`;
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

        if (jsonObject.error) {
          tag.innerHTML += " ❌";
          tag.title = jsonObject.error;
          return;
        }

        // Look for variables prefixed by '$' 
        // http://ip-api.com/json/[!getjson](my lat/lon: $lat $lon)
        const regex = /(?<=\$)\w*/g; 
        let variablesFound = description.match(regex);
        if (variablesFound != null) {          
          let tagContent = description;
          
          variablesFound.forEach((stringToExtract) => {
            options[3].jsonExplorer(jsonObject, stringToExtract, 
              
              function (found) {
                if (tagContent.indexOf(stringToExtract) >= 0) {
                  tagContent = tagContent.replace(`$${stringToExtract}`, found);
                  tag.innerHTML = tagContent;
                } 
                else 
                  tag.innerHTML += found;
                tag.title = link + (cronInterval == null ? "" : `${cronInterval}`);
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
        tag.innerHTML = jsonObject;
        tag.title = link;
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
    if (description) apiElement.innerHTML = description;

    switch (typeOfCall) {
      case "json":
        // Look for cron defined by !getjsonxxx   xx… = digit[s]
        // http://ip-api.com/json/[!getjson =lat =lon](my lat/lon: $lat $lon)    single call
        // http://ip-api.com/json/[!getjson60 =lat =lon](my lat/lon: $lat $lon)  call every 60 sec
        let cronInterval = classes.match(/(?<=!getjson)\d+/);
        let enrichedDescription = description;
        if (cronInterval != null) {
          enrichedDescription = [description, `. Fetch frequency: ${cronInterval[0]} sec`];
          setInterval(() => {
            this.createTopicFromApiWithJson( hash, link, classes, enrichedDescription ); 
          }, cronInterval[0] * 1000);                            
        } 

        this.createTopicFromApiWithJson( hash, link, classes, enrichedDescription );
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

let utils = {
  clock: document.querySelector("#clock"),

  snackbar: document.getElementById("snackbar"),

  modalContainer: document.querySelector(".modalContainer"),
  modalContent: document.getElementById("modalContent"),
  modalTitle: document.getElementById("modalTitle"),

  alarm: document.getElementById("alarm"),
  alarmSign: document.getElementById("alarmSign"),
  alarmTimer: null,
  alarmReason: 0,
  alarmVisible: false,
  alarmRate: 0,
  alarmRemainder: 0,
  externalHeartbeat: null,

  init: function (context = null) {
    this.externalHeartbeat = context.tick.bind(context);
    setInterval(() => this.tick(), 1000);
  },

  tick: function () {
    this.clock.innerText = getTime();
    if (this.externalHeartbeat != null) this.externalHeartbeat();
    if (this.alarmTimer) {
      this.alarmRemainder -= this.alarmRate;
      this.alarmSign.style.width = `${Math.trunc(this.alarmRemainder)}%`;
    }
  },

  getHash: (str) => window.btoa(str),

  copyToClipboard: async function (stringToCopy, show = null) {
    try {
      await navigator.clipboard.writeText(stringToCopy.toString());
      this.snackbar(`copied ${show == true ? stringToCopy : ""}`);
    } catch (err) {
      console.error(`Failed to copy ${stringToCopy}`, err);
    }
  },

  isModalVisible: function () {
    return this.modalContainer.classList.contains("visible");
  },

  modalShow: function (title, content) {
    this.modalTitle.innerText = title;
    this.modalContent.querySelectorAll("*").forEach((n) => n.remove());
    this.modalContent.appendChild(content);
    this.modalContainer.classList.add("visible");
  },

  modalClose: function () {
    this.modalContainer.classList.remove("visible");
  },

  alarmOpenClose: function () {
    this.alarm.classList.toggle("alarm");
    this.alarmVisible = this.alarm.classList.contains("alarm");
  },

  alarmSet: function (minutes, reason) {
    if (minutes == 0) {
      clearTimeout(this.alarmTimer);
      const msg = `Alarm canceled: ${this.alarmReason}`;
      document
        .querySelector(".alarmItem.alarm-active")
        .classList.remove("alarm-active");
      this.speak(msg);
      this.snackbar(msg);
      this.alarmSign.classList.remove("active");
      this.alarmRate = 0;
      return;
    }

    // Start Countdown
    this.alarmSign.classList.add("active");
    this.alarmRemainder = 100;
    this.alarmRate = 100 / (minutes * 60); // rate at wich, each sec, thecountdown progressbar must be reduced

    this.alarmReason = reason;
    this.alarmTimer = setTimeout(() => {
      const msg = `Alarm (${minutes} min elapsed)<br/>${
        reason != "" ? '"' + reason + '"' : ""
      }`;
      this.snackbar(msg, 5000);
      if (msg.trim().slice(0, 2) != "//")
        // dot not speak msg prefixed by //
        this.speak(msg.replace("<br/>", ""));
      document
        .querySelector(".alarmItem.alarm-active")
        .classList.remove("alarm-active");
      this.alarmSign.classList.remove("active");
    }, minutes * 60 * 1000);
  },

  speak: function (msg) {
    if (msg != "" && window.speechSynthesis) {
      var to_speak = new SpeechSynthesisUtterance(msg);
      window.speechSynthesis.speak(to_speak);
    }
  },

  snackbar: function (msg, duration = 2500) {
    snackbar.innerHTML = msg;
    snackbar.classList.add("show");
    setTimeout(() => snackbar.classList.remove("show"), duration);
  },

  fullScreen: function (elem) {
    const request =
      elem.requestFullscreen ||
      elem.webkitRequestFullScreen ||
      elem.mozRequestFullScreen ||
      elem.msRequestFullscreen;
    request.call(elem);
  },

  downloadJsonFile: async function (file, options, callback) {
    let response = null;
    let jsonData = null;
    try {
      response = await fetch(file);
      jsonData = await response.json();
    } catch (e) {
      let error = null;
      if (response)
        error = `${file} FAILED - ${response.status} - ${response.statusText} / ${e}`;
      else
        error = `Error with ${file}: ${e}`;      
      
      console.log(`downloadJsonFile: ${error}`);
      jsonData = {'error': error};
    }
    finally {
      callback(options, jsonData);
    }
  },
  downloadTextFile: function (file, options, callback) {
    try {
      fetch(file)
        .then((resp) => {
          return resp.text();
        })
        .then(function (text) {
          callback(options, text);
        });
    } catch (e) {
      console.log(`downloadTextFile: error: ${file}`, e);
    }
  },
};





document.addEventListener("DOMContentLoaded", function () {
	
	let app = new bka("assets/slides", ".view");
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
    if (e.target.matches(".copy")) {
      utils.copyToClipboard(e.target.innerText);
    } else if (e.target.matches("#help")) {
      if (utils.isModalVisible()) utils.modalClose();
      else {
        // show help

        // let res = downloadTextFile("readme.md", null, function(data, res) {
        // 	const instance = document.createElement("div");
        // 	instance.innerHTML = application.markdownToHtml(res);
        // 	utils.modalShow("HELP", instance);
        // });

        const fragment = document.getElementById("helpTemplate");
        const instance = document.importNode(fragment.content, true);
        utils.modalShow("HELP", instance);
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

  // INIT CUSTOMIZED VIEWS	
  view_tools_init();

  if (showdown) 
  	showdown.setFlavor("github");  
});

})();

/* CUSTOMIZE VIEWS */ 

function view_tools_init() {
  document.querySelector("#timestamp").value = Math.floor( new Date().getTime() / 1000.0 );
  document.querySelector("#timestampDecode").value = Math.floor( new Date().getTime() / 1000.0 );
  document.querySelector("#timestampEncode").value = new Date().toISOString();

  var b64PlainText = document.getElementById("b64PlainText");
  var b64EncodedText = document.getElementById("b64EncodedText");
  document.getElementById("b64Encode").addEventListener("click", function () {
    b64EncodedText.value = btoa(b64PlainText.value);
  });
  document.getElementById("b64Decode").addEventListener("click", function () {
    b64PlainText.value = atob(b64EncodedText.value);
  });

  
  /* Regex */
  var regexPattern = document.getElementById("regexPattern");
  var regexInput = document.getElementById("regexInput");
  var regexOutput = document.getElementById("regexOutput");
 
  regexPattern.addEventListener("keydown", e => parseRegex());
  regexInput.addEventListener("keydown", e => parseRegex());

  function regexMatch(input, expression, flags = "g") {
    let regex = expression instanceof RegExp ? expression : new RegExp(expression, flags);
    let matches = input.matchAll(regex);
    matches = [...matches];
    return matches.map((item) => {
      return {
        match: item[0],
        matchAtIndex: item.index,
        capturedGroups: item.length > 1 ? item.slice(1) : undefined,
      };
    });
  }

  function parseRegex() {
    try {
      let flags = '';
      [...document.querySelectorAll(".regex")].map((r) => { 
        if (r.checked) 
          flags += r.nextSibling.nodeValue[0]
      });
      const regex = new RegExp(regexPattern.value, flags);
      let matches = regexMatch(regexInput.value, regex);
      regexOutput.value = `Flags: ${flags}\r\n` +JSON.stringify(matches)
          .replace(/(?<sep>["}],)/g, "$1\r\n")
          .replace(/]},/g, "]},\r\n");                                  
    }
    catch(e){
      regexOutput.value = `Error Regex ${e}`;        
    }

  }
  
  /* Drag-Drop image */

  const canvas = document.getElementById("b64Canvas");
  const context = canvas.getContext("2d");
  initCanvas(context);

  function initCanvas(ctx) {    
    ctx.fillStyle = "#FFEB3B";
    ctx.font = "16px Courier";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText('Drop image here', 100, 10);
  }
  function imageError(img) {
    img.src = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";    
  }

  function createImage() {
     const image = new Image();
     image.crossOrigin = "Anonymous";
     image.onload = () => {
       context.drawImage(image, 0, 0, 200, 150);
     };
     return image; 
  }


  const onImageDrop = (e) => {
    e.preventDefault();

    let imageFile = null;
     if (e.dataTransfer.files.length > 0) {
       imageFile = e.dataTransfer.files[0];
     } else {
       imageFile = e.dataTransfer.getData("URL");
       
       fetch(imageFile)
         .then((response) => response.blob())
         .then(function (myBlob) {
           imageFile = URL.createObjectURL(myBlob);           
           const image = createImage();   
           image.src = imageFile;           
           b64EncodedText.value = canvas.toDataURL();
         });
         return;
     }


    const imageReader = new FileReader();
    imageReader.onload = (imageFile) => {      
      const image = createImage();            
      image.src = imageFile.target.result;
       if (image.complete || image.complete === undefined) {
         imageError(image);
       }
    };
    imageReader.readAsDataURL(imageFile);
    b64EncodedText.value = canvas.toDataURL();
  };

  canvas.addEventListener("dragover", (e) => e.preventDefault(), false);
  canvas.addEventListener("drop", onImageDrop, false);  
}






















async function initToc() {
  // Part 1
  const currentSlide = document.querySelector(".slide.current");
  const slideToc = document.querySelector("#slide_toc");
  if (!currentSlide) {           
    slideToc.classList.remove("current");
    return;
  }

  slideToc.classList.add("current");

  // Part 2
  const $headings = [...currentSlide.querySelectorAll("h1, h2")];
  const linkHtml = generateLinkMarkup($headings);
  slideToc.innerHTML = linkHtml;

  // Part 3
  const $links = [...slideToc.querySelectorAll("a")];
  const observer = createObserver($links);
  $headings.map((heading) => observer.observe(heading));

  // Part 4
  const motionQuery = window.matchMedia("(prefers-reduced-motion)");
  $links.map((link) => {
    link.addEventListener("click", (evt) =>
      handleLinkClick(evt, $headings, motionQuery)
    );
  });
}


function generateLinkMarkup($headings) {
  console.log($headings);
  const parsedHeadings = $headings.map((heading) => {
    return {
      title: heading.innerText,
      depth: heading.nodeName.replace(/\D/g, ""),
      id: heading.getAttribute("id"),
    };
  });
  const htmlMarkup = parsedHeadings.map(
    (h) => `
  <li class="${h.depth > 1 ? "pl-1" : ""}">
    <a href="#${h.id}">${h.title}</a>
  </li>
  `
  );
  const finalMarkup = `
    <ul>${htmlMarkup.join("")}</ul>
  `;
  return finalMarkup;
}

function updateLinks(visibleId, $links) {
  $links.map((link) => {
    let href = link.getAttribute("href");
    link.classList.remove("active-title");
    if (href === visibleId) link.classList.add("active-title");
  });
}

function handleObserver(entries, observer, $links) {
  entries.forEach((entry) => {
    const { target, isIntersecting, intersectionRatio } = entry;
    if (isIntersecting && intersectionRatio >= 1) {
      const visibleId = `#${target.getAttribute("id")}`;
      updateLinks(visibleId, $links);
    }
  });
}

function createObserver($links) {
  const options = {
    rootMargin: "0px 0px 0px 0px", // rootMargin: target area limits = top of viewport here
    threshold: 1,
  };

  const callback = (e, o) => handleObserver(e, o, $links);
  return new IntersectionObserver(callback, options);
}

function handleLinkClick(evt, $headings, motionQuery) {
  evt.preventDefault();
  let id = evt.target.getAttribute("href").replace("#", "");
  let section = $headings.find((heading) => heading.getAttribute("id") === id);
  section.setAttribute("tabindex", -1);
  section.focus();

  window.scroll({
    behavior: motionQuery.matches ? "instant" : "smooth",
    top: section.offsetTop - 20,
  });
}