import { utils } from "./utils.js";

export class Blog {
  currentBlog = null;

  constructor(blogArticleContainer) {
    this.currentBlog = document.querySelector(blogArticleContainer);
  }

  hideBlog() {
    this.currentBlog.classList.remove("active");
    renderScrollSyncCatalog(".blogArticleContainer.active", ".blogCatalog");
  }
  
  async showBlog(blogLink) {
    try {
      let blogFile = blogLink.getAttribute("blog_file");

      // Click the same / click out => hide blog
      if (blogFile == this.currentBlog.getAttribute("data-blog_file")) {
        this.currentBlog.classList.toggle("active");
        return;
      }

      if (!this.currentBlog.classList.contains("active"))
        this.currentBlog.classList.toggle("active");
      let response = await fetch(blogLink.href);
      let markdown = await response.text();

      let blogTitle = blogFile.replace(/(_|\.md)/g, " ");
      let blogDate = "";
      let date = utils.parseDate(blogFile);
      if (date) {
        blogDate = `${date.day}.${date.month}.${date.year}`;
        blogTitle = blogTitle.replace(date.source, "").toUpperCase();
      }

      const preMarkdown = `<p><a href='${blogLink.tag}' class='blogArticleLinkEdit' title='edit blog' rel='noopener' target='_blank'>${blogTitle}<sub class='fs-medium'>  ${blogDate}</sub></a></p>`;
      let html = this.markdownToHtml(`${preMarkdown}${markdown}`);
      this.currentBlog.innerHTML = html;
      this.currentBlog.setAttribute("data-blog_file", blogFile);
      renderScrollSyncCatalog(
        ".blogArticleContainer.active",
        ".blogCatalog",
        "h1, h2, h3"
      );
    } catch (e) {
      console.log("Error in showBlog ", e);
    }
  }

  listBlogArticles(articlesFiles) {
    const blogContainer = document.getElementById("blog_articles");
    // Clean blog articles container
    blogContainer.querySelectorAll("*").forEach((s) => s.remove());

    articlesFiles.map((article) => {
      if (article["name"] != "assets") {
        // Article = <li><a href=article_url>article Title
        let ArticleLI = document.createElement("li");
        let articleA = document.createElement("a");

        let date = utils.parseDate(article["name"]);
        if (date) {
          let articleDate = `${date.day}.${date.month}.${date.year}  `;
          let small = document.createElement("small");
          small.innerText = articleDate;
          articleA.appendChild(small);
        }

        let articleTitleElement = document.createElement("span");
        let articleTitle = article["name"]
          .replace(".md", "")
          .replace(/\d{4}-\d\d-\d\d-/, "")
          .replace(/[-_]/g, " ");
        articleTitleElement.innerText = utils.capitalize(articleTitle);
        articleA.appendChild(articleTitleElement);
        articleA.classList = "blogArticleLink"; // To drive the click to showBlog( clicked_link )
        articleA.href = article["download_url"];
        articleA.tag = article["html_url"];
        articleA.setAttribute("blog_file", article["name"]);

        ArticleLI.appendChild(articleA);
        blogContainer.appendChild(ArticleLI);
      }
    });
  }
}