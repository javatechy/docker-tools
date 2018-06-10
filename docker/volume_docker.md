
# Understanding Docker Volumes

 * Docker Volumes: means how to manage data within your Docker containers.
 * the fundamental thing that we are trying to get over here is to separate out the container lifecycle from the data
 *  even if the container is removed and in the future you launch another container, you would like that data to still be there.
 
 
# Few points to keep in mind about Data Volumes

* A data volume is a specially designed directory in the container.
* It is initialized when the container is created. By default, it is not deleted when the container is stopped. It is not even garbage collected when there is no container referencing the volume.
* The data volumes are independently updated. Data volumes can be shared across containers too. They could be mounted in read-only mode too.


Steps:

* Volume attached to busybox 

```
docker run -it -v /datadeepak --name sample_container  busybox
```

* it will create a voulme inside datadeepak
Now even if the container dies data will remain the same
create a file inside /datadeepak and create a sample file.

* docker attach sample_container

U will find the same data again insdie the datadeepak folder.


# Check location of this volume 

```
docker inspect sample_container
```

# Check all volumes

```
docker volume ls
```

# Remove all volumes/images/container

```
docker rm --help
```

# -v Option
To mount a host volume while launching a Docker container, we have to use the following format for volume -v :

```
-v HostFolder:ContainerVolumeName
```

# Mapping a volume from host machine to container

```
docker run -it --name container1 -v /Users:/datavol busybox
```

* this will map host machine's /Users to /datavol in busy box

* When you change somethis in /Users dir it will imediatly reflected in docker.
or vice versa

* a single host file too as a data volume.


# Data volume containers
if you want to share data between containers or you want to use the data from non-persistent containers. The process is really two step:

```
$ docker run -it -v /data --name container1 busybox
$ docker run -it --volumes-from container1 --name container2 busybox
$ docker run -it --volumes-from container1 --name container3 busybox
$ docker run -it --volumes-from container1 --name container4 busybox
```

