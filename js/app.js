import * as assets from "./addons.js"

( function() {
	
const getTime = () => new Date().toLocaleTimeString();

const config = {
  mouseDownDurationForCopySec: 3,
};
class bka {
  currentView = null;
  views = []; // [{ id:0, dom: null, name: '', slideId: 0 }, …]
  viewName = null;
  viewMeter = null;
  currentSlideId = 0;
  currentSlidesFile = null;
  slidesVisible = null;
  slides = [];
  slidesFolder = "";

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
    this.viewMeter = document.getElementById("viewMeter");
    utils.downloadJsonFile("assets/topics.json", this.extractTopics);
  }

  heartbeat() {
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
      this.currentView.slideId = this.currentSlideId + 1; // memo thz slide id to retrieve after anothers view navigation and come back
    } else {
      switch (e.keyCode) {
        case 37: // left arrow key
          this.changeSlide(-1);
          break;
        case 39: // right arrow key
          this.changeSlide(+1);
          break;
        case 70: // f key
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
    else if (!this.slidesVisible && this.currentSlideId == 0 && direction == +1) {
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
      if (!response.ok)
        markdown = markdown.replace(relativePath, `${relativePath} ⚠️`);
      const html = this.markdownToHtml(markdown);
      const htmlSides = html.split("<hr />");
      
      // slides meter
	    this.viewMeter.value = 0;
	    this.viewMeter.max = response.ok ? htmlSides.length : 1e5;
      
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
  this.viewMeter.value = this.currentSlideId+1;
  this.viewName.childNodes[0].innerHTML = `${this.currentView.name}'s slides <sup><small>${this.currentSlideId+1}/${this.slides.length}</small></sup>`;
  this.slides.forEach((s, i) =>
      this.slidesVisible && i == this.currentSlideId
        ? s.classList.add("current")
        : s.classList.remove("current")
    );
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

  extractTopics(topics, callback) {
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

  static createTopic(link, classes, description) {
    const prefix =
      (classes || "block").indexOf("inline") >= 0 ? "inline" : "block";
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

  init: function(context=null) {
	this.externalHeartbeat = context.heartbeat.bind(context);
    setInterval( () => this.heartbeat(), 1000);    
  },

  heartbeat: function() {
	this.clock.innerText = getTime();
	if (this.externalHeartbeat != null) 
		this.externalHeartbeat();
    if (this.alarmTimer) {
      this.alarmRemainder -= this.alarmRate;
      this.alarmSign.style.width = `${Math.trunc(this.alarmRemainder)}%`;
    }
  },

  copyToClipboard: async function (stringToCopy, show=null) {
    try {
      await navigator.clipboard.writeText(stringToCopy);
      this.snackbar(`copied ${show==true ? stringToCopy : ''}`);
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

  downloadJsonFile: async function (file, callback) {
    try {
      let response = await fetch(file);
      let jsonData = await response.json();
      callback(jsonData);
    } catch (e) {
      console.log(`downloadJsonFile: error: ${file}`, e);
    }
  },
  downloadTextFile: function (file, callback) {
    try {
      fetch(file)
        .then((resp) => {
          return resp.text();
        })
        .then(function (text) {
          callback(text);
        });
    } catch (e) {
      console.log(`downloadTextFile: error: ${file}`, e);
    }
  }

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

        // let res = downloadTextFile("readme.md", function(res) {
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

  btoa(text);
  atob(text);  

}


