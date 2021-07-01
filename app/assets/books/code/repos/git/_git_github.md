## GITHUB

## GITHUB ISSUES
popular bug trackers
provide the owners of a repository the ability to organize, tag, and associate issues to milestones.
If you open an issue on a project managed by someone else, it will stay open until either you close it


## SOCIAL CODING

		Participate in the rich open-source community
		Cloning a repo to try it out should be second-nature to you, and you should understand how to use branches on collaborative projects.

		GitHub
			https://github.com
			https://help.github.com
			https://github-windows.s3.amazonaws.com/GitHubSetup.exe 		Gitub for Windows, a credential helper to tell git that you don´t want to type your user/pwd every time you talk to a remote server.
            
            GitHub - Git is a type of source code repository - a place where code can be stored and collaboratively worked on.
			GitHub is an online service that allows you to create and share Git repositories.

			est le meilleur emplacement pour partager du code avec des amis, des collègues, des camarades de classe et de parfaits inconnus.
			Plus de trois millions de personnes utilisent GitHub pour créer des choses incroyables ensemble.

			a web-based hosting service for software development projects that use the Git version control system.
			Erlang is used for RPC proxies to ruby processes

## SOCIAL CODING
FOLLOW
    you can follow a developer or a repository
    the activity will show up in your dashboard
    you see what people do.
STARS
    star a repository. This action will include it in your “starred repositories” list, which allows you to keep track of projects you find interesting and discover similar projects.
[Trending page](https://github.com/trending)
        features the repositories that get the most stars in a determined period of time 
FORK
    indicator of a project is the number of forks.
    a fork is the base of a Pull Request (PR), which is a change proposal. A person may fork your repository, make some changes, and then create a pull request to ask you to merge those changes.
    a person may fork your repository, makes some changes, and then create a pull request to ask you to merge those changes.

## PROJECT MANAGEMENT
    https://github.com/marketplace
    Organize, manage, and track your project with tools that build on top of issues and pull requests
MONITORING
    Monitor the impact of your code changes. Measure performance, track errors, and analyze your application.
CONTINUOUS INTEGRATION
    Automatically build and test your code as you push it to GitHub, preventing bugs from being deployed to production.
CODE QUALITY
    Automate your code review with style, quality, security, and test-coverage checks when you need them.

## WEBHOOKS AND SERVICES
GitHub offers many features that help the developer workflow

WEBHOOKS
    Webhooks allow external services to be pinged when certain events happen in the repository, for example when code is pushed, a fork is made, or a tag was created or deleted.
    When an event happens, GitHub sends a POST request to the URL we tell it to use.
SERVICES
    GitHub services, and the new GitHub apps, are 3rd party integrations that improve the developer experience or provide a service to you.
    For example, you can setup a test runner to run the tests automatically every time you push some new commits, using TravisCI. https://travis-ci.org/
    You can setup Continuous Integration using CircleCI. https://circleci.com/
    You might create a Codeclimate integration that analyzes the code and provides a report of “Technical Debt” and test coverage. https://codeclimate.com/

download.page(code/repos/git/_git_githubpages.md)
download.page(code/repos/git/_git_github_packages.md)




# GITHUB

applications	https://github.com/settings/installations

Issue with files starting by '_': 
https://github.community/t/unable-to-access-resources-in-folder-with-name-starting-with/10505

		INSTALLED GITHUB APPS
			GitGuardian	
			Netlify	Netlify
		
		AUTHORIZED GITHUB APPS
			Gatsby Cloud
			GitGuardian							
			GitHub Codespaces						
			Netlify						
			Vercel		

### AUTHORIZED OAUTH APPS   applications granted to access your account.

			* 8base
			* CircleCI
			* FaunaDB Cloud
			* GitHub CLI
			* GitHub Desktop
			* Glitch
			* Microsoft Events
			* Microsoft-Corporation
			* Netlify Auth
			* p5.js Web Editor
			* Serverless
			* Skillvalue (prod)
			* SwaggerHub SaaS
			* Travis CI


https://codeburst.io/what-makes-a-good-github-profile-ced754284e3d

# When created a new repo:

ps>ls -Attributes hidden    	to view '.git'
ps>ls -Att hidden		    	to view '.git'

…or push an existing repository from the command line
	git remote add origin https://github.com/guinetn/guinetn.git
	git branch -M main		
	git push -u origin main
	
…or create a new repository on the command line
	echo "# guinetn.github.io" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git branch -M main
			\___ git branch -m master main    Renaming: master → main

			error: refname refs/heads/master not found
			fatal: Branch rename failed
			 \___ Fix: git add readme.md + git commit -m "first commit"
	git remote add origin https://github.com/guinetn/guinetn.github.io.git
		fatal: remote origin already exists.
		  \___ Fix: git remote remove origin  
	git push -u origin main
			  \__ Set upstream 
			 	 First occurrence of git push included 
			 	 	* the “set upstream” option -u
			 	 	* the destination origin
			 	 	* master
			 	 Once set up, omit all those details and just 'git push'
			 	 Download any changes automatically when we run 'git pull'



guinetn/guinetn
	special repository because its `README.md` (this file) appears on your GitHub profile.
	
	- 🔭 I’m currently working on ...
	- 🌱 I’m currently learning ...
	- 👯 I’m looking to collaborate on ...
	- 🤔 I’m looking for help with ...
	- 💬 Ask me about ...
	- 📫 How to reach me: ...
	- 😄 Pronouns: ...
	- ⚡ Fun fact: ...


# API
	
	https://api.github.com/

	const res = await fetch('https://api.github.com/')
    const urls = await res.json()

	{
	  "current_user_url": "https://api.github.com/user",
	  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
	  "authorizations_url": "https://api.github.com/authorizations",
	  "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",
	  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",
	  "emails_url": "https://api.github.com/user/emails",
	  "emojis_url": "https://api.github.com/emojis",
	  "events_url": "https://api.github.com/events",
	  "feeds_url": "https://api.github.com/feeds",
	  "followers_url": "https://api.github.com/user/followers",
	  "following_url": "https://api.github.com/user/following{/target}",
	  "gists_url": "https://api.github.com/gists{/gist_id}",
	  "hub_url": "https://api.github.com/hub",
	  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
	  "issues_url": "https://api.github.com/issues",
	  "keys_url": "https://api.github.com/user/keys",
	  "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",
	  "notifications_url": "https://api.github.com/notifications",
	  "organization_url": "https://api.github.com/orgs/{org}",
	  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",
	  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",
	  "public_gists_url": "https://api.github.com/gists/public",
	  "rate_limit_url": "https://api.github.com/rate_limit",
	  "repository_url": "https://api.github.com/repos/{owner}/{repo}",
	  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",
	  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",
	  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",
	  "starred_gists_url": "https://api.github.com/gists/starred",
	  "user_url": "https://api.github.com/users/{user}",
	  "user_organizations_url": "https://api.github.com/user/orgs",
	  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
	  "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"
	}

	GET REPO FILES LIST

		braincache
			\__ css
			\__ js                                            add 'contents'
																↓
			https://api.github.com/repos/guinetn/braincache/contents
			https://api.github.com/repos/guinetn/braincache/contents/css   
																	  ↑____ 'contents'	/ folder																  
			FILE
				{
			    "name": "index.css",
			    "path": "css/index.css",
			    "sha": "1d79f4b59549899107f8008fb187aa46dae446b0",
			    "size": 7874,
			    "url": "https://api.github.com/repos/guinetn/braincache/contents/css/index.css?ref=main",
			    "html_url": "https://github.com/guinetn/braincache/blob/main/css/index.css",
			    "git_url": "https://api.github.com/repos/guinetn/braincache/git/blobs/1d79f4b59549899107f8008fb187aa46dae446b0",
			    "download_url": "https://raw.githubusercontent.com/guinetn/braincache/main/css/index.css",   ← TO DOWNLOAD
			    "type": "file",
			    "_links": {
			      "self": "https://api.github.com/repos/guinetn/braincache/contents/css/index.css?ref=main",
			      "git": "https://api.github.com/repos/guinetn/braincache/git/blobs/1d79f4b59549899107f8008fb187aa46dae446b0",
			      "html": "https://github.com/guinetn/braincache/blob/main/css/index.css"
			    }
			  },

			DIR																  
			{
				"name": "from_others",
			    "path": "css/from_others",
			    ...
			    "download_url": null,
			    "type": "dir",                 ← A DIR !!
			    "_links": {
			      "self": "https://api.github.com/repos/guinetn/braincache/contents/css/from_others?ref=main",
			      "git": "https://api.github.com/repos/guinetn/braincache/git/trees/6297872ac5ebfbf7db132c20a928c66b131fc8e5",
			      "html": "https://github.com/guinetn/braincache/tree/main/css/from_others"    ← 
			    }
			  },

		https://markheath.net/post/list-and-download-github-repo-cs
		
		var httpClient = new HttpClient();
		httpClient.DefaultRequestHeaders.UserAgent.Add(
		    new ProductInfoHeaderValue("MyApplication", "1"));
		var repo = "markheath/azure-deploy-manage-containers";
		var contentsUrl = $"https://api.github.com/repos/{repo}/contents";
		var contentsJson = await httpClient.GetStringAsync(contentsUrl);
		var contents = (JArray)JsonConvert.DeserializeObject(contentsJson);
		foreach(var file in contents)
		{
		    var fileType = (string)file["type"];
		    if (fileType == "dir")
		    {
		        var directoryContentsUrl = (string)file["url"];
		        // use this URL to list the contents of the folder
		        Console.WriteLine($"DIR: {directoryContentsUrl}");
		    }
		    else if (fileType == "file")
		    {
		        var downloadUrl = (string)file["download_url"];
		        // use this URL to download the contents of the file
		        Console.WriteLine($"DOWNLOAD: {downloadUrl}");
		    }
		}	  


# PRODUCTS

* [GITHUB.COM](https://docs.github.com/en/github)
 manage accounts and access, licenses, and billing

* [GitHub CLI](https://cli.github.com/)
	
	GitHub to your terminal
	https://cli.github.com/manual/

	 gh auth login --hostname github.com   .... pwd
	 ./dothings > output.txt
	 gh gist create output.txt -d "Debugging info"

* [GITHUB DESKTOP](https://docs.github.com/en/desktop)

* [GITHUB ACTIONS](https://docs.github.com/en/actions)

	https://blog.jakoblind.no/aws-lambda-github-actions/

* [GITHUB PACKAGES](https://docs.github.com/en/packages)
	
	hosting and managing packages, containers and other dependencies

	publish and consume packages
	store your packages alongside your code
	share your packages 
		privately with your team
		publicly with the open source community
	automate your packages with GitHub Actions

	GitHub Container Registry 
		host and manage Docker container images in your organization or personal user account on GitHub. 
		GitHub Container Registry allows you to configure who can manage and access packages using fine-grained permissions.

	https://docs.github.com/en/packages/publishing-and-managing-packages/publishing-a-package#publishing-a-package

	Publishing a package using an action
		Configure a workflow so that anytime a developer pushes code to the default branch, 
		the workflow runs CI tests. If those tests pass, the workflow publishes a new package 
		version to GitHub Packages. This workflow automates the creation of new package versions 
		only if the code meets your quality standards.

* [ENTERPRISE SERVER](https://docs.github.com/en/enterprise/admin)

* [DEVELOPERS](https://docs.github.com/en/developers)

	your GitHub workflow:

	Generate a new personal access token with GitHub developer settings or use the "Create a new authorization" endpoint in the OAuth Authorizations API to generate a new OAuth token. 
	https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

	Webhooks and events→
		You can set up, test, and secure webhooks so your integrations can subscribe and react to events on GitHub.

	Apps→
		You can automate and streamline your workflow by building your own apps.

	GitHub Marketplace→
		List your tools in GitHub Marketplace for developers to use or purchase.

* [REST API](https://docs.github.com/en/rest)

	curl -i https://api.github.com/users/guinetn
	[Personal access tokens](https://github.com/settings/tokens)

	Keys, SSH
	extend and customize your GitHub experience
	
	https://docs.github.com/en/developers/apps/building-oauth-apps
	

	* REST API
		to get the data you need to integrate with GitHub

		https://api.github.com + Accept: application/vnd.github.v3+json
		https + json

		curl -i https://api.github.com/users/octocat/orgs

		Basic authentication 				$ curl -u "username" https://api.github.com
		OAuth2 token (sent in a header)		$ curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com

		https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps#projects
			GET /projects/{project_id}
			PATCH /projects/{project_id}
			DELETE /projects/{project_id}
			GET /projects/{project_id}/collaborators

	* GraphQL API

		https://api.github.com/graphql

		$ curl -H "Authorization: bearer token" -X POST -d " \
		 { \
		   \"query\": \"query { viewer { login }}\" \
		 } \
		" https://api.github.com/graphql

* [GRAPHQL API](https://docs.github.com/en/graphql)

* [GITHUB INSIGHTS](https://docs.github.com/en/insights)

* [ATOM ](https://atom.io/docs)

* [ELECTRON ](https://electronjs.org/docs)

* GitHub Marketplace
	
	connects you to developers who want to extend and improve their GitHub workflows. 
	List your tools in GitHub Marketplace for developers to use or purchase.
	tools: GitHub Actions 
	       Apps




# DELETE REPOS 'BULK WAY POWERSHELL'

	https://stackoverflow.com/questions/19319516/how-to-delete-a-github-repo-using-the-api

	If you have github.com/foo/bar, then :owner is foo and :repo is bar
	curl -X DELETE -H 'Authorization: token {access token goes here}' https://api.github.com/repos/{yourUsername}/{name of repo}

	First run the following command in powershell (otherwise you might get an "can't create ssl/tls channel"exception)
	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
						guinetn/quickstart
						guinetn/socketnodeci
							↓
	get-content C:\Temp\repolist.txt | ForEach-Object { Invoke-WebRequest -Uri https://api.github.com/repos/$_ -Method “DELETE” -Headers @{"Authorization"="token abcdef....abcdef"} }
			↓
			CREATE ThE TOKEN FROM https://github.com/settings/tokens
								  GENERATE NEW TOKEN
								  X delete_repo  Delete repositories


	Delete all
	http https://api.github.com/user/repos "Authorization:token $TOKEN" per_page==100 type==owner | jq '.[].full_name' | xargs -I '{}' http DELETE https://api.github.com/repos/'{}' "Authorization:token $TOKEN" 

# GitHub for Windows: CLONE OR DOWNLOAD: open in desktop
	
	clone by github-windows
	
	<a href="github-windows://openRepo/https://github.com/guinetn/njs01" class="btn btn-outline get-repo-btn tooltipped tooltipped-s tooltipped-multiline" aria-label="Clone guinetn/njs01 to your computer and use it in GitHub Desktop.">
	    Open in Desktop
	  </a>


# WIKI
https://www.youtube.com/watch?v=4B0XNThjO0E
[](https://github.com/guinetn/guinetn.github.io/wiki/)

# GIST
short code reminder shared store 
https://gist.github.com

# Git is a version control system that tracks changes to files in a project over time. 

ue-grid-layout
	vue-grid-layout is 
# Features
# Installation
	install the vue-grid-layout package package using npm:
	npm install vue-grid-layout
	or
# Usage
	Bundler (Webpack, Rollup)
		import Vue from 'vue'
	Browser
		<script src="vue-grid-layout.min.js"></script>
# Contribute
	If you have a feature request, please add it as an issue or make a pull request.

	# Contributing to Apress Source Code

	Copyright for xxx source code belongs to the author(s). However, under fair use you are encouraged to fork and contribute minor corrections and updates for the benefit of the author(s) and other readers.

	## How to Contribute

	1. Make sure you have a GitHub account.
	2. Fork the repository for the relevant book.
	3. Create a new branch on which to make your change, e.g. 
	`git checkout -b my_code_contribution`
	4. Commit your change. Include a commit message describing the correction. Please note that if your commit message is not clear, the correction will not be accepted.
	5. Submit a pull request.

	Thank you for your contribution!

# TODO List
# License


# GITHUB
# GitHub is a web hosting service for the source code of software and web development projects (or other text based projects) that use Git.
# In many cases, most of the code is publicly available, enabling developers to easily investigate, collaborate, download, use, improve, and remix that code. The container for the code of a specific project is called a repository.
# Emoji
	GitHub supports emoji! :sparkles: :camel: :boom:
	To see a list of every image we support, check out the Emoji Cheat Sheet.

# There are thousands of really cool and exciting repositories on GitHu
### POPULAR ON GITHUB
# Twitter Bootstrap, an extremely popular front-end framework for mobile first websites, created by developers at Twitter.
# HTML5 Boilerplate, a front-end template for quickly building websites,
# The JavaScript Visualization Library D3
# Ruby on Rails, the open-source web framework built on Ruby.




## [GITHUB PAGES](https://pages.github.com/)

issue with files starting with '_':
	GitHub Pages uses Jekyll by default to build Pages sites. Because of the way that Jekyll works, any files or folders that start with _, ., # or end with ~ are not built:
	https://help.github.com/articles/files-that-start-with-an-underscore-are-missing/ 36
	If you’re not using Jekyll, you can add an empty file named .nojekyll to the root of your publishing source to avoid this.
	If you are using Jekyll, you can use the include directive in your _config.yml file to explicitly include these files/folders:
	https://jekyllrb.com/docs/configuration/options/ 30




https://github.com/guinetn/wed
				↓
# GHP https://guinetn.github.io/wed/

# GitHub pages is a service offered by GitHub that allows hosting for websites configured straight from the repository. 

# You get one site per GitHub account and organization, and unlimited project sites

# Hosting solution for websites with HTML, CSS, JS
# Repository is named a certain way (guinetn.github.io) or use cusom domain
# HTML/Markdown files inside can be viewed like any other website
# Pages have Jekyll as static site generator 

https://www.gatsbyjs.org/docs/how-gatsby-works-with-github-pages/
https://help.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain


[Creating and Hosting a Personal Site on GitHub](http://jmcglone.com/guides/github-pages/)
https://www.thinkful.com/learn/a-guide-to-using-github-pages/
https://guinetn.github.io/

# GitHub Pages are public webpages hosted for free through GitHub. GitHub users can create and host both personal websites (one allowed per user) and websites related to specific GitHub projects. Pages lets you do the same things as GitHub, but if the repository is named a certain way and files inside it are HTML or Markdown, you can view the file like any other website. GitHub Pages is the self-aware version of GitHub. Pages also comes with a powerful static site generator called Jekyll, which we'll learn more about later on.

easy hosting solution for websites with HTML, CSS, and JavaScript files

# Custom domain
# Custom domains allow you to serve your site from a domain other than guinetn.github.io. Learn more.

http://www.backalleycoder.com/2016/05/13/sghpa-the-single-page-app-hack-for-github-pages/

# Infinite Scroll With Jekyll <http://tobiasahlin.com/blog/>
# If you want to use Jekyll but don’t want to settle with a list of links to your blog posts, I just open sourced the parts that drives this blog’s infinite scroll. As I mentioned in Moving from WordPress to Jekyll, the implementation is built around collecting the links to all blog posts in a JSON file, and using that to load more posts as you scroll.

http://jekyllrb.com/
# Free hosting with GitHub Pages
# Sick of dealing with hosting companies? GitHub Pages are powered by Jekyll, so you can easily deploy your site using GitHub for free—custom domain name and all.

# What is Git, GitHub, and GitHub Pages?
# Git, GitHub, and GitHub Pages are all very closely related. Imagine Git as the workflow to get things done and GitHub and GitHub Pages as places to store the work you finish. Projects that use Git are stored publicly in GitHub and GitHub Pages, so in a very generalized way, Git is what you do locally on your own computer and GitHub is the place where all this gets stored publicly on a server.


# Deploying to GH Pages
	To make test on a real device... 
	To do so, we just need to deploy and access the URL from a real mobile device.

	GH pages is free, so we can just deploy there:		
		npm install gh-pages --save-dev    	// Install the GitHub Pages SDK:
 		"deploy": "gh-pages -d ." 			// package.json scripts
		git remote add origin <GITHHUB-URL> // Setup a GitHub repository and add it as origin:
		npm run deploy

		


## Webhooks 
	
	a way for notifications to be delivered to an external web server whenever certain actions occur on a repository or organization. ... A repository is pushed to. A pull request is opened. A GitHub Pages site is built.

	are basically user defined HTTP callbacks (or small code snippets linked to a web application) which are triggered by specific events. Whenever that trigger event occurs in the source site, the webhook sees the event, collects the data, and sends it to the URL specified by you in the form of an HTTP request.

	used to connect two different applications. When an event happens on the trigger application, it serializes data about that event and sends it to a webhook URL from the action application—the one you want to do something based on the data from the first application

	to build or set up integrations, such as GitHub Apps or OAuth Apps, which subscribe to certain events on GitHub.com
	Webhooks can be installed on an organization or a specific repository. 
	Once installed, the webhook will be triggered each time one or more subscribed events occurs.

## Github Actions: automate your workflow

	https://medium.com/@adam.zolyak/my-first-week-with-github-actions-5d92de4c4851

	In Visual Studio
		https://devblogs.microsoft.com/visualstudio/using-github-actions-in-visual-studio-is-as-easy-as-right-click-and-publish/
		Visual Studio will create the GitHub Action workflow file, including the deployment action to Azure App Service. 
		The default trigger is “on push” for your code in the default branch for your repository. 
		Visual Studio will also automatically download the publish profile from the Azure portal and store it as an encrypted 
		secret in your GitHub repo as required by the workflow. As soon as you commit and push the generated GitHub Action 
		workflow file, deployment to Azure begins. 
		
		Right now, this feature is only available for ASP.NET Core projects deployed to Azure App Service 
		and Azure Functions projects

	Samples
 		https://github.com/waffleio/waffleio-gh-actions/tree/master/action-newissuecomment
		https://github.com/anothrNick/github-tag-action
 		https://itnext.io/creating-a-github-action-to-tag-commits-2722f1560dec *****
 		https://www.youtube.com/watch?reload=9&v=J4EhgEskSZA    GitHub Actions Tutorial: yarn init -y + dotenv
 		https://blog.jakoblind.no/aws-lambda-github-actions/    Netlify + aws lambda

	way to automate and customize your team's workflow in GitHub

	Github Actions is a CI/CD that you can use for building, testing and deploying your code. 
	The nice thing with this is that it’s built into GitHub. 
	You don’t need to signup for another service for this. 
	It’s actually already there, but you might not have noticed. 
	Go to the page of you repo in GitHub and you’ll see an “Actions” tab.

	create custom software development life cycle (SDLC) workflows in your GitHub repository
	Actions are 100% contained to GitHub and your GitHub repo. 
	No additional tools or services or money 😁! 
	You can store your Actions code in your GitHub repo, and GitHub runs your Actions code for you.

	Both Workflows and Actions are
		written as code 
		stored as part of your GitHub repo 
		100% reproducible from code

	
	Action
		individual task 
			create your own actions
			customize actions shared by the GitHub community
		can be combined to create jobs (and customize your workflow)
		You can discover, create, and share actions to perform any job 
		Actions don’t require any hosting.
		Actions can be written in the framework and language of your choice.

		An Action is a Docker container that runs as part of a Workflow. 
		If you haven’t used a Docker container before — it basically means that you can run anything you want in any programming language you want 👏👏👏. You can store your Actions within your GitHub repo or use other people’s Actions stored in public GitHub repos or use prebuilt Docker images from Docker registries.

		Actions let you write scripts that are triggered based on certain events in your GitHub repo (basically any GitHub webhook event) — creating a new issue, pushing a commit, merging a pull request.
	
	Create Your Own GitHub Action

          starting by checking out our New Issue Comment action
          It's a good example of a basic GitHub Action that updates an GitHub issue via the GitHub API
          https://github.com/waffleio/waffleio-gh-actions/tree/master/action-newissuecomment
          	→ post a welcome comment when a new issue is created

          		This GitHub Action runs when an issues event webhook is fired in your GitHub repo. 
          		The action checks if the event is of type action = opened and posts a comment to the issue thanking the user for their contribution.

          		1. Create a .github/main.workflow in your GitHub repo.

				2. Add the following code to the main.workflow file and commit it to the repo's master branch.
				workflow "Comment on New Issues" {
				  resolves = ["AddComment"]
				  on = "issues"
				}

				action "AddComment" {
				  uses = "waffleio/gh-actions/action-newissuecomment@master"
				  secrets = ["GITHUB_TOKEN"]
				}

				3. Create a new issue!

				4. Click on the Actions tab in your repo. You should see a new action that was recently 
				   triggered when you created the new issue. 
				   After a few seconds, there should be a comment on your issue.

				Code
					entryPoint.sh					
						#!/bin/bash
						echo "starting bash..."
						echo "current working directory is " $PWD
						cd ../../
						cd /action
						npm install
						node app.js

					app.js
						console.log("started nodejs...")

						const helpers = require('./helpers')

						//require octokit rest.js 
						//more info at https://github.com/octokit/rest.js
						const octokit = require('@octokit/rest')()

						//set octokit auth to action's GITHUB_TOKEN env variable
						octokit.authenticate({type: 'app', token: process.env.GITHUB_TOKEN })

						//set eventOwner and eventRepo based on action's env variables
						const eventOwnerAndRepo = process.env.GITHUB_REPOSITORY	
						const slicePos1 = eventOwnerAndRepo.indexOf("/");
						const eventOwner = eventOwnerAndRepo.slice(0, slicePos1);
						const eventRepo = eventOwnerAndRepo.slice(slicePos1 + 1, eventOwnerAndRepo.length);
						 
						async function commentOnNewIssue() {

						    //read contents of action's event.json
						    const eventData = await helpers.readFilePromise('..' + process.env.GITHUB_EVENT_PATH)
						    console.log(eventData)
						    const eventJSON = JSON.parse(eventData) 

						    //set eventAction and eventIssueNumber
						    eventAction = eventJSON.action
						    eventIssueNumber = eventJSON.issue.number

						    console.log('event action: ' + eventAction)

						    //if a new issue was opened 
						    if (eventAction === 'opened') {
						        console.log("creating welcome comment on issue")

						        //add a comment to the new issue
						        await octokit.issues.createComment({
						          owner: eventOwner,
						          repo: eventRepo,
						          number: eventIssueNumber,
						          body: "🎉 Thanks for opening a new issue!  This community is successful because of it's contributors!  To help make sure your issue gets the attention it deserves, check out our [Contributing Guidelines](../blob/master/CONTRIBUTING.md)."
						        }).then(({ data, headers, status }) => {
						          // handle data
						          console.log('break 1')
						        })
						    }

						}

						//run the function
						commentOnNewIssue()

						module.exports.commentOnNewIssue = commentOnNewIssue

					helper.js
						const fs = require('fs')
						module.exports.readFilePromise = function(filename) {
						    return new Promise((resolve, reject) => {
						        fs.readFile(filename, 'utf8', (err, data) => {
						        if (err) reject(err);
						        else resolve(data);
						        })
						    }).catch(err => {
						        console.log(err)
						    })
						}


	GitHub hosted virtual machines
		Allow to run workflows
		Contains an environment of tools, packages, settings (environment variables)
		https://help.github.com/en/articles/virtual-environments-for-github-actions#github_token-secret

## Workflow

		Triggered based on GitHub Webhook events that fire when certain things happen 
		in your repo — creating a new issue, commenting on a pull request, merging a branch. 
		A Workflow runs one or more Actions.

		a configurable automated process made up of one or more jobs
		You must create a YAML file to define your workflow configuration.
		http://www.btellez.com/posts/triggering-github-actions-with-webhooks.html

			https://github.com/khanhicetea/.com/tree/master/.github/workflows

			https://github-actions.netlify.com/gatsby-cli
			workflow "Build Gatsby Site" {
			  on = "push"
			  resolves = ["build"]
			}
			action "build" {
			    uses = "jzweifel/gatsby-cli-github-action"
			    args = "build"
			}

			workflow "Build Gatsby Site in Subdirectory" {
			  on = "push"
			  resolves = ["build"]
			}
			action "build" {
			    uses = "jzweifel/gatsby-cli-github-action"
			    env = {
			      GATSBY_PROJECT_PATH = "./client"
			    }
			    args = "build"
			}
			Environment variables
			GATSBY_PROJECT_PATH- Optional. Directory from which to execute the Gatsby CLI.
			An open source list of GitHub Actio

	Events 
		Trigger workflows
		Workflows can run when 
			* specific activity on GitHub happens
			* at a scheduled time
			* when an event outside of GitHub occurs

# Actions → New workflow → node.js
	npm ci
	npm run build --if-present
	npm test

	Gatsby_try/.github/workflows/nodejs.yml
		name: Node CI

		on: [push]

		jobs:
		  build:

		    runs-on: ubuntu-latest

		    strategy:
		      matrix:
		        node-version: [8.x, 10.x, 12.x]

		    steps:
		    - uses: actions/checkout@v1
		    - name: Use Node.js ${{ matrix.node-version }}
		      uses: actions/setup-node@v1
		      with:
		        node-version: ${{ matrix.node-version }}
		    - name: npm install, build, and test
		      run: |
		        npm ci
		        npm run build --if-present
		        npm test
		      env:
		        CI: true


# Github take care of a number of processes which can be triggered by a variety of events on the platform, be it pushing code, making a release or creating issues among others.		

handling continuous integration and deployment (building, testing and deploying applications)
publishing npm modules
triggering alerts via mail or SMS
...

# GitHub Packages (formerly GitHub Package Registry)

https://github.com/features/packages

# Package: self-contained piece of software (code+metadata {version, name, dependencies)
         simplify using and distributing solutions (such as needing a common framework for developing a project, testing runners and linters to improve code quality, or introducing industry-standard machine learning tools to power your application)
		 Integrated  with * GitHub APIs
		 				  * GitHub Actions
		 				  * Webhooks 
		 			 to create an end-to-end DevOps workflow that includes your code, CI, and deployment solutions.
		
		An access token allow 
			* to publish, install, delete packages 
			* use a personal access token to authenticate with your username directly to GitHub Packages or the GitHub API. 
			* use a GITHUB_TOKEN to authenticate using a GitHub Actions workflow.

### Clients and formats:

		PACKAGE CLIENT	LANGUAGE	PACKAGE FORMAT	DESCRIPTION
		-------------------------------------------------------
		npm				JavaScript	package.json	Node package manager
		gem				Ruby		Gemfile			RubyGems package manager
		mvn				Java		pom.xml			Apache Maven project management and comprehension tool
		gradle			Java		build.gradle 	Gradle build automation tool for Java
		docker			N/A			Dockerfile		Docker container management platform
		dotnet CLI		.NET		nupkg			NuGet package management for .NET


# You can publish packages in 
	public packages		to share with all of GitHub
	private packages	to share with collaborators or an organization.
						You can host multiple packages in one repository

# GitHub roles+teams 	to limit who can install or publish each package
					packages inherit the permissions of the repository. 
						anyone with read permissions for a repository can install a package as a dependency in a project
						anyone with write permissions can publish a new package version.



# Publish and consume packages within your organization or with the entire world.
# Software package hosting service that allows you to host your software packages privately or publicly and use packages as dependencies in your projects.

# To combine your source code and packages in one place (+integrated permissions management +billing)
# Packages hosted on GitHub include details and download statistics, along with their entire history

npm login --registry=https://npm.pkg.github.com --scope=@phanatic
npm publish


# README PERFECT

https://medium.com/swlh/how-to-make-the-perfect-readme-md-on-github-92ed5771c061

* Add a license
* Add a readme 
	gives brief idea about what the project is about, which language it has used, what are the terms and conditions, licensing, how many forks/stars the repository has got, what your project can do, screenshots of your running application, etc
	.md extension (Markdown, a lightweight markup language with plain text formatting syntax). It’s a very simple language used to create beautiful and presentable readme files for GitHub.

	images side by side?

	## Screenshots 
		<img . PNG" 
		alt="Home Screen" 
		style="float: left; 
		<img 
		alt="Home Screen" 
		style="float: left; 
		<img 
		alt="Home Screen" 
		style="float: left; 
		width-"186"/> <img 
		alt="Home Screen" 
		style="float: left; 
		width- " 189" / > 
		margin-right: ICpx; " 
		src=" images/Capture2. PNG" 
		margin-right: ICpx; " 
		src="https : //media.gi2_by.com/media/g4M22W129fexgy34g7/2@ew d . gif" 
		margin-right: ICpx; " 
		src="https : //media.gi2_by.com/media/pzdFU08zPdlJhVMpWeX/2@ew d . gif" 
		margin-right: ICpx; " 

## Licensing

	 3 major licenses used are :
		Apache License v2.0 
		   	open source product and you want people to distribute as well as contribute to your code
		   	https://www.apache.org/licenses/LICENSE-2.0

		   	Apache License v2.0 in your readme as well as your repository, Type the following in your readme file.
		   	
				Copyright [yyyy] [name of copyright owner]

				Licensed under the Apache License, Version 2.0 (the "License");
				you may not use this file except in compliance with the License.
				You may obtain a copy of the License at

				    http://www.apache.org/licenses/LICENSE-2.0

				Unless required by applicable law or agreed to in writing, software
				distributed under the License is distributed on an "AS IS" BASIS,
				WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
				See the License for the specific language governing permissions and
				limitations under the License.
		GNU General Public License v3.0
		MIT License

	badges
		https://shields.io/



