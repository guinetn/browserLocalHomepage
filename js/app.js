import { config } from "./config.js";
import { Bka } from "./bka.js";
import { utils } from "./utils.js";
import { slideShow } from "./slideshow.js";

( function() {
  let app = null;

  document.addEventListener("DOMContentLoaded", function () {
    utils.downloadTextFile("index-main.html", null, initApplication);
  });

  // INIT CUSTOMIZED VIEWS
  function initApplication(options, mainContent) {
    document.getElementById("mainContent").innerHTML = mainContent;

    app = new Bka();
    utils.init(app);

    document.addEventListener("mousedown", onMouseDown);
    document.addEventListener("mouseup", onMouseUp);
    document.addEventListener("keydown", onKeydown);
    document.addEventListener("click", onClick);
    window.addEventListener("message", dispatchEvents);

    // INIT VIEWS WITH CUSTOM FUNCTIONS
    tools_init();

    // Configure
    if (showdown) showdown.setFlavor("github");
    if (slideShow) slideShow.showSlides();

    utils.fetchMasonry(".topics", config.masonryColumns);
    utils.fetchGithubFolder(config.blogRepoApi, app.listBlogArticles);
  }

  function showHelp() {
    
    utils.downloadTextFile("help.md", null, function (options, helpContent) {
      const helpContainer = document.createElement("div");
      helpContainer.classList = "bkahelp";
      let help = app.markdownToHtml(helpContent, false);
      // Replace elements '##xxxxx##' by their values from 'config' object
      const sharps = [...help.matchAll(/##(?<SHARP>[^#]*)##/gi)].map(
        (x) => x.groups["SHARP"]
      );
      sharps.forEach(
        (x) => (help = help.replace(`##${x}##`, `${x}: ${config[x]}`))
      );
      helpContainer.innerHTML = help;
      utils.modalShow(`BKA help`, helpContainer);
    });
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

  function onKeydown(e) {
    if (
      utils.alarmVisible ||
      utils.isModalVisible() ||
      e.target.type == "text" ||
      e.target.type == "textarea"
    )
      return; // we need all the keys to enter alarm msg. Exit if on a form input)

    app.onViewKeydown(e);
    if (!e.defaultPrevented) app.onSlideKeydown(e);
  }

  function onClick(e) {
    if (e.target.matches(".slideShowSlidePrev") && slideShow) {
      slideShow.plusSlides(e.target.parentNode.id, -1);
      return;
    } else if (e.target.matches(".slideShowSlideNext") && slideShow) {
      slideShow.plusSlides(e.target.parentNode.id, 1);
      return;
    } else if (e.target.matches(".slideShowDot")) {
      slideShow.currentSlide(
        e.target.parentNode.parentNode.id,
        e.target.getAttribute("data-dotSpan")
      );
    } else if (
      e.target.parentNode.matches(".blogLink") ||
      e.target.matches(".blogLink")
    ) {
      // Click a blog link
      e.preventDefault();

      const target = e.target.parentNode.matches(".blogLink")
        ? e.target.parentNode
        : e.target;
      app.showBlog(target);
    } else if (e.target.matches(".copy")) {
      utils.copyToClipboard(e.target.innerText);
    } else if (
      e.target.matches(`${config.viewsCssSelector}.active`) ||
      e.target.parentNode.matches(`${config.viewsCssSelector}.active, .topics`)
    ) {
      // Click on empty element => close opened windows (alarm, blog)
      app.hideBlog();
      if (utils.alarmVisible) utils.alarmOpenClose();
    } 
    else if (e.target.matches(".slideTocLink")) {
      // Slides ToC clicked: navigate to clicked slide
      app.showSlide(e.target.dataset.slideid);
    } else if (e.target.matches("#help")) {
      if (utils.isModalVisible()) utils.modalClose();
      else {
        showHelp();
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
  }
})();