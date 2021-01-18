# Chef

Configure & manage your cloud infrastructure with IaC (infrastructure as code) 
One of the main components of Chef is to push configurations (aka cookbooks) to all nodes connected on the server, which enables easier scaling and infrastructure modifications.
https://www.chef.io/

Chef’s configuration options consist of Cookbooks and Recipes. The recipes are the definition files that can be combined with attributes, files, libraries, and other recipes to build Cookbooks. These cookbooks can then be used for client deployment. 


* CHEF WORKSTATION 

The Chef workstation is used by system engineers to create, test, and deploy the cookbooks to the Chef master servers.

* CHEF MASTER SERVER 

Chef Servers are essentially the hub where all the Chef configuration data is stored. This information includes cookbooks, server data, and other relevant info.

- Stores information about your node’s current and desired configuration. 
- Push the desired configuration instructions (cookbooks) to all other nodes connected to the server. These instructions help us easily scale and modify our infrastructure if needed.
- Open Source / Enterprise pricing


* CHEF CLIENT 

The Chef client is the end-node machines managed by Chef master servers. These servers periodically pull and execute cookbook configurations from the Chef master server.
