# Docker Tools
This project aimed to setup tools.

Assumptions:
-----------------------------
 * Docker is installed

Jenkins
-----------------------------
Follow these steps to run this project:

Reference : https://docs.docker.com/samples/library/jenkins/
Assuming /Users/deepak/jenkins-data is already created for jenkins
 * run this command `docker run -p 8080:8080 -p 50000:50000 -v /Users/deepak/jenkins-data:/var/jenkins_home jenkins`

Nexus
-----------------------------

Reference : https://hub.docker.com/r/sonatype/nexus3/
 * run this command `docker run -p 8080:8080 -p 50000:50000 -v /Users/deepak/jenkins-data:/var/jenkins_home jenkins`

Prometheus
------------------
```
docker pull prom/prometheus
docker run -p 9090:9090 prom/prometheus
```
#### Cloning:
Clone the project `git clone https://github.com/javatechy/fab-backend.git`

**Note**: Relax and play Fur Elise, It will work  .
