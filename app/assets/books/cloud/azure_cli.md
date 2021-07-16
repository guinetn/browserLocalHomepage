## Azure cli: commands used to create and manage Azure resources

- https://docs.microsoft.com/en-us/cli/azure/
- https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
- https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli 

## Cloud shell

Cloud Shell is a browser-accessible interactive shell.

- https://www.red-gate.com/simple-talk/devops/containers-and-virtualization/running-container-workloads-in-microsoft-azure/
- https://shell.azure.com/


>az account show
>az account set --subscription 'my azure subscription or ID'        to change subscription


>az login
>az find secret
>az network nsg --help
>az account list

* CREATE AND RUN A CONTAINER INSTANCE
>az group create --name <resource-group> --location <location>
>az group create --location westus --resource-group MyResourceGroup
>az group create --location westeurope --resource-group MyResourceGroup --tags {tags}
>az group list --query "[?location=='westeurope']"
>az group create --name TutorialResources --location eastus

CONTAINERS
>az group create --name mycontainerrg --location westus
>az container create --resource-group mycontainerrg --name mynginxv1 --image dockdemorepo/myacirepo:nginx-helloworld --ports 80 --dns-name-label mynginxv1 --location westus
The value for –dns-name-label should be unique. If the name you are trying is taken by someone else in the same location (westus), it will error out. 

Start and stop containers
>az container stop --name mynginxv1 --resource-group mycontainerrg
>az container start --name mynginxv1 --resource-group mycontainerrg

View container-related logs:
>az container logs --name mynginxv1 --resource-group mycontainerrg

Execute shell commands inside the container
>az container exec --exec-command /bin/bash --container-name mynginxv1 --resource-group mycontainerrg --name mynginxv1

Access web page served by the NGINX by using the FQDN provided in the container creation output.


VM
>az vm list
>az vm show
>az vm create --resource-group TutorialResources --name TutorialVM1 --image UbuntuLTS --generate-ssh-keys --output json --verbose
    --generate-ssh-keys → SSH key named id_rsa
    SSH key files 'C:\Users\nguin\.ssh\id_rsa' and 'C:\Users\nguin\.ssh\id_rsa.pub' have been generated 
    under ~/.ssh to allow SSH access to the VM. If using machines without permanent storage, back up your keys     to a safe location.
    It is recommended to use parameter "--public-ip-sku Standard" to create new VM with Standard public IP. 
{
  "fqdns": "",
  "id": "/subscriptions/3f4...121b7/resourceGroups/TutorialResources/providers/Microsoft.Compute/virtualMachines/TutorialVM1",
  "location": "eastus",
  "macAddress": "00-0D-3A-8A-83-62",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "13.92.183.89",          → CONNECT TO ssh <PUBLIC_IP_ADDRESS>
  "resourceGroup": "TutorialResources",
  "zones": ""
}

>ssh 13.92.183.89
    The authenticity of host '13.92.183.89 (13.92.183.89)' can't be established.
    ECDSA key fingerprint is SHA256:Fk...Qg.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '13.92.183.89' (ECDSA) to the list of known hosts.    

    Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1051-azure x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    System information as of Thu Jul  8 09:53:14 UTC 2021

    System load:  0.13              Processes:           112
    Usage of /:   4.6% of 28.90GB   Users logged in:     0
    Memory usage: 5%                IP address for eth0: 10.0.0.4
    Swap usage:   0%

C:\Users\nguin\.ssh
    📝 known_hosts
    13.92.183.89 ecdsa-sha2-nistp256 AAA5446...dU8=
    📝 id_rsa
    -----BEGIN RSA PRIVATE KEY-----
    MIIEp...
    📝 id_rsa.pub
    ssh-rsa AAAA...xX
    
>az vm show --name TutorialVM1 --resource-group TutorialResources
Get the network interface controller (NIC) object ID: 
>az vm show --name TutorialVM1 --resource-group TutorialResources --query 'networkProfile.networkInterfaces[].id' --output tsv
>az group delete --name TutorialResources --no-wait     ui not blocked
>az group wait --name TutorialResources --deleted       ui blocked



Resource type	Azure CLI command group
Resource group	az group
Virtual machines	az vm
Storage accounts	az storage account
Key Vault	az keyvault
Web applications	az webapp
SQL databases	az sql server
CosmosDB	az cosmosdb

--help          commands information, lists available subgroups and commands.
--output   -o   output format. json (default), jsonc (colorized JSON), tsv (Tab-Separated Values), table, yaml
--verbose       information about resources created in Azure during an operation...
--debug         more information about CLI operations
--query         uses the JMESPath query language to filter the output returned from Azure services
                [JMESPath query language](http://jmespath.org/)
                Queries are written in the JMESPath query language.
                Get the network interface controller (NIC) object ID: az vm show --name TutorialVM1 --resource-group TutorialResources --query 'networkProfile.networkInterfaces[].id' --output tsv
--resource-group  -g
--name -n
