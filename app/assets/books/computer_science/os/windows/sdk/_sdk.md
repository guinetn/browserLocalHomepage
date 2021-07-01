# SDK - Software development kit

a collection of APIs that you can reference as a single item in Visual Studio. 
The Reference Manager dialog box lists all the SDKs that are relevant to the project. When you add an SDK to a project, the APIs are available in Visual Studio.

Two types of SDKs:

***Platform SDKs***
Mandatory components for developing apps for a platform. For example, the Windows 8.1 SDK is required to develop Windows 8.x Store apps.

All platform SDKs install in: HKLM\Software\Microsoft\Microsoft SDKs\[TPI]\v[TPV]\@InstallationFolder = [SDK root]. 
Accordingly, the Windows 8.1 SDK is installed at HKLM\Software\Microsoft\Microsoft SDKs\Windows\v8.1.

ex: Ordinateur\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Microsoft SDKs\ServiceHosting\v2.9
    FullVersion=2.9.8899.26
    InstallPath=C:\Program Files\Microsoft SDKs\Azure\.NET SDK\v2.9\
    
```text
\[InstallationFolder root]
            SDKManifest.xml         describes how Visual Studio should consume the SDK.
                <FileList 
                    DisplayName="Windows" 
                    PlatformIdentity="Windows, version=8.1" 
                    TargetFramework=".NET for Windows Store apps, version=v4.5.1; .NET Framework, version=v4.5.1" 
                    MinVSVersion="14.0"> 
                    <File Reference="Windows.winmd"> 
                        <ToolboxItems VSCategory="Toolbox.Default" /> 
                    </File> 
                </FileList>
            \References             API binaries that can be coded against: Windows Metadata (WinMD) files or assemblies.
                  \[config]
                        \[arch]
            \DesignTime             XML docs, libraries, headers...files that are needed only at pre-run/debugging time
                  \[config]
                        \[arch]     x86, x64, ARM, and neutral
```

***Extension SDKs*** 
Optional components that extend a platform but aren't mandatory for developing apps for that platform.
Can be installed for 
- all users:   %Program Files%\Microsoft SDKs<target platform>\v<platform version number>\ExtensionSDKs
Defined in HKLM\Software\Microsoft\Microsoft SDKs<target platform>\v<platform version number>\ExtensionSDKs<SDKName><SDKVersion>\
- a user-specific: %USERPROFILE%\AppData\Local\Microsoft SDKs<target platform>\v<platform version number>\ExtensionSDKs


General infrastructure of SDKs
Create a platform SDK and an extension SDK

https://docs.microsoft.com/en-us/visualstudio/extensibility/creating-a-software-development-kit?view=vs-2019
https://docs.microsoft.com/en-us/visualstudio/extensibility/walkthrough-creating-an-sdk-using-csharp-or-visual-basic?view=vs-2019