/* CUSTOMIZE BOOKS */

function tools_init() {
  document.querySelector("#timestamp").value = Math.floor(
    new Date().getTime() / 1000.0
  );
  document.querySelector("#timestampDecode").value = Math.floor(
    new Date().getTime() / 1000.0
  );
  document.querySelector("#timestampEncode").value = new Date().toISOString();

  var b64PlainText = document.getElementById("b64PlainText");
  var b64EncodedText = document.getElementById("b64EncodedText");
  document.getElementById("b64Encode").addEventListener("click", function () {
    b64EncodedText.value = btoa(b64PlainText.value);
  });
  document.getElementById("b64Decode").addEventListener("click", function () {
    b64PlainText.value = atob(b64EncodedText.value);
  });

  /* Regex */
  var regexPattern = document.getElementById("regexPattern");
  var regexInput = document.getElementById("regexInput");
  var regexOutput = document.getElementById("regexOutput");

  regexPattern.addEventListener("keydown", (e) => parseRegex());
  regexInput.addEventListener("keydown", (e) => parseRegex());

  function regexMatch(input, expression, flags = "g") {
    let regex =
      expression instanceof RegExp ? expression : new RegExp(expression, flags);
    let matches = input.matchAll(regex);
    matches = [...matches];
    return matches.map((item) => {
      return {
        match: item[0],
        matchAtIndex: item.index,
        capturedGroups: item.length > 1 ? item.slice(1) : undefined,
      };
    });
  }

  function parseRegex() {
    try {
      let flags = "";
      [...document.querySelectorAll(".regex")].map((r) => {
        if (r.checked) flags += r.nextSibling.nodeValue[0];
      });
      const regex = new RegExp(regexPattern.value, flags);
      let matches = regexMatch(regexInput.value, regex);
      regexOutput.value =
        `Flags: ${flags}\r\n` +
        JSON.stringify(matches)
          .replace(/(?<sep>["}],)/g, "$1\r\n")
          .replace(/]},/g, "]},\r\n");
    } catch (e) {
      regexOutput.value = `Error Regex ${e}`;
    }
  }

  /* Drag-Drop image */

  const canvas = document.getElementById("b64Canvas");
  const context = canvas.getContext("2d");
  initCanvas(context);

  function initCanvas(ctx) {
    ctx.fillStyle = "#FFEB3B";
    ctx.font = "16px Courier";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("Drop image here", 100, 10);
  }
  function imageError(img) {
    img.src =
      "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";
  }

  function createImage() {
    const image = new Image();
    image.crossOrigin = "Anonymous";
    image.onload = () => {
      context.drawImage(image, 0, 0, 200, 150);
    };
    return image;
  }

  const onImageDrop = (e) => {
    e.preventDefault();

    let imageFile = null;
    if (e.dataTransfer.files.length > 0) {
      imageFile = e.dataTransfer.files[0];
    } else {
      imageFile = e.dataTransfer.getData("URL");

      fetch(imageFile)
        .then((response) => response.blob())
        .then(function (myBlob) {
          imageFile = URL.createObjectURL(myBlob);
          const image = createImage();
          image.src = imageFile;
          b64EncodedText.value = canvas.toDataURL();
        });
      return;
    }

    const imageReader = new FileReader();
    imageReader.onload = (imageFile) => {
      const image = createImage();
      image.src = imageFile.target.result;
      if (image.complete || image.complete === undefined) {
        imageError(image);
      }
    };
    imageReader.readAsDataURL(imageFile);
    b64EncodedText.value = canvas.toDataURL();
  };

  canvas.addEventListener("dragover", (e) => e.preventDefault(), false);
  canvas.addEventListener("drop", onImageDrop, false);
}
