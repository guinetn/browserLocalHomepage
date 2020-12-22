async function setTableOfContentVisibility(
  source,
  tocContainer,
  elementToToc = "h1, h2"
) {
  // Part 1  ".slide.current", "#slide_toc"
  const currentSource = document.querySelector(source);
  const ToC = document.querySelector(tocContainer);
  if (!currentSource) {
    ToC.classList.remove("current");
    return;
  }

  ToC.classList.add("current");

  const $tocs = [...currentSource.querySelectorAll(elementToToc)];
  const linkHtml = generateLinkMarkup($tocs);
  ToC.innerHTML = linkHtml;

  const $links = [...ToC.querySelectorAll("a")];
  const observer = createObserver($links);
  $tocs.map((heading) => observer.observe(heading));

  const motionQuery = window.matchMedia("(prefers-reduced-motion)");
  $links.map((link) => {
    link.addEventListener("click", (evt) =>
      handleLinkClick(evt, $tocs, motionQuery)
    );
  });
}

function generateLinkMarkup($headings) {
  const parsedHeadings = $headings.map((heading) => {
    return {
      title: heading.innerText,
      depth: heading.nodeName.replace(/\D/g, ""),
      id: heading.getAttribute("id"),
    };
  });
  const htmlMarkup = parsedHeadings.map(
    (h) => `
  <li class="${h.depth > 1 ? "pl-1" : ""}">
    <a href="#${h.id}">${h.title}</a>
  </li>
  `
  );
  const finalMarkup = `
    <ul>${htmlMarkup.join("")}</ul>
  `;
  return finalMarkup;
}

function updateLinks(visibleId, $links) {
  $links.map((link) => {
    let href = link.getAttribute("href");
    link.classList.remove("active-title");
    if (href === visibleId) link.classList.add("active-title");
  });
}

function handleObserver(entries, observer, $links) {
  entries.forEach((entry) => {
    const { target, isIntersecting, intersectionRatio } = entry;
    if (isIntersecting && intersectionRatio >= 1) {
      const visibleId = `#${target.getAttribute("id")}`;
      updateLinks(visibleId, $links);
    }
  });
}

function createObserver($links) {
  const options = {
    rootMargin: "0px 0px 0px 0px", // rootMargin: target area limits = top of viewport here
    threshold: 1,
  };

  const callback = (e, o) => handleObserver(e, o, $links);
  return new IntersectionObserver(callback, options);
}

function handleLinkClick(evt, $headings, motionQuery) {
  evt.preventDefault();
  let id = evt.target.getAttribute("href").replace("#", "");
  let section = $headings.find((heading) => heading.getAttribute("id") === id);
  section.setAttribute("tabindex", -1);
  section.focus();

  window.scroll({
    behavior: motionQuery.matches ? "instant" : "smooth",
    top: section.offsetTop - 20,
  });
}
