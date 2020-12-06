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
	showdown.extension('BkaCodeExtension', function () {
    ("use strict");

    let getHash = (str) => window.btoa(str);

    let downloadTextFile = async function (file, hash, converter=null) {
      try {
        const response = await fetch(file);
		let res = await response.text();
		if (converter!=null)
			res = converter.makeHtml(res);
        document.getElementById(hash).innerHTML = res;
      } catch (e) {
        console.log(`downloadTextFile: error: ${file}`, e);
      }
	};
	
    // download.md(assets/slides/code.md)
    // download.div(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // download.code(https://raw.githubusercontent.com/mortennobel/cpp-cheatsheet/master/cheatsheet-as-sourcefile.cpp)
    // var converter = new showdown.Converter({extensions: ["BkaCodeExtension"],
    // 	<script src="js/showdown.extension.bka.js"></script>

    var bkaDivRegex = /(?:download\.)(?<bkatype>div)\((?<link>[^)]*)\)/g,
      bkaCodeRegex = /(?:download\.)(?<bkatype>code)\((?<link>[^)]*)\)/g,
      bkaMdRegex = /(?:download\.)(?<bkatype>md)\((?<link>[^)]*)\)/g;

    var bkaMdExt = {
      type: "lang",
      filter: function (text, converter, options) {
			return text.replace(bkaMdRegex, function (s, bkatype, link) {
			var hash = getHash(link);
			downloadTextFile(link, hash, converter);
			return `<div id='${hash}'></div>`;
			});
		}
	};
	
    var bkaDivExt = {
      type: "lang",
      regex: bkaDivRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadTextFile(link, hash);
        return `<div id='${hash}'></div>`;
      },
    };

    var bkaCodeExt = {
      type: "lang",
      regex: bkaCodeRegex,
      replace: function (s, bkatype, link) {
        var hash = getHash(link);
        downloadTextFile(link, hash);
        return `<strong><code><pre id='${hash}'></pre></code</strong>`;
      },
    };

    return [bkaMdExt, bkaDivExt, bkaCodeExt];
  });
});
