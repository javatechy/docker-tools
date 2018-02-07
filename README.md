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
##### Run mysql on docker
```
docker run --name mysql -p 3306:3306 -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1 -d mysql
```
#### Run mysql on docker
```
docker run -d -p 3000:3000 -v metabase-data:/tmp -e "MB_DB_FILE=/tmp/metabase.db" --name metabase metabase/metabase
```
##### Execute a mysql
```
docker exec -it mysql bash
```

#### Remove Stopped Containes
```
docker ps -aq --no-trunc | xargs docker rm
```

#### Remove container
```
docker rm 036a0bcd196c5___id
```

#### Install Kafka
```
docker run -p 2181:2181 -p 9092:9092 -d --env ADVERTISED_HOST=`docker-machine ip \`docker-machine active\`` --env ADVERTISED_PORT=9092 spotify/kafka
```

#### Cloning:
Clone the project `git clone https://github.com/javatechy/fab-backend.git`

**Note**: Relax and play Fur Elise, It will work  .




mvn install:install-file -Dfile=../java-utils/base/target/base-0.1.jar -DgroupId=com.google.code -DartifactId=base -Dversion=0.1 -Dpackaging=jar
mvn install:install-file -Dfile=../java-utils/sqljpa/target/sqljpa-0.1.jar -DgroupId=com.google.code -DartifactId=sqljpa -Dversion=0.1 -Dpackaging=jar



