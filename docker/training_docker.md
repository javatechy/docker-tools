# Introduction:
- Docker - Container service CE & EE and Container VS. VMs
 
 Now hotelier is running on Docker on Dev ENV. Please let me know if something is not working @Hasrh
Installation:

✓ Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/#upgrade-docker-after-using-the-convenience-script
✓ Mac https://store.docker.com/editions/community/docker-ce-desktop-mac
- create your account on https://hub.docker.com/
✓ Play your game here :https://labs.play-with-docker.com/

https://www.tutorialspoint.com/docker/images/various_layers.jpg

- Test Cases - env basedwifi_fab!
- wifi_fab!

# Images:
 
 - Search an image docker search busybox
 - Pull and image docker pull image_name
 - docker repository
  
# Containers:

 - Remove a container
 - Random Ports mapping : -P port/random mapping : -p HostPort:ContainerPort
 - docker rm MyWebServer
 - docker inspect <container_id>
 - Go inside a container docker exec -it <cname> bash
 - docker inspect sample_container
 
# Volumes: 
 
 - Volume attached to busybox : 
 	- docker run -it -v /datadeepak --name sample_container  busybox
 - Check location of this volume
 - Check all volumes list docker volume ls
 - docker volume prune
 - docker volume rm Remove one or more volumes
 
# Images Demo:
- docker run -d --name MyWebServer -P httpd 

- docker run --name elasticsearch  -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -v elasticsearch-data_1:/usr/share/elasticsearch javatechy/elastdump:1.0
- docker exec elasticsearch sh export $SOURCE_SERVER:9200 user-index


docker run -it -p 5600:5601 --name kibana --link elasticsearch:elasticsearch  docker.elastic.co/kibana/kibana:6.2.4


docker exec elasticsearch sh devexport http://35.154.206.110:9200 user-index,
- jenkins etc.

- docker run --name mysql -p 3306:3306 -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1 -d mysql

-  Check all images  docker images
- remove all changes
- Run an image in interactive mode
 

# Persist Changes in the container:

- docker run -it --name test_container busybox
-  vi temp add commetnsd s  and exit 
- Docker push to repository
- docker commit test_container javatechy/test_container
- docker push javatechy/test_container


# Data volume containers:

if you want to share data between containers or you want to use the data 
from non-persistent containers. The process is really two step

```
$ docker run -it -v /data --name container1 busybox
$ docker run -it --volumes-from container1 --name container2 busybox
$ docker run -it --volumes-from container1 --name container3 busybox
$ docker run -it --volumes-from container1 --name container4 busybox
```

# Registry: Local & remote

- docker pull registry
- docker run -d -p 5000:5000 --name localregistry registry
- docker tag alpine:latest localhost:5000/myalphineL:latest
- docker push localhost:5000/myalphine:latest

# Linking Containers:

- docker run -d --name redis1 redis
- docker run -it --link redis1:redis --name redisclient1 busybox
- cat /etc/hosts
- docker run -it --link redis1:redis --name client1 redis sh
- redis-cli -h redis

# Build Your own image:

FROM busybox:latest
MAINTAINER Deepak Kumar (deepak.kumar@fabhotels.com)
CMD ["date"]
EXPOSE 80

docker build -t myimage:latest .
docker run -it myimage
docker run -d -p 80:80 --name webserver myimage
docker images
docker run -it myimage
 
# Dockerizing Spring boot:
 - Mention repository
 - Docker file and Wrapper.
 - Ref http://www.mojohaus.org/properties-maven-plugin/

# Dockerizing FabHotelier Spring Apps:
 
 - Property manager
 - Spring profiling
 - Embedded Tomcat
 - Deploy.sh
 - acctuator / Replaces health check

```
###.  Run a docker images
docker run -it -v /var/log/casa:/var/log/casa -p 9000:8000 -e ENV_NAME=local 425123548659.dkr.ecr.ap-south-1.amazonaws.com/hotelier:1.0 --rm

docker run -it -v /var/log/casa:/var/log/casa -p 9000:8000 -e ENV_NAME=dev -d 425123548659.dkr.ecr.ap-south-1.amazonaws.com/hotelier:1.0

docker run -it -v /var/log/casa:/var/log/casa -e ENV_NAME=local -p 9000:8000 javatechy/dockboot:1.0
```

# ECS/Kube:

 - Create Repository in ECR
 - Create Tasks
 - Create Cluster
 - minikube start && kubectl port-forward hello-nginx-556b7bf96-7vlbd 8001:80 
 - aws ecr get-login --no-include-email --region ap-south-1
 - aws ecr create-repository --repository-name hotelier


# Prune:
- Prune Commands -  docker system df
