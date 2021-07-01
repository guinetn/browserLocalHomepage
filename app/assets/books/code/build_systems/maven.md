# MAVEN

https://maven.apache.org/
http://linsolas.developpez.com/articles/java/outils/builds/
http://maven.apache.org/guides/getting-started/index.html

## Apache Maven is a build tool for Java and other JVM-based projects

Software project manager
Manage a project´s build, reporting and documentation from a central piece of information
Automatic build tool
. Compilation
. Deployment du livrable on a "repository" 						
. Code Quality Report (Sonar)

POM.xml (PROJECT OBJECT MODEL): project description
. l´endroit où se situent le code source et les fichiers de ressources
. la version de Java utilisée pour compiler le code source
. les dépendances directes du projet
. les plugins utilisés
. les rapports techniques demandés
...


Maven breaks an application into many smaller components to 
. bring in third party components 
. share your own components
Maven components are stored in repositories
component repositories and the dependency mechanism

Convention over Configuration 		
. source files are in src/main/cpp
. compiled classes were placed in ${basedir}/target/classes

### MAVEN PROJECT STRUCTURE

        my-app 
        |pom.xml 							← At the root of the project
        |__src                              ← All of the source files should be under it
            |__main                         ← All of the main application sources go under this folder
            |	|___C++                     ← project´s source files for the component (no need to specify it because 'convention')
            |   |     |___ file.cpp                      
            |   |
            |   |___resources 				← component´s resources (properties files…) copied to the output folder during the build process
            |
            |__test 
                |___C++
                |    |___ filetest.cpp
                |  
                |___resources 	            ← Test resources – used only during testing

        pom.xml		     
        <project>
            <modelVersion>4.0.0</modelVersion>
            <groupId>com.mycompany.app</groupId>
            <artifactId>my-app</artifactId>
            <version>1.0</version>                     ← if you are still working on it, you should stick '-SNAPSHOT' after the version number
            <packaging>jar</packaging>                   (“Draft” or “Work in Progress” component)
        </project>


    DEPENDENCIES
        Une librairie (component) est définie par trois informations: groupId, artifactId, version. Add these 3 in you pom
        Ex: use lib log4j in version 1.2.14 (maven take it in the REMOTE REPO and copy it in LOCAL REPO)

            <dependencies>
                <dependency>
                    <groupId>log4j</groupId>
                    <artifactId>log4j</artifactId>
                    <version>1.2.14</version>
                <dependency>
            </dependencies>

                POM.xml

                ↑ 1
            
                M A V E N    →  REMOTE REPO
                            3      ↓ 
                ↓ 2  ↑ 5           ↓ 
                                   ↓
            LOCAL REPO   ← ← 4 ← ←

            Maven commence par définir la liste des dépendances nécessaires au projet, via la lecture du pom.xml du projet.
            Maven interroge alors le repository local afin de trouver les dépendances utilisées.
            Si la dépendance n'est pas trouvée, alors Maven va interroger les repositories distants.
            Les dépendances absentes du repository local sont alors téléchargées depuis les repositories distants, de telle façon à ce qu'elles soient disponibles lors des prochains builds.
            Maven peut alors utiliser la dépendance pour la construction du projet.

            Other sample

                <dependencies>
                    <dependency>
                        <groupId>log4j</groupId>
                        <artifactId>log4j</artifactId>
                        <version>1.2.17</version>
                    </dependency>
                    <dependency>
                        <groupId>junit</groupId>
                        <artifactId>junit</artifactId>
                        <version>4.10</version>
                        <type>jar</type>
                        <scope>test</scope>
                    </dependency>
                </dependencies>


COMMANDS
            mvn compile 		download your dependencies and compile you c++ files
            mvn package		 	create a jar file in the target folder

            MAVEN BUILD LIFECYCLE

                validate 									validate the project is correct and all necessary information is available
                    ↓
                    Compile 								compile the source code of the project
                        ↓
                        Test 								test the compiled source code using a suitable unit testing framework. 
                            ↓ 								These tests should not require the code be packaged or deployed		
                            Package 							take the compiled code and package it in its distributable format, such as a JAR.
                                ↓
                            Integration-test 				process and deploy the package if necessary into an environment where integration tests can be run
                            ↓
                            verify 							run any checks to verify the package is valid and meets quality criteria
                            ↓
                        Install 							install the package INTO THE LOCAL REPOSITORY, for use as a dependency in other projects locally
                            ↓
                        Deploy	 							done in an integration/release env, copies final package to the remote repository for sharing with 
                                                            other developers and projects

TERMS
    repository		Endroit où sont stockés les différents artefacts, les librairies, etc
    livrable    	(artefact)	Produit final de la construction du projet: exe, librairie Java (JAR), une application web (WAR), ZIP, ...
    snap 			casser, rompre
    snapshot 		instantané
    
    JAR 			(Java Archive) is a package file format typically used to aggregate many Java class files and associated metadata and resources 
                    (text, images, etc.) into one file to distribute application software or libraries on the Java platform.
                    JAR files are packaged with the ZIP file format

                    In the Java world, the standard unit of delivery is the jar/war/(x)ar file. 
                    For applications which don’t fit the ‘single file’ delivery model, there is no standard alternative.  
                    To provide a solution, I will show you how to package your application with Maven as an RPM.

    RPM 			RPM Package Manager (RPM) (originally Red Hat Package Manager), a Linux format for distributing software bundles for easy installation on 					Linux, Novell/SuSE…
                    It is like a super-zip
                    RPM distributions may or may include source and/or binaries

NEXUS: gestionnaires de repositories locaux
http://nexus.sonatype.org/






