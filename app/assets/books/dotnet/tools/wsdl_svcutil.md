## SVCUTIL - WSDL
 to scaffold the code that will be used to interact with the service with the help of a tool called ServiceModel Metadata Utility Tool (Svcutil).
>dotnet tool install --global dotnet-svcutil
# make project dir & change into that dir
$ mkdir TempConvert && cd TempConvert
# create solution
$ dotnet new sln
# make src dir & cd
$ mkdir src && cd src
# make webapi project & cd back
$ dotnet new webapi -o TempConvert
$ cd ..
# add webapi project to solution
$ dotnet sln add src/TempConvert/TempConvert.csproj

cd src/TempConvert
$ dotnet-svcutil https://www.w3schools.com/xml/tempconvert.asmx?wsdl

The tool will generate Classes & Interfaces that we will use to communicate with the service.
../TempConvert/src/TempConvert/ServiceReference/Reference.cs

https://medium.com/swlh/consuming-wsdl-services-using-asp-net-core-141fbc77924f

