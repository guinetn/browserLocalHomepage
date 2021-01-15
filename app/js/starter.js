import { config } from "./config.js";
import { App } from "./app.js";
import { utils } from "./utils.js";
import { slideShow } from "./slideshow.js";

// Init the application
( function() {
  let app = null;

  document.addEventListener("DOMContentLoaded", function () {
    utils.downloadTextFile(config.viewsFile, null, initApplication);
  });

  // INIT CUSTOMIZED VIEWS
  function initApplication(options, viewsContent) {
    document.querySelector(config.viewsContainer).innerHTML = viewsContent;

    app = new App();
    utils.init(app);

    listenForEvents();
    initViews();
    initComponents();
    setTopicsLayout();
    loadBlogArticles();
  }

  // Manage app events (keyboard, mouse)
  function listenForEvents() {
    document.addEventListener("mousedown", onMouseDown);
    document.addEventListener("mouseup", onMouseUp);
    document.addEventListener("keydown", onKeydown);
    document.addEventListener("click", onClick);
    window.addEventListener("message", dispatchEvents);
  }
  // Configure app's components:showdown (md), slideshow
  function initComponents() {
    if (showdown) showdown.setFlavor("github");
    if (slideShow) slideShow.showSlides();
  }

  // Some views require an initialization
  function initViews() {
    tools_init();
  }

  // Init the layout of the 'topics' part of each view
  function setTopicsLayout() {
    // Each view has a <div class="topics"> containing the topics
    // Set the masonry layout to each view 'topics' element
    utils.setMasonryLaout(".topics", config.masonryColumns);
  }

  function loadBlogArticles() {
    utils.fetchGithubFolder(config.blogRepoApi, app.listBlogArticles);
  }

  function showHelp() {
    utils.downloadTextFile(
      "app/help.md",
      null,
      function (options, helpContent) {
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
      }
    );
  }

  function dispatchEvents(e) {
    app.slidesChanged(e);
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

    // Send key events to the app view and slide
    app.keydownEvent(e);
  }

  // Manage app's clicks events
  function onClick(e) {
    if (reloadBlogArticles(e)) return;
    else if (slideShowEvents(e)) return;
    else if (showBlogArticle(e)) return;
    else if (copyAction(e)) return;
    else if (emptyClickToClose(e)) return;
    else if (openView(e)) return;
    else if (slideNavigation(e)) return;
    else if (helpClicked(e)) return;
    else if (closeModal(e)) return;
    else if (showAlarmsPanel(e)) return;
    else alarmChosen(e);
  }
  
  // Refresh blog articles
  function reloadBlogArticles(e) {
    if (!e.target.matches(".articlesReloadLink")) return false;

    loadBlogArticles();
    return true;
  }

  function slideShowEvents(e) {
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
        e.target.getAttribute("data-dotSpan")
      );
      return true;
    }

    return false;
  }

  // Click a blog article
  function showBlogArticle(e) {
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
    app.showBlog(target);
    return true;
  }

  function copyAction(e) {
    if (!e.target.matches(".copy")) return false;

    utils.copyToClipboard(e.target.innerText);
    return true;
  }

  // Click on empty element => close opened windows (alarm, blog)
  function emptyClickToClose(e) {
    if (
      !(
        e.target.matches(`${config.viewsCssSelector}.active`) ||
        e.target.parentNode.matches(
          `${config.viewsCssSelector}.active, .topics`
        )
      )
    )
      return false;
    app.hideBlog();
    if (utils.alarmVisible) utils.alarmOpenClose();

    return true;
  }

  function openView(e) {
    if (!e.target.matches(".viewsCatalogLink")) return false;

    const linkWidthAreaToOpenSlides = 35;
    app.selectViewAndOpenSlide(
      e.target.dataset.viewid,
      e.offsetX < linkWidthAreaToOpenSlides
    );
    return false;
  }

  function slideNavigation(e) {
    if (!e.target.matches(".slideCatalogLink")) return false;
    // Slides ToC clicked: navigate to clicked slide
    app.showSlide(e.target.dataset.slideid);
    return true;
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

  function showAlarmsPanel(e) {
    if (
      !(
        e.target.matches("#clock") ||
        e.target.matches("#alarm") ||
        (utils.alarmVisible && e.target.className == "active view")
      )
    )
      return false;

    utils.alarmOpenClose();
    return true;
  }

  function alarmChosen(e) {
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
    utils.snackbar(`Alarm in ${alarmDurationMin} min<br/>${alarmReason}`);
    utils.speak(`Alarm in ${alarmDurationMin} min`);
    utils.alarmSet(alarmDurationMin, alarmReason);

    return true;
  }

  // TOUCH EVENTS
  let touchStart = undefined;
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
        app.selectView(vector.x / Math.abs(vector.x) == -1 ? "prev" : "next");
      touchStart = undefined;
    },
    false
  );
})();