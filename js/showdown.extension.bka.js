/*! showdown-youtube 14-09-2017 */
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

    let downloadFile = async function (file, hash, converter, callback) {
      try {
        const response = await fetch(file);
        let res = await response.text();
        callback(res, file, converter);
      } catch (e) {
        console.log(`downloadTextFile: error: ${file}`, e);
      }
    };

    // usage:
    // download.md(assets/slides/code.md)
    // download.html(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.html)
    // download.raw(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // [video title](https://www.youtube.com/watch?xyzabc)  --> <iframe src="//www.youtube.com/embed/xyzabc" frameborder="0" allowfullscreen=""></iframe>
    // setup:[The Map of Physics](ZihywtixUYo)
    // <script src="js/showdown.extension.bka.js"></script>
    // var converter = new showdown.Converter({extensions: ["BkaShowDownExtension"])

    var bkaRawRegex = /(?:download\.)(?<bkatype>raw)\((?<link>[^)]*)\)/gi,
      bkaHtmlRegex = /(?:download\.)(?<bkatype>html)\((?<link>[^)]*)\)/gi,
      bkaCodeRegex = /(?:download\.)(?<bkatype>code)\((?<link>[^)]*)\)/gi,
      bkaMdRegex = /(?:download\.)(?<bkatype>md)\((?<link>[^)]*)\)/gi,
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
                      <a href='${videotitle}' target='_blank'>${videotitle}</a>
                    </td>
                  </tr>
                </table>`;
      }
    };

    var bkaDownloadMarkdownExtension = {
      type: "lang",
      filter: function (text, converter, options) {
        return text.replace(bkaMdRegex, function (s, bkatype, link) {
          var hash = getHash(link);
          downloadFile(link, hash, converter, function (res, file, converter) {
            document.getElementById(hash).innerHTML = converter.makeHtml(res);
          });
          return `<div id='${hash}'></div>`;
        });
      },
    };

    var bkaDownloadRawExtension = {
      type: "lang",
      regex: bkaRawRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadFile(link, hash, null, function (res, file) {
          document.getElementById(hash).innerText = res;
        });
        return `<div id='${hash}'></div>`;
      },
    };

    var bkaDownloadHtmlExtension = {
      type: "lang",
      regex: bkaHtmlRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadFile(link, hash, null, function (res, file) {
          document.getElementById(hash).innerHTML = res;
        });
        return `<div id='${hash}'></div>`;
      },
    };

    var bkaDownloadCodeExtension = {
      type: "lang",
      regex: bkaCodeRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadFile(link, hash, null, function (res, file) {
          const filExt = file.substring(file.length - 3, file.length);
          let resCode = `<p><a title='download item' class='originOfLink' target='_blank' href='${file}'>${file}</a></p><?prettify ...?><pre><code id='${hash}' class='language-${filExt}'>${res}</code></pre>`;
          document.getElementById(hash).innerHTML = resCode;
          PR.prettyPrint();
        });
        return `<div id='${hash}'></div>`;
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
      bkaPrettyPrintExtension,
      bkaYoutubeExtension,
    ];
  });
});
