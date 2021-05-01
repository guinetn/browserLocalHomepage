import React from "https://cdn.skypack.dev/react";
import ReactDOM from "https://cdn.skypack.dev/react-dom";

function App() {
  return (
    React.createElement("div", { className: "box" },
    React.createElement("h1", null, "Hello World")));
}

ReactDOM.render(React.createElement(App, null), document.getElementById("root"));