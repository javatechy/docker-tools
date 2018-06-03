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
##### Execute a image bash
```
docker exec -it images_name bash
```

#### Remove Stopped Containes
```
docker ps -aq --no-trunc | xargs docker rm
```

#### Remove container
```
docker rm 036a0bcd196c5___id
```

#### Check all images
```
docker images
```

### docker push an image

$docker tag my_image $DOCKER_ID_USER/my_image

Push your image to Docker Hub using docker push (making the same replacements as in the previous step).

docker push $DOCKER_ID_USER/my_image
 
```
docker tag codegen javatechy/codegen
docker push javatechy/codegen
```


