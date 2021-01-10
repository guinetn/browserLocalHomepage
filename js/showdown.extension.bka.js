import { config } from "./config.js";


(function (extension) {
  "use strict";

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
          
	showdown.extension('BkaShowDownExtension', function () {
    ("use strict");

    let getHash = (str) => window.btoa(str);
    let promisedFileContainer = (hash, link) => `<div data-type='promised_file' id='${hash}'>wanting for…${link}</div>`;
    let replaceHash = function(hash, htmlData, textData) {
      const slideContainer = document.getElementById(hash);
      
      let div = document.createElement("div");      
      if (htmlData) div.innerHTML = htmlData;
      else div.innerText = textData;
      
      let prevNode = slideContainer.previousElementSibling;
      if (prevNode && config.slidesSeparator.test(prevNode.outerHTML)) {
        while (prevNode != null) {
          if (prevNode.classList.contains("slides")) {
            div.className = "slide";
            prevNode.insertAdjacentElement("beforeEnd", div);
            slideContainer.previousElementSibling.remove(); // remove <p>::::</p>
            break;
          }
          prevNode = prevNode.parentNode;
        }
      } else {
        slideContainer.parentNode.appendChild(div);
      }
      slideContainer.remove();
      // Warn bka that dom has changed      
      window.postMessage('slides changed', '*');
    }
    
    let downloadFile = async function (file, hash, converter, callback) {
      try {
        const response = await fetch(file);
        let res = await response.text();
        callback(res, file, converter);
      } catch (e) {
        console.log(`Showdown extension bka: downloadTextFile: error: ${file}`, e);
      }
    };

    // usage:
    // download.md(assets/slides/code.md)
    // download.html(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.html)
    // download.raw(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // download.exec(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // download.iframe(url,[w,h]) :
    //    download.iframe(assets/slides/web/front/react_samples/react01/index.html)
    //    download.iframe(assets/slides/web/front/react_samples/react01/index.html,500,200)
    //
    // [video title](https://www.youtube.com/watch?xyzabc)  --> <iframe src="//www.youtube.com/embed/xyzabc" frameborder="0" allowfullscreen=""></iframe>
    // setup:[The Map of Physics](ZihywtixUYo)
    // <script src="js/showdown.extension.bka.js"></script>
    // var converter = new showdown.Converter({extensions: ["BkaShowDownExtension"])

    var bkaRawRegex = /(?:download\.)(?<bkatype>raw)\((?<link>[^)]*)\)/gi,
      bkaHtmlRegex = /(?:download\.)(?<bkatype>html)\((?<link>[^)]*)\)/gi,
      bkaCodeRegex = /(?:download\.)(?<bkatype>code)\((?<link>[^)]*)\)/gi,
      bkaExecCodeRegex = /(?:download\.)(?<bkatype>exec)\((?<link>[^)]*)\)/gi,
      bkaMdRegex = /(?:download\.)(?<bkatype>md)\((?<link>[^)]*)\)/gi,
      bkaIFrameRegex = /(?:download\.)(?<bkatype>iframe)\((?<link>.*?) ?(?: ?, ?(?<width>\d{0,4}) ?, ?(?<height>\d{0,4}) ?)?\)/gi,
      bkaPrettyPrintRegex = /(<pre[^>]*>)?[\n\s]?<code([^>]*)>/gi,
      bkaYoutubeRegex = /<a href="(?:(?:https?:)?(?:\/\/)?)(?:(?:www)?\.)?youtube\.(?:.+?)\/(?:(?:watch\?v=)|(?:embed\/))(?<videoid>[a-zA-Z0-9_-]{11})(?:[^"'])*(?:"|')+\s*>(?<videotitle>[^<]*)/gi;

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

    var bkaDownloadMarkdownExtension = {
      type: "lang",
      filter: function (text, converter, options) {
        return text.replace(bkaMdRegex, function (s, bkatype, link) {
          var hash = getHash(link);
          downloadFile(link, hash, converter, function (res, file, converter) {
            //document.getElementById(hash).innerHTML = converter.makeHtml(res);
            replaceHash(hash, converter.makeHtml(res));            
          });
          return promisedFileContainer(hash, link);
        });
      },
    };

    function addAttribute(attributeName, value, suffix) {
      return value == null ? "" : `${attributeName}='${value}${suffix}'`;
    }
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

    var bkaDownloadRawExtension = {
      type: "lang",
      regex: bkaRawRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadFile(link, hash, null, function (res, file) {          
          replaceHash(hash, null, res);                      
        });
        return promisedFileContainer(hash, link);
      },
    };

    var bkaDownloadHtmlExtension = {
      type: "lang",
      regex: bkaHtmlRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadFile(link, hash, null, function (res, file) {
          replaceHash(hash, res);
        });
        return promisedFileContainer(hash, link);
      },
    };

    var bkaDownloadCodeExtension = {
      type: "lang",
      regex: bkaCodeRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadFile(link, hash, null, function (res, file) {
          const filExt = file.substring(file.length - 3, file.length);
          let resCode = `<p><a title='download item' class='originOfLink' rel='noopener' target='_blank' href='${file}'>${file}</a></p><?prettify ...?><pre><code id='${hash}' class='language-${filExt}'>${res}</code></pre>`;
          replaceHash(hash, resCode);                      
          PR.prettyPrint();
        });
        return promisedFileContainer(hash, link);
      },
    };

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
      bkaDownloadRawExtension,
      bkaDownloadCodeExtension,
      bkaDownloadIframeExtension,
      bkaDownloadHtmlExtension,
      bkaExecCodeRegexExtension,
      bkaPrettyPrintExtension,
      bkaYoutubeExtension,
    ];
  });
});
