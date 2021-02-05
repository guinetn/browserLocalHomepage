  // used by renderChaptersCatalog() & renderBooksCatalog()
  function renderCatalog(
    source,
    target,
    itemsAttribute,
    itemsClass,
    clearTarget = false,
    numbering_start = 1
  ) {
    const catalog = document.querySelector(target);
    if (clearTarget) catalog.innerHTML = null;

    source.forEach((s, i) => {
      [...s.querySelectorAll("h1")].map((x, j) => {
        let div = document.createElement("div");
        if (j > 0)
          // sub-chapter
          div.innerHTML = `&nbsp; &nbsp; └─${"─".repeat(j)} ${x.innerText}`;
        else div.innerText = `${("0" + (numbering_start + i)).slice(-2)} ${x.innerText}`;
        div.setAttribute(itemsAttribute, i);
        div.className = itemsClass;
        catalog.appendChild(div);
      });
    });
  }
  
// Show/Hide catalog
// Complex catalog (+IntersectionObserver to sync scroll/current catalog)  
async function renderScrollSyncCatalog(
  sourceElement,
  catalogContainer,
  htmlElementToCatalog = "h1, h2, h3"
) {
  const source = document.querySelector(sourceElement);
  const catalog = document.querySelector(catalogContainer);
  if (!source) {
    catalog.classList.remove("current");
    return;
  }

  catalog.classList.add("current");

  const catalogItems = [...source.querySelectorAll(htmlElementToCatalog)];
  const linkHtml = generateLinkMarkup(catalogItems);
  catalog.innerHTML = linkHtml;

  const links = [...catalog.querySelectorAll("a")];
  const observer = createObserver(links);
  catalogItems.map((heading) => observer.observe(heading));

  const motionQuery = window.matchMedia("(prefers-reduced-motion)");
  links.map((link) => {
    link.addEventListener("click", (evt) => handleLinkClick(evt, catalogItems, motionQuery));
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
