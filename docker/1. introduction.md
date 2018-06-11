#  Persistant nature of docker
```
> docker run -t -i busybox
> del *.*
> exit
```

## Search An image on docker hub

```
docker search busybox

docker images

docker ps -a
```

# Pull an image from docker hub

```
docker pull image_name
```

# Remove a container: ()

```
docker rm MyWebServer
```

# Random Ports mapping

```
docker run -d --name MyWebServer -P httpd
```
* --name :  name of the container
* -P. What this parameter does is that it “Publish all exposed ports to random ports”

#  Port Mapping: 

-p HostPort:ContainerPort
 
 
 Images are Immutable and Containers are Ephemeral”
 
 ```
 $ docker run -it --name mycontainer1 --rm ubuntu:latest
 ```
 — rm flag while starting the container, which means that the container is removed on termination.
 
 
 
 # Persist Changes in the container:
 
```
$> docker run -it --name test_container busybox
$> vi temp
# add commetnsd s 
$> exit 
# Docker push to repository
$> docker commit test_container javatechy/test_container
$> docker push javatechy/test_container
```

