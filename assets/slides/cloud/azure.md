# AZURE

## 1. Creating an Azure App Service using Command Line

|||
|---|---|
|az login  |Login to Azure<br/>A browser window will open asking for your Microsoft Account credentials|
|az group create --name myResourceGroup --location westus|Add a Resource Group|
|az configure --defaults group=myResourceGroup location=westus|Set the default resource group and location for all subsequent commands|
|az appservice plan create --name myPlan --sku F1|Create an App Service plan|
|az webapp create --name __your_app_name__ --plan myPlan --runtime "DOTNETCOREi3.1"|Create the App Service itself|
|http://__your_app_name__.azurewebsites.net|Check app Service is running|

## 2. Deploying the App to Azure App Service using Command Line

|||
|---|---|
|az webapp deployment user set --user-name &lt;username&gt; --password &lt;password&gt;|Set deployment credentials. Replace username and password with your azure credentials.|
|az webapp deployment source config-local-git --name &lt;your_app_name&gt;|Retrieve the Git endpoint to which we want to push the app code:<br/>output: { "url": "https://gergely.sinka@mydomain.com@&lt;your_app_name&gt;.scm.azurewebsites.net/&lt;your_app_name&gt;.git"}|
|git remote add azure https://&lt;your_app_name&gt;.scm.azurewebsites.net/<your_app_name>.git|Set output URL without credentials as a remote for the local git repository:|
|git push azure master|Push the code to the new remote repository:|
|Open http://&lt;your_app_name&gt;.azurewebsites.net|Make sure the app is running|
