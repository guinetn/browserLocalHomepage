# CI-CD

To frequently deliver apps to customers by introducing automation into the stages of app development. 

For software lifecycle,  CD/CI together mean that whatever changes are made to the code, should be integrated into the Production environment without turning the environment OFF.

CI/CD pipeline enable teams to release a constant flow of software updates into production to quicken release cycles, lower costs, and reduce the risks associated with development.

Continuous Integration (CI)
Continuous Delivery (CD)
Continuous Deployment (The other CD)

Delivery process tools
- automate build testing
- reduces the risk of manual errors
- provides standardized development feedback loops
- enables fast product iterations.

With a deployment pipeline, teams can release software in a fast, repeatable and reliable manner 

![](assets/books/devops/assets/ci_cd_process01.png)

![](assets/books/devops/assets/ci_cd_process02.png)


## Release 
Snapshot of the deployment process and the associated assets (packages, scripts, variables) as they existed when the release was created. The release is given a version number, and you can deploy that release as many times as you need to.  
SQL Server 2019 is a release of SQL Server.   

A deployment is what happens when someone deploys a release to an environment. Releases are deployed many times as they progress through each of your environments, for instance, from dev to test to staging and finally into production.

## Staging environment
- where changes are run against production-equivalent infrastructure and data to ensure that they will work properly when released.
- use the 'develop' branch
- deploy to the staging server

## Production environment
- use the 'master/main' branch
- deploy to the live server 
- master branch should always be ready for a deployment to live


A developer’s job typically ends at reviewing a pull request from a teammate and merging it to the master branch. Buddy then takes over from there by running all tests and deploying the code to production, while keeping the team notified through channels like Slack (we shall discuss setting up Slack notifications later).

download.page(devops/ci.md)

download.page(devops/cd.md)


### Automating in CI/CD pipelines

- https://developer.okta.com/blog/2020/12/09/dotnet-cloud-host-publish
- https://developer.okta.com/blog/2020/10/07/dotnet-container-azure-devops
- https://developer.okta.com/blog/2020/06/22/deploy-dotnet-container-aws-fargate
- https://cloud.google.com/solutions/deploy-dotnet-applications
- https://medium.com/marionete/building-a-serverless-ci-cd-pipeline-on-aws-12d1660ea384
- https://www.redhat.com/en/topics/devops/what-is-ci-cd