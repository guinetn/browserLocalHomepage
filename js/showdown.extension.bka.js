/*
SHOWDOWN Extensions

USAGE:
  download.md(assets/slides/code.md)
  download.html(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.html)
  download.raw(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
  download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
  download.exec(assets/slides/computer_science/assets/show_ascii_table.js)
  download.iframe(url,[w,h]) :
  download.iframe(assets/slides/web/front/react_samples/react01/index.html)
  download.iframe(assets/slides/web/front/react_samples/react01/index.html,500,200)

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
      
      let promisedMarker = (hash, link) => `<div data-type='promised_file' id='${hash}'>waiting for…${link}</div>`;
      
        let replaceMarker = function (hash, htmlData, textData) {        
        // Warn bka that the DOM has changed
        window.postMessage( {
            reason: "slides changed",
            hash: hash,
            htmlData: htmlData,
            textData:textData,
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
          console.log(`Showdown extension bka: downloadTextFile: error: ${file}`, e);
        }
      };

      // EXTENSIONS
    
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

      function addAttribute(attributeName, value, suffix) {
        return value == null ? "" : `${attributeName}='${value}${suffix}'`;
      }
      var bkaDownloadIframeExtension = {
        type: "lang",
        filter: function (text, converter, options) {
          return text.replace(
            bkaIFrameRegex,
            function (s, bkatype, link, width, height) {
              return `<iframe src='${link}'  ${addAttribute( "width", width, "px" )} ${addAttribute("height", height, "px")}></iframe>`;
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
            replaceMarker(hash, null, res);
          });
          return promisedMarker(hash, link);
        },
      };

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
