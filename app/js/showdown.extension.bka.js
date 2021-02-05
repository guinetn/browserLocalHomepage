import { config } from "./config.js";
/*
SHOWDOWN Extensions

USAGE:
  download.md(assets/books/code.md)
  download.page(code.md) : automatically prefix the link with 'assets/books'
  download.html(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.html)
  download.raw(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
  download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
  download.exec(assets/books/computer_science/assets/show_ascii_table.js)
  download.iframe(url,[w,h]) :
  download.iframe(assets/books/web/front/react_samples/react01/index.html)
  download.iframe(assets/books/web/front/react_samples/react01/index.html,500,200)
  
  download.slideshow('assets/books/code/langs/c++/c++01.md')

  [video title](https://www.youtube.com/watch?xyzabc)  --> <iframe src="//www.youtube.com/embed/xyzabc" frameborder="0" allowfullscreen=""></iframe>
  setup:[The Map of Physics](ZihywtixUYo)
  <script src="js/showdown.extension.bka.js"></script>
  var converter = new showdown.Converter({extensions: ["BkaShowDownExtension"])

  Writing showdown extensions: https://github.com/showdownjs/showdown/wiki/Extensions
*/

(function (extension) {
  "use strict";

  // Use it from backend or frontend
  if (typeof showdown !== "undefined") {
    extension(showdown);
  } else if (typeof define === "function" && define.amd) {
    define(["showdown"], extension);
  } else if (typeof exports === "object") {
    module.exports = extension(require("showdown"));
  } else {
    throw Error("Could not find showdown library");
  }
})(
	function (showdown) {

    // Register showdown extensions
    showdown.extension("BkaShowDownExtension", function () {
      ("use strict");

      let getHash = (str) => window.btoa(str);

      let promisedMarker = (hash, link) =>
        `<div data-type='promised_file' id='${hash}'>waiting for…${link}</div>`;
      let promisedSlideShowMarker = (hash, link) =>
        `<div class='slideShowContainer' data-type='promised_slideshow' id='${hash}'></div>`;

      let replaceMarker = function (hash, htmlData, textData) {
        // Warn bka that the DOM has changed
        window.postMessage(
          {
            reason: "chapters changed",
            hash: hash,
            htmlData: htmlData,
            textData: textData,
          },
          "*"
        );
      };

      let downloadFile = async function (file, hash, converter, callback) {
        try {
          const response = await fetch(file);
          let res = await response.text();
          callback(res, file, converter);
        } catch (e) {
          console.log(`Showdown extension bka: downloadFile error: ${file}`, e);
        }
      };

      function addAttribute(attributeName, value, suffix) {
        return value == null ? "" : `${attributeName}='${value}${suffix}'`;
      }

      // EXTENSIONS

      var bkaRawRegex = /(?:download\.)(?<bkatype>raw)\((?<link>[^)]*)\)/gi,
        bkaSlideShowRegex = /(?:download\.)(?<bkatype>slideshow)\((?<link>[^)]*)\)/gi,
        bkaHtmlRegex = /(?:download\.)(?<bkatype>html)\((?<link>[^)]*)\)/gi,
        bkaCodeRegex = /(?:download\.)(?<bkatype>code)\((?<link>[^)]*)\)/gi,
        bkaExecCodeRegex = /(?:download\.)(?<bkatype>exec)\((?<link>[^)]*)\)/gi,
        bkaMdRegex = /(?:download\.)(?<bkatype>md)\((?<link>[^)]*)\)/gi,
        bkaMdPageRegex = /(?:download\.)(?<bkatype>page)\((?<link>[^)]*)\)/gi,
        bkaIFrameRegex = /(?:download\.)(?<bkatype>iframe)\((?<link>.*?) ?(?: ?, ?(?<width>\d{0,4}) ?, ?(?<height>\d{0,4}) ?)?\)/gi,
        bkaPrettyPrintRegex = /(<pre[^>]*>)?[\n\s]?<code([^>]*)>/gi,
        bkaYoutubeRegex = /<a href="(?:(?:https?:)?(?:\/\/)?)(?:(?:www)?\.)?youtube\.(?:.+?)\/(?:(?:watch\?v=)|(?:embed\/))(?<videoid>[a-zA-Z0-9_-]{11})(?:[^"'])*(?:"|')+\s*>(?<videotitle>[^<]*)/gi;

      /*
      in: <a href='……youtube……'> : any link containing 'youtube' 
      out: <iframe src='//www.youtube.com/embed/...
      */
      var bkaYoutubeExtension = {
        type: "output",
        regex: bkaYoutubeRegex,
        replace: function (s, videoid, videotitle) {
          return `<table class='youtube'>
                  <tr>
                    <td>
                       <iframe src='//www.youtube.com/embed/${videoid}' frameborder='0' allowfullscreen></iframe>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <a href='${videotitle}' rel='noopener' target='_blank'>${videotitle}</a>
                    </td>
                  </tr>
                </table>`;
        },
      };

      /*
      in: download.md(assets/books/code.md)
      out: target.innerHTML will receive the markdown source file converted in html
      */
      var bkaDownloadMarkdownExtension = {
        type: "lang",
        filter: function (text, converter, options) {
          return text.replace(bkaMdRegex, function (s, bkatype, link) {
            var hash = getHash(link);
            downloadFile(
              link,
              hash,
              converter,
              function (res, file, converter) {
                replaceMarker(hash, converter.makeHtml(res));
              }
            );
            return promisedMarker(hash, link);
          });
        },
      };

      /*
      idem  download.md() but looks for a file in 'assets/books'
      in: download.page(/code.md). ~ bkaDownloadMarkdownExtension but looks for the file in 'assets/books'
      out: out: target.innerHTML will receive the markdown source file converted in html
      */
      var bkaDownloadMarkdownChapterExtension = {
        type: "lang",
        filter: function (text, converter, options) {
          return text.replace(bkaMdPageRegex, function (s, bkatype, link) {
            var hash = getHash(link);
            downloadFile(
              `assets/books/${link}`,
              hash,
              converter,
              function (res, file, converter) {
                replaceMarker(hash, converter.makeHtml(res));
              }
            );
            return promisedMarker(hash, link);
          });
        },
      };

      /*
      in:download.iframe(url,[w,h]) :
      out: <iframe src='${link}' [width=…, height=…]
      */
      var bkaDownloadIframeExtension = {
        type: "lang",
        filter: function (text, converter, options) {
          return text.replace(
            bkaIFrameRegex,
            function (s, bkatype, link, width, height) {
              return `<iframe src='${link}'  ${addAttribute(
                "width",
                width,
                "px"
              )} ${addAttribute("height", height, "px")}></iframe>`;
            }
          );
        },
      };

      /*
      in: download.raw(https://...)
      out:  target.innerText will receive the file contant as it is (raw, not prettified)
      */
      var bkaDownloadRawExtension = {
        type: "lang",
        regex: bkaRawRegex,
        replace: function (s, bkatype, link) {
          var hash = getHash(link);
          downloadFile(link, hash, null, function (res, file) {
            replaceMarker(hash, null, res);
          });
          return promisedMarker(hash, link);
        },
      };

      /* Create a slide show from a file. The slides separator is ::::
      in: download.slideshow(assets/books/code/langs/cpp/cpp01.md)
          Ex: slide 1 :::: slide 2 :::: slide 3....        
      out:
        <div class="slideShowContainer">
          <div class="slideShowSlide">slide 1</div>
          <div class="slideShowSlide">slide 2</div>
          ...
       */
      var bkaDownloadSlideShowExtension = {
        type: "lang",        
        filter: function (text, converter, options) {
          return text.replace(bkaSlideShowRegex, function (s, bkatype, link) {                  
          var hash = getHash(link);
          downloadFile(link, hash, converter, function (res, file, converter) {
            var slideShow = document.getElementById(hash);

            var slides = res.split(config.chaptersSeparator); // slides separator is ::::
            slides.forEach((part) => {
              var htmlPart = converter.makeHtml(part);
              var slide = document.createElement("div");
              slide.className = "slideShowSlide";
              slide.innerHTML = htmlPart; //`<pre><code>${htmlPart}</code></pre>`;
              slideShow.appendChild(slide);
            });
          });
          return promisedSlideShowMarker(hash, link);
          })      
      }};
      
      /*
      in: download.html(assets/code/code.html)
      out: target.innerHTML will receive the file content as it is
      */
      var bkaDownloadHtmlExtension = {
        type: "lang",
        regex: bkaHtmlRegex,
        replace: function (s, bkatype, link) {
          var hash = getHash(link);
          downloadFile(link, hash, null, function (res, file) {
            replaceMarker(hash, res);
          });
          return promisedMarker(hash, link);
        },
      };

      /*
      in: download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
      out: target.innerHTML will receive the file content prettyfied according the file extension
      */
      var bkaDownloadCodeExtension = {
        type: "lang",
        regex: bkaCodeRegex,
        replace: function (s, bkatype, link) {
          var hash = getHash(link);
          downloadFile(link, hash, null, function (res, file) {
            const filExt = file.substring(file.length - 3, file.length);
            let resCode = `<p><a title='download item' class='originOfLink' rel='noopener' target='_blank' href='${file}'>${file}</a></p><?prettify ...?><pre><code id='${hash}' class='language-${filExt}'>${res}</code></pre>`;
            replaceMarker(hash, resCode);
            PR.prettyPrint();
          });
          return promisedMarker(hash, link);
        },
      };

      /*
      in: download.exec(assets/books/computer_science/assets/show_ascii_table.js)
      out: will evaluate the file as a javascript code
      */
      var bkaExecCodeRegexExtension = {
        type: "lang",
        regex: bkaExecCodeRegex,
        replace: function (s, bkatype, link) {
          var hash = getHash(link);
          downloadFile(link, hash, null, function (res, file) {
            let scriptElement = document.getElementById(hash);
            scriptElement.innerText = res;
            eval(res);
          });
          return `<script id='${hash}'></script>`;
        },
      };

      /* DRAFT
      in: <pre><code>....</code></pre>
      out: <pre class='prettyprint linenums'><code>...</code></pre>
      */
      var bkaPrettyPrintExtension = {
        type: "output",
        regex: bkaPrettyPrintRegex,
        replace: function (s, pre, codeClass) {
          return pre
            ? `<pre class='prettyprint linenums'><code ${codeClass}>`
            : `<code class='prettyprint'>`;
        },
      };

      return [
        bkaDownloadMarkdownExtension,
        bkaDownloadMarkdownChapterExtension,
        bkaDownloadRawExtension,
        bkaDownloadSlideShowExtension,
        bkaDownloadCodeExtension,
        bkaDownloadIframeExtension,
        bkaDownloadHtmlExtension,
        bkaExecCodeRegexExtension,
        bkaPrettyPrintExtension,
        bkaYoutubeExtension,
      ];
    });
  });
