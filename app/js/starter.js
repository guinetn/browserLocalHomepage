import { config } from "./config.js";
import { App } from "./app.js";
import { utils } from "./utils.js";
import { slideShow } from "./slideshow.js";

// Init the application
( function() {
  let app = null;
  let touchStart = undefined;

  // Get books file (visual parts of the app)
  document.addEventListener("DOMContentLoaded", function () {
    utils.downloadTextFile(config.booksFile, null, initApplication);
  });

  function initApplication(options, booksLoaded) {
    document.querySelector(config.booksContainer).innerHTML = booksLoaded;

    app = new App();
    utils.init();
    utils.addHeartBeat(app);

    listenForEvents();
    initBooks();
    initComponents();
    setTopicsLayout();
  }

  // Manage app events (keyboard, mouse)
  function listenForEvents() {
    document.addEventListener("mousedown", onMouseDown);
    document.addEventListener("mouseup", onMouseUp);
    document.addEventListener("keydown", onKeydown);
    document.addEventListener("click", onClick);
    window.addEventListener("message", dispatchEvents);
    startTouchEvents();
  }
  // Configure app's components:showdown (converter markdown to html), slideshow
  function initComponents() {
    if (showdown) showdown.setFlavor("github");
    if (slideShow) slideShow.showSlides();
    if (hljs) hljs.initHighlightingOnLoad();
  }

  // Some books require an initialization
  function initBooks() {
    tools_init();
  }

  // Init the layout of the 'topics' part of each book
  function setTopicsLayout() {
    // Each book has a <div class="topics"> containing the topics
    // Set the masonry layout to each book's 'topics' element
    utils.setMasonryLaout(".topics", config.masonryColumns);
  }

  function showHelp() {
    utils.downloadTextFile(config.help, null, function (options, helpContent) {
      const helpContainer = document.createElement("div");

      let help = app.markdownToHtml(helpContent, false);
      // Get help elements ##xxxxx## to replace with configuration values
      const sharps = [...help.matchAll(/##(?<SHARP>[^#]*)##/gi)].map(
        (x) => x.groups["SHARP"]
      );
      // Replace '##xxxxx##' by their values from 'config'
      sharps.forEach(
        (x) => (help = help.replace(`##${x}##`, `${x}: ${config[x]}`))
      );
      helpContainer.innerHTML = help;
      utils.modalShow(`BKA help`, helpContainer);
    });
  }

  function dispatchEvents(e) {
    app.chaptersChanged(e);
  }

  function onMouseDown(e) {
    app.onMouseDown(e);
  }

  function onMouseUp(e) {
    app.onMouseUp(e);
  }

  // Manage key down for the app
  function onKeydown(e) {
    // Avoid side effects of keys listeners on regular html controls or for some app's status
    if (
      utils.alarmVisible ||
      utils.isModalVisible() ||
      e.target.type == "text" ||
      e.target.type == "textarea"
    )
      return;

    // Send key events to the app book and slide
    app.keydownEvent(e);
  }

  // Manage app's clicks events
  function onClick(e) {
    if (helpClicked(e)) return;
    else if (closeModal(e)) return;
    else app.onClick(e);
  }

  function helpClicked(e) {
    if (!e.target.matches("#help")) return false;

    if (utils.isModalVisible()) utils.modalClose();
    else showHelp();

    return true;
  }

  // click on the modalContainer to close it
  function closeModal(e) {
    if (e.target.className != "modalContainer visible") return false;
    utils.modalClose();
    return true;
  }

  // start touch events
  function startTouchEvents(e) {
    addEventListener(
      "touchstart",
      (event) => {
        touchStart = {
          x: event.changedTouches[0].clientX,
          y: event.changedTouches[0].clientY,
        };
      },
      false
    );

    addEventListener(
      "touchend",
      (event) => {
        touchStart = undefined;
      },
      false
    );

    addEventListener(
      "touchmove",
      (event) => {
        if (touchStart == undefined) return;
        const vector = {
          x: touchStart.x - event.changedTouches[0].clientX,
          y: touchStart.y - event.changedTouches[0].clientY,
        };
        const horizontal = Math.abs(vector.x) > Math.abs(vector.y);
        let back = horizontal ? vector.x < 0 : vector.y < 0;
        if (horizontal)
          app.selectBook(vector.x / Math.abs(vector.x) == -1 ? "prev" : "next");
        touchStart = undefined;
      },
      false
    );
  }
})();