## GITHUB PAGES

allows you to host simple HTML sites for free on GitHub’s infrastructure.

https://github.com/blog/2289-publishing-with-github-pages-now-as-easy-as-1-2-3
Publishing a website or software documentation with GitHub Pages now requires far fewer steps — three to be exact:
-Create a repository (or navigate to an existing repository)
-Commit a Markdown file via the web interface, just like you would any other file
-Activate GitHub Pages via your repository's settings

## GitHub Pages uses the special gh-pages branch in place of master

$ mkdir -p repos/sample_website	
$ cd repos/sample_website
$ touch index.html	
$ git init
$ git add -A
$ git commit -m "Initialize repository"

now ready to push our repo up to GitHub.
Go to github.com, log in if necessary, and then create a new repository 
git remote add origin `repo url`  

$git checkout -b gh-pages
$ git push -u origin gh-pages

https://`username`.github.io/`repo_name`