# Terraform
 
 Tool for infrastructure provisioning to build out infrastructure through code (infrastructure as code software tool)
 open-source created by HashiCorp 
 Users define and provision data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language (HCL), or optionally JSON
 You define WHAT you want (the desired "end state") rather then describing exactly each step or HOW to do it.
 
 infrastructure can be
 - Created
 - Adjusted/Changed
 - Replicated (dev/prod)
 
 CODE / PLAN / APPLY
### Infrastructure provisioning

Infrastructure = servers, microservices, apps & DB (docker containers)

A. Prepare Infrastructure:
1. Private network space
2. EC2 server Instances
3. install docker...
4. Security

2 main Compoenents:

```
provider "aws" {
    version = "~> 2.0
    region  = "us-east-1" 
} 
resource "aws-vpc" "example" {
    cidr_block = "10.0.0.0/16"
}
```
TF-Config
  +
  +
  +-------> CORE compare state VS desired state (config file) 
  +              Execution Plan: what needs to be created/updated/destroyed    
  +
State (current setup state)
- remove 2 servers (or i want 7 servers)
- add firewall config
- add permissions to aws user
 
 
Providers: 100+
- AWS, Azure, IaaS
- Kubernetes, PaaS
- Fastly, SaaS

B. Deploy application

Terraform does:
Create VPC ('virtual private cloud)
Create AWS users, permissions
Spin up servers
Install Docker

- Terraform vs Ansible
Both IAC

### Terraform Basic Commands

- Refresh
Query infrastructure provider to get current state
- Plan (preview, not real impact)
Create an execution plan. can be an update, a remove...
- Apply
Execute the plan
- Destroy
destroy the resources/infrastructure

## MORE
 - https://github.com/priximmo/sommaire-xavki-devops-fr
 - https://www.freecodecamp.org/news/build-a-screenshot-capture-api-using-terraform-aws-api-gateway-and-aws-lambda/
 - https://www.youtube.com/hashtag/terraform
- https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFpFZ1A4REpuUmlrRnFuNnlDVzRQdXhaeU1yd3xBQ3Jtc0ttZm5aaTdhQll2czJDbjM2c0tCSmRyNDh1OEdGa3dhcUJJUzUxdHg4b3E1VEZ3QUdvMkJrZTdha0c3WWR2X2ZZVU9NamxyZ3J3M2JXZ1FkUy1scnJDTFQ2UmtzYUxyVWMxQ193bFZiSzFwWGdMRVZOQQ&q=https%3A%2F%2Fwww.terraform.io%2Fdocs%2Fproviders%2Findex.html 
- https://medium.com/workfall/how-to-manage-infrastructure-as-code-iac-with-terraform-on-aws-1fa6cd6bccfe
- https://medium.com/bb-tutorials-and-thoughts/how-to-create-a-static-website-on-azure-with-terraform-9971e55e2884
