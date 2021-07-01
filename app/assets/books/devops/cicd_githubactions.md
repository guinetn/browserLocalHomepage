## GitHub Actions

Released  in November 2019

An API that can react to any event (on push event on the repository run test cases)

For continuous integration of your app
For continuous deployment (ex, pushing a Docker image to a Docker registry Docker Hub)

Tool to perform CI/CD
Run automatically tasks/actions on certain events (SDLC workflows in your GitHub Repo directly)


Like many other CI/CD systems, GitHub Actions lets you define a workflow to automatically build, test, and deploy your apps. And it integrates with GitHub so you can automate the process in a single platform, without any external tools. Your code is on GitHub, your CI/CD runs on GitHub, and—if you want—you can have your distribution on GitHub


Salient Features of GitHub Actions
You can create, share, reuse, and fork your software development practices.
It is fully integrated with GitHub, making it manageable from a single place.
You can perform multi-container testing by adding support for Docker.
You can choose from multiple CI templates or even create your own.
Include 2000 free build minutes/month for all your private repositories.

my_github_repo  
  └── .github
        └──workflows            
            └── my_file.yml    .yml file specifying CI/CD steps

Template:        
YAML files are uncomfortable (large = indentation problems might become unnoticed, and support from IDEs is rare).
```yaml
# Workflow name
name: Build
on:
# When it will be triggered
# And in which branch
  pull_request:
  push:
    branches:
      - main
# Where will they run
jobs:
  build:

    runs-on: ubuntu-latest    
```


```yaml
on: push
name: npm build, lint, test and publish
jobs:
  build-and-publish:
    name: build and publish
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: npm install
        uses: actions/npm@master
        with:
          args: install
      - name: npm test
        uses: actions/npm@master
        with:
          args: run test
      - name: npm lint
        uses: actions/npm@master
        with:
          args: run lint
      - name: docker build
        uses: actions/docker/cli@master
        with:
          args: build -t abhinavdhasmana/github-action-example-node .
      - name: docker login
        uses: actions/docker/login@master
        env:
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
          DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
      - name: docker push
        uses: actions/docker/cli@master
        with:
          args: push abhinavdhasmana/github-action-example-node
```

On every push, perform these actions in the given order
- git clone the repo
- run npm install
- run npm lint
- run npm test
- build the docker image
- login to docker hub
- Push the image to docker hub


## Actions

https://github.com/features/actions

***Type of step*** that help us with the task of automating our CI/CD. 

There is a good number of options already available as GitHub actions, including notifications on Telegram, via E-Mail or Discord. 
https://github.com/appleboy/telegram-action
https://github.com/marketplace/actions/send-email
https://github.com/Ilshidur/action-discord

Anybody can publish their Action as open-source, and they are browsable via GitHub: https://github.com/actions
APIs to create your own actions as you need them, or accessing them from the GitHub marketplace: https://github.com/marketplace?type=actions
[Create your own](https://docs.github.com/en/free-pro-team@latest/actions/creating-actions)

ex: https://github.com/actions/checkout : Action for checking out a repo
```yaml
- uses: actions/checkout@v2
  with:
    fetch-depth: 0
```
    
    
Many of the functionality we might want to implement is likely already here, so it is worth taking a look to avoid reinventing the wheel. And of course, it is possible to fork and modify existing actions or create our own ones.
Now, here is a list of some suggestions of operations we can perform in Android. As the name CI/CD, we typically want to start building and deploying apps, but there are some goodies that we can apply (notify certain channels or platforms, etc). Let’s get started.


## More
- https://blog.bitsrc.io/
- https-medium-com-adhasmana-how-to-do-ci-and-cd-of-node-js-application-using-github-actions-860007bebae6
- https://medium.com/google-developer-experts/github-actions-for-android-developers-6b54c8a32f55
- https://andrewlock.net/auto-assigning-issues-using-a-github-action