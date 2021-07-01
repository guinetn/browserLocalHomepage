# .NET Core applications on Linux

Since Microsoft started moving away from closed-source and platform-dependent solutions, a Linux-based development environment has its advantages. I believe tools like VSCode and Rider—also available on every platform

.NET Core runtime 
    To run applications on Linux that were made with .NET Core but didn’t include the runtime. 
    Need only the runtime in a production environment

.Net Core SDK
    To run & develop and build .NET Core applications. 
    Need the SDK only in a development environment

* Install .NET Core SDK/Runtime on Linux    
> wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
>sudo apt-get update; \
>  sudo apt-get install -y apt-transport-https && \
>  sudo apt-get update && \
>  sudo apt-get install -y dotnet-sdk-3.1

>dotnet --version
>dotnet build
>dotnet run

- https://www.roundthecode.com/dotnet/asp-net-core-web-hosting/how-to-install-an-asp-net-core-in-net-5-app-on-ubuntu-20-04