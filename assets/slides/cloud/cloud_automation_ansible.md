# Ansible 

https://www.ansible.com/

Automation tool to manage remote machines. 
Agentless configuration management tool: doesn't require to install agents on remote machines for remote management. It manages remote machines over the SSH (RDP on Windows) protocols to open a connection to the client servers to execute  predefined commands.   

Ansible is installed on a Centralized Server and from there all other remote Machines are managed. Centralized Server where Ansible is installed is known as Control node and remote Machines are known as a Managed node.

System for describing and managing configurations
Python open-source tool that uses playbooks to enable configuration management, software provisioning, and application deployment.
Consistent, secure, reliable, and it requires a minimal learning curve. Simply put, Ansible is a powerful tool for automating apps and infrastructure. 
Red Hat IaC friendly tool
The enterprise version of this tool is called Ansible Tower, and it is capable of performing automation and orchestration tasks. 

Has transformed the industry. It is one of the critical components of modern technology firms that rely on a large number of machines or servers they need to maintain in their daily business.

Ansible is usually configured as a single active master server (referred to as a Primary Instance) as no agents are required to connect to it. A secondary master can be configured to take over if the master server goes down. Because Ansible uses an agent-less approach, it can deploy changes or push updates relatively quickly to all the nodes by an engineer. A downside to Ansible is that the client computers do not check for any periodic configuration changes on the primary master.

### Playbooks
    modules describing automation tasks   
    yaml configuration files (simplicity)
        SPACE INDENTED format for representing data
        File starts with — (3 hyphens)
    to deploy multi-tiered applications
    to run updates on clusters of servers, load balancers, or other specific monitoring servers (Prometheus,  Nagios). 

    It is also very easy to convert bash or shell scripts into playbooks

    Sets of “directives” (or plays) that a user can send to a single target server or multiple servers. 
    They are at the heart of Ansible itself and enable automating infrastructure management. 

    A task is an action that will be performed on the target hostname/s (executing a command, installing a package, etc.)

### hosts: inventory file
Add our hostnames so that Ansible understands the hosts where the playbook is executed.  
Add them one by one, but we can also create a group for easier targeting inside the playbook.

/etc/ansible/hosts
```txt

    mainserver.test.com

    [webservers]
    web01.test.com
    web02.test.com

    [dbservers]
    db01.test.com
    db02.test.com

    [apps]
    app01.test.com
    app02.test.com
```

### playbooks

Playbook sample: install and start-up httpd (apache) on the host 'mainserver.test.com'

```ansible
---
    name: install and start HTTPD         run this playbook only on one hostname – mainserver.test.com
    hosts: mainserver.test.com          ← to run this playbook on our webservers replace by a group name
    remote_user: root
    tasks:
    - name: Install HTTPD
         yum:
                name: httpd
                state: present
         
    - name: Start HTTPD
         service:
                 name: httpd
                 state: started
```


Install and configure Apache on all our servers within the [webservers] group noted in the inventory file.

playbook.yaml
```ansible
 ---
     name: Install and configure Apache
     remote_user: root
     hosts: webservers     

     tasks:
       - name: Install Apache.
         command: yum install --quiet -y httpd httpd-devel
       - name: Copy configuration files.
         command: cp httpd.conf /etc/httpd/conf/httpd.conf
         command: cp httpd-vhosts.conf /etc/httpd/conf/httpd-vhosts.conf
       - name: Start Apache and configure it to run at boot.
         command: service httpd start
         command: chkconfig httpd on
```
root@host:~# ansible-playbook playbook.yaml
root@host:~# ansible-playbook /etc/ansible/playbooks/playbook.yml

### Schedule playbooks

Ex: run /etc/ansible/playbooks/playbook.yml file at 0400 a.m
    crontab -e
    0 4 * * * /usr/bin/ansible-playbook /etc/ansible/playbooks/playbook.yml


- https://devopsmyway.com/how-to-install-ansible-on-amazon-linuxec2/
- https://devopsmyway.com/install-ansible-ubuntu-18-04/
- https://www.liquidweb.com/kb/how-to-use-ansible/
- https://www.liquidweb.com/kb/how-to-install-and-configure-ansible/
- https://www.liquidweb.com/kb/using-ansible-in-devops-a-beginners-guide/
- [ANSIBLE - 11. PLAYBOOK : PREMIERS PAS ET OPTIONS](https://www.youtube.com/watch?v=yN29WlhIUrI&feature=youtu.be)
