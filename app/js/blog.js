import { utils } from "./utils.js";

export class Blog {
  currentBlog = null;

  constructor(blogArticlePlaceHolder) {
    this.currentBlog = document.getElementById(blogArticlePlaceHolder);
  }

  hideBlog() {
    this.currentBlog.classList.remove("active");
    setTableOfContentVisibility(".stickyBlogArticle.active", "#catalog");
  }

  async showBlog(target) {
    try {
      let blogFile = target.getAttribute("blog_file");
      
      // Click the same / click out => hide blog
      if (blogFile == this.currentBlog.getAttribute("data-blog_file")) {
        this.currentBlog.classList.toggle("active");        
        return;      
      }
      
      if (! this.currentBlog.classList.contains('active'))
        this.currentBlog.classList.toggle('active');      
      let response = await fetch(target.href);
      let markdown = await response.text();

      let blogTitle = blogFile.replace(/(_|\.md)/g, " ");
      let blogDate = "";
      let date = utils.parseDate(blogFile);      
      if (date) {
        blogDate = `${date.day}.${date.month}.${date.year}`;
        blogTitle = blogTitle.replace(date.source, "").toUpperCase();
      }

      const preMarkdown = `<p><a href='${target.tag}' class='blogArticleLinkEdit' title='edit blog' rel='noopener' target='_blank'>${blogTitle}<sub class='fs-medium'>  ${blogDate}</sub></a></p>`;
      let html = this.markdownToHtml(`${preMarkdown}${markdown}`);
      this.currentBlog.innerHTML = html;
      this.currentBlog.setAttribute("data-blog_file", blogFile);
      setTableOfContentVisibility(
        ".stickyBlogArticle.active",
        "#catalog",
        "h1, h2, h3"
      );
    } catch (e) {
      console.log("Error in showBlog ", e);
    }
  }

  listBlogArticles(filesList) {
    
    const blogContainer = document.getElementById("blog_items");
    // Clean blog items
    blogContainer.querySelectorAll("*").forEach((s) => s.remove());
    
    filesList.map((x) => {
      if (x["name"] != "assets") {
        let liElement = document.createElement("li");
        let aElement = document.createElement("a");

        let date = utils.parseDate(x["name"]);      
        if (date) {                          
          let blogDate = `${date.day}.${date.month}.${date.year}  `;
          let small = document.createElement("small");
          small.innerText = blogDate;
          aElement.appendChild(small);
        }

        let blogTitleElement = document.createElement("span");
        let blogTitle = x["name"]
          .replace(".md", "")
          .replace(/\d{4}-\d\d-\d\d-/, "")
          .replace(/[-_]/g, " ");
        blogTitleElement.innerText = utils.capitalize(blogTitle);
        aElement.appendChild(blogTitleElement);
        aElement.classList = "blogArticleLink"; // To drive the click to showBlog( clicked_link )
        aElement.href = x["download_url"];
        aElement.tag = x["html_url"];
        aElement.setAttribute("blog_file", x["name"]);

        liElement.appendChild(aElement);
        blogContainer.appendChild(liElement);
      }
    });
  }
}