# DevOps

* Dev: people who create software
* Ops: people who manage the software

DevOps is all about:
- culture
- automation
- monitoring metrics
- sharing

https://github.com/priximmo/sommaire-xavki-devops-fr

Continually provide a high-value software product to the customer
At high speed while monitoring and improving the overall process
                            
Teams + process + tools → quality product in a fast continuous iterations delivery
* Tools: Docker, Kubernetes, CI/CD, CaI:Terraform-Ansible, unix-based command line, powershell  
* Practices
that combine software development (Dev) and IT Operations (Ops) into a single unifying force

DevOps has to communicate with various departments inside the company and with the customers to deliver high-value products: Need for better collaboration between developers, operations teams, system administrators and system engineers.

Devops comes from agility to move fast in a stable infrastructure

## MVP

![mvp_howto.jpg](assets/books/devops/assets/mvp_howto.01.jpg)
![mvp_howto.jpg](assets/books/devops/assets/mvp_howto.02.png)
![mvp_howto.jpg](assets/books/devops/assets/mvp_03.jpg)
## DevOps Phases 
* Planning          Better growth 
* Code				Development and review, continuous integration tools
* Test				Selenium to automate application testing
* Build				Control tools, code merging, build status, error testing
* Configure			Write IaC (Infrastructure as Code) to automate
Achieved by Configuration management tools (ansible, puppet, Ceph , SaltStack)
Package		    Repository, application pre-deployment staging
                    ci/cd pipeline triggered by configuration (webhook)
                    Automating the testing using selenium
* Release			Management, release approvals, release automation
* Deploy
* Operate
* Monitor			Performance monitoring (Metrics: cpu, ram…), end user experience. Alerts + Logs

Improve speed+quality of the entire production process

Cloud providers such as AWS, Google Cloud Platform (GCP), Azure... offer DevOps tools directly integrated into their services (source code managers, integration chains…)

![devops](assets/books/devops/assets/devops0.png)
![devops](assets/books/devops/assets/devops2.jpg)
![devops](assets/books/devops/assets/devops3.png)
![devops](assets/books/devops/assets/devops.png)

::::
## Software development methodology history

* 1990 - Waterfall
1. Make product requirement documentation
2. Build
3. Start Tests
Testing and bug fixing can take time...
Rigidity: What if the roadmap changes?
* 2001 - Agile Manifesto
Iterative approach: continuously build features that add value, then test and release
But agile fails joining developers and operations team
* 2008 - DevOpsDays to “evolving” Agile to create a Bridge between two siloed teams

::::
download.page(devops/agility.md)
 ::::
## DEVOPS TERMS

* Have a fully autonomous infrastructure
* Reduce repeatable processes
* Reduce manual tasks (man-hours worked)
* Reduce errors
* Throttle development efforts
* Reduce costs
* Increase CI/CD process speed
* Increase customer satisfaction

#### DevOps Engineer
Bridge between developers and operations team to successfully “supervise” code releases and improve CD/CD pipelines.

#### IT (Information Technology)
Is the use of any computers, storage, networking and other physical devices, infrastructure...

####  IT operations
Processes and services administered by an organization's information technology (IT) department:  administrative processes with support for hardware and software.
Roles:
- Monitor IT servers and systems
- Help desk
- Updates & installations
- Tech management
- Quality assurance
- Infrastructure management
- support both internal and external clients

#### CALMS Model/Framework
The CALMS model help organizations understand and define DevOps principles. It is a framework through which we can analyze if an organization is ready for DevOps processes. The CALMS model stands for Culture, Automation, Lean, Measurement, and Sharing.

::::
## DEVOPS TOOLS

Development Product
Deployment
Monitoring

* Provisioning tools include:
- Terraform - cloud agnostic
- AWS Cloudformation AWS only
- Pulumi - similar to Terraform but we can use Python, Go etc. instead of HCL DSL.

* Configuration management tools include:
- Chef - Ruby/Erlang, Knife, recipe, cookbook
- Puppet - Ruby, Puppet manifests, Factor, catalog
- Ansible - Python, Playbook, inventory
- CFEngine
- SaltStack - Python, YAML, Jinja2, salt master / salt minion
- Fabric - Python


### 🔱 PROJECT MANAGEMENT = PLANNING/COLLABORATION

Team ←→ company ←→ client communication, collaboration, planning.

download.page(devops/collaboration_jira.md)

download.page(devops/collaboration_slack.md)

download.page(devops/collaboration_asana.md)

download.page(devops/collaboration_trello.md)

Clarizen – An SaaS project management tool.
Basecamp – A tool used for project management and real-time communication between teams.

### 🔱 VERSIONING CONTROL

- GitHub
https://github.com
code hosting with git version control
share your code publicly or privately
allows multiple users to work on the same project and to review ongoing submitted changes
Free for up to 3 collaborations/private repositories

Subversion — a versioning control system inspired by CVS (Concurrent Versions System)

GitLab — Similar in name but different from Git; it is a complete DevOps platform that does everything from project planning and source code management to CI/CD and monitoring.

GitKraken — Helps developers work more efficiently with Git on Windows, Mac, and Linux.

Mercurial — A open-source software written in Python as a replacement for BitKeeper.

BitKeeper is one of the oldest distributed source management systems licensed under the Apache 2.0 License. It is not actively developed.

::::
### CI/CD

download.page(devops/cicd.md)

::::
### IAC - INFRASTRUCTURE AS CODE

AUTOMATION / CONFIGURATION MANAGEMENT

download.page(cloud/cloud_automation.md)

::::
### MONITORING

download.page(cloud/cloud_monitoring.md)

::::

### Continuous Feedback Tools

Help keep all team members engaged and involved in the conversation and permit end-user interaction.

Jira — One of the most popular feedback, issue tracking, and task management tools developed by Atlassian.

MouseFlow — A tool that gives insights on how end-users interact with a website in terms of clicks, scrolls, and overall browsing experience.

SurveyMonkey — An online survey tool.

### Issue Tracking Software

Keep track of bugs and how fast they are fixed. Top picks include:

Jira – The standard in this category and is widely deployed by DevOps teams across multiple organizations.

Mantis Bug Tracker – An agile, open-source security, and license compliance management tool that identifies real-time security and compliance issues with libraries.

WhiteSource Bolt – A tool developed by Atlassian for Azure DevOps that manages open-source security and compliance.

Snort – An open-source security tool for real-time traffic analysis.

OverOps – A tool for data optimization and code analysis.

Code Climate – A code review tool that automatically monitors code health from the command line to the cloud.

Zendesk – Customer support software for better communication between end-users and support teams.

## More

- https://dev.to/rahulku48837211/let-s-build-a-devops-project-4b65
- https://roadmap.sh
- https://www.bogotobogo.com/DevOps/DevOps_Jenkins_Chef_Puppet_Graphite_Logstash.php