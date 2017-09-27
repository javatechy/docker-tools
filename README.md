# Docker Tools
This project aimed to setup tools.

Jenkins:
-----------------------------

Assuming:
 * Docker is installed

Jenkins
-----------------------------
Follow these steps to run this project:

Reference : https://docs.docker.com/samples/library/jenkins/
Assuming /Users/deepak/jenkins-data is already created for jenkins
 * run this command `docker run -p 8080:8080 -p 50000:50000 -v /Users/deepak/jenkins-data:/var/jenkins_home jenkins`

#### Cloning:
Clone the project `git clone https://github.com/javatechy/fab-backend.git`

Database Structure
-----------------------------
Following are created:
* `Jenkins`: for storing users wallet balance

**Note**: Relax it will work.
