## JENKINS

https://jenkins.io/

Java open-source Automation server tool 
To build, test, deliver, deploy software via ci (continuous integration) processes. 
+ 1,500 plugins: support all kinds of automation tasks

Facilitates continuous integration and continuous delivery in software projects by automating parts related to  build, test and deployment.   
Software build using build systems such as Gradle, Maven, and more.  
Automation testing using test frameworks such as Nose2, PyTest, Robot, Selenium, and more.  
Execute test scripts (using Windows terminal, Linux shell...)
Test automation with Selenium, etc.
### Jenkins Pipeline

pipeline { 
    
    agent { 
        docker { 
            image  'ubuntu'
                }
            }
    }
        
    agent any 
        stages { 
            stage ('Build') { 
                steps { 
                    echo 
                    'Running build phase. ' 
                }
            }
            stage ('Test') {         
            }
            stage ('QA') {             
            }
            stage ('Deploy') {            
            }
            stage ('Monitor') {    
            }
        }
    }

pipeline  {
includes all the processes (create, check, deploy..)
* declarative pipelines
* scripted pipelines
}

node  {
a system running a complete workflow 
part of the syntax of the scripted pipeline
}

Agent { 
a directive that can run multiple builds using just one Jenkins instance
Workload is Spread to various agents and execute multiple projects within Jenkins’s single instance. It instructs Jenkins to assign the builds to an executor.

Any
Runs the stage pipeline on any available agent.

None
This parameter is added to the root of the pipeline. It means that there is no global agent for the entire pipeline, and each stage must define its own agent.

Label
Performs on the labeled agent the pipeline/stage.

Docker
Uses a docker container as a pipeline execution environment
Pull an image of Ubuntu. This image can now be used to run multiple commands as an execution environment    
}

Stages { 
Work that needs to be completed. The work is defined in the form of stages.
Each stage executes a particular task
}

Steps {
Within a stage block, the pipeline can be described as a series of steps. 
}
### More
- https://www.lambdatest.com/blog/what-is-jenkins  
- https://devopsmyway.com/jenkins-github-integration
- https://devopsmyway.com/jenkins-job-create-your-first-build-job/
- https://www.lambdatest.com/blog/jenkins-pipeline-tutorial