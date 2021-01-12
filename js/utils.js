import { config } from "./config.js";

export let utils = {
  getTime: () => new Date().toLocaleTimeString(),

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
    this.clock.innerText = this.getTime();
    if (this.externalHeartbeat != null) this.externalHeartbeat();
    if (this.alarmTimer) {
      this.alarmRemainder -= this.alarmRate;
      this.alarmSign.style.width = `${Math.trunc(this.alarmRemainder)}%`;
    }
  },

  scrollTo: function (y = 0, behaviour = "smooth") {
    document.documentElement.scrollTo({ top: y, behavior: behaviour });
  },

  getHash: (str) => window.btoa(str),

  capitalize: (string) => string[0].toUpperCase() + string.slice(1),

  parseDate: function (stringDate) {
    let date = stringDate.match(/(?<year>\d{4})-?(?<month>\d{2})-?(?<day>\d{2})-?/);
    return date
      ? {
          source: date[0],
          day: date.groups["day"],
          month: date.groups["month"],
          year: date.groups["year"],
        }
      : null;
  },

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
    this.modalTitle.innerHTML = title;
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

  snackbar: function (msg, duration = config.snackbarDurationSec) {
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
      else error = `Error with ${file}: ${e}`;

      console.log(`downloadJsonFile: ${error}`);
      jsonData = { error: error };
    } finally {
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

  setMasonry: function (container, cols) {
    var masonryWrapper = container.parentNode;
    var masonryItems = container.children;
    container.parentNode.removeChild(container);

    // <div id='xxx_topics' class='masonry-layout column-x'>
    var newContainer = document.createElement("div");
    newContainer.setAttribute("id", `${masonryWrapper.id}_topics`),
      newContainer.classList.add("masonry-layout", "topics", "columns-" + cols),
      masonryWrapper.appendChild(newContainer);

    /* <div class='masonry-column-1'>
        <div class='masonry-column-2'>
        ...
      */
    for (var col = 1; col <= cols; col++) {
      var divColumn = document.createElement("div");
      divColumn.classList.add("masonry-column-" + col);
      newContainer.appendChild(divColumn);
    }

    // Assign topic's subjects to columns
    var col = 1;
    [...masonryItems].forEach(function (r) {
      newContainer
        .querySelector(`#${newContainer.id} > .masonry-column-${col}`)
        .appendChild(r);
      col = col < cols ? col + 1 : 1;
    });
  },

  fetchMasonry: function (container, cols) {
    [...document.querySelectorAll(container)].map((c) => {
      this.setMasonry(c, cols);
    });
  },

  fetchGithubFolder: async function (repo, callback) {
    this.downloadJsonFile(repo, null, function (options, filesList) {
      callback(filesList);
    });
  },
};
