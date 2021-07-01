# IAC - INFRASTRUCTURE AS CODE 

IAC = coded architecture = IT automation
The goal is to guarantee the same environment is created every time the code is executed. Enable teams to focus on provisioning rather than individual configuration management

Managing/provisioning your IT infrastructure using configuration files instead of physical/manual hardware configuration  
IaC is also used in DevOps practices and SRE specializations. DevOps and SRE (Site Reliability Engineer) are also popular methodologies.

To have a well-defined infrastructure written with high-quality documentation

Why: server administration is complex, repeating tasks...
- Left to the developers and system administrators= a 'soluble' expertise
- Most if not all configuration information was stored on the servers themselves.
- configuration not documented/updated

Ex: ordering a VPS  
When we placed our order BEFORE AUTOMATION WAS IN PLACE, SOMEONE WOULD HAVE TO manually allocate both the hardware and software resources. We would then install the OS, cPanel/WHM, and the other default server software, and we would test to make sure everything is working correctly.

SOLUTION: IaC = automation: a single click perform multiple complex tasks

Describes the entire infrastructure in code form
Server documentation being translated into human-readable, maintainable, well-written code

IaC Approach
- Declarative (functional)    describes what the problem is and the expected result.
- Imperative (procedural)     focused on what changes to make.
- Intelligent                 explains why the infrastructure should be configured this way.
    
IaC methods
- Push    the management host sends configuration changes
- Pull    the primary host itself initializes the receipt of its configuration


## Configuration Management: define tasks 
 
|Tools|Year|Method|Approach|Lang|
|---|---|---|---|---|
|Ansible|2012|Push|Dec & Imperative|Python|
||system for describing and managing configurations|
|Chef|2009|Pull|Dec & Imperative|Ruby|
|| configuration management system for automation and control of current processes|
|Puppet|2005|Pull|Declarative|Ruby|
||to manage the OS and App configuration installed on multiple computers|
|SaltStack|2011|Push & Pull|Dec & Imperative|Python|
||configuration management and remote execution system|

Comparison of different lac tools 


|       | Terraform   | Ansible | Chef | Puppet | SaltStack |
|---|---|---|---|---|---|
| code | Open Source   | Open Source | Open Source | Open Source | Open Source |
| Cloud | All   | All | All | All | All |
| Type | Orchestration   | Config Mgmt | Config Mgmt | Config Mgmt | Config Mgmt |
| Infrastructure | Immutable   | Mutable | Mutable | Mutable | Mutable |
| Language | Declarative   | Procedural | Procedural | Declarative | Declarative |
| Architecture | Client Only   | Client Only | Client/Server | Client/Server | Client/Server |

## Configuration Orchestration: play tasks in order

Automate the deployment of servers and other infrastructure

|Tools|Year|Method|Approach|Lang|
|---|---|---|---|
|Google Cloud Deployment Manager|	2015|	Push|	Declarative|	Go|
||specify the resources needed for our application in a declarative format using yaml files |
|Terraform	|2014	|Push|	|Declarative	|Go|
||open-source infrastructure as code software tool created by HashiCorp. Users define and provision data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language (HCL), or optionally JSON|
|Azure Resource Manager|2014|Push|Declarative||
||To deploy and manage Azure services|
|AWS Cloudformation|https://aws.amazon.com/fr/cloudformation|

## IaC Problems

Exotic DSL (domain-specific language): description of the language used in each application
Diversity of Technologies

## DSC - Desired State Configuration platform 

To configure machines, environments, and processes. Using DSC allowed them to define configurations from a single source of truth, as well as deploy multiple environments.
- https://github.com/SteveByerly/dsc-demo
- https://intellitect.com/powershell-dsc/

## More

- https://medium.com/workfall/how-to-manage-infrastructure-as-code-iac-with-terraform-on-aws-1fa6cd6bccfe