# intro
A Dockerfile is a text file that has a series of instructions on how to build your image

###Supported Commands:

Set of commands:

```
FROM, CMD, ENTRYPOINT, VOLUME, ENV etc.
```

### Steps:
 
 * create  a file named `Dockerfile` for docker instructions.
 * Sample  codes:

```
FROM busybox:latest
MAINTAINER Romin Irani (email@domain.com)
CMD ["date"]
EXPOSE 80
```

 *  ** FROM ** : command sets the base image for the rest of the instructions. 
 *  ** MAINTAINER ** :  author of the generated image
 *  **  CMD ** :if you want to execute a custom command after instruction.
 *  **  EXPOSE ** :  EXPOSE command here to inform what port the container will be listening on. 
 
 Remember in our earlier chapters, we saw that if we use the -P command, then the EXPOSE port will be used by default.
  
### Build Image:
 
  ```
  docker build -t myimage:/version/ .
 
  examples:
 
  docker build -t myimage:latest .
  docker build -t myimage:1.1 .
  ```
 * -t is the Docker image tag. You can give a name to your image and a tag.
 *  ‘.’ specifies the location of the Dockerfile
 
 Output:

``` 
 $ docker run -it myimage
Thu Dec 14 11:14:42 UTC 2017
```

 ```
 docker run -d -p 80:80 --name webserver myimage
 ```
 
 Check all created images:
 ```
  docker images
 ```
 
 Run an images in iteractvie image:
 
 ```
 docker run -it myimage
 ```

 
 References:
 * https://rominirani.com/docker-tutorial-series-writing-a-dockerfile-ce5746617cd