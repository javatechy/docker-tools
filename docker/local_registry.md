
# Create your own local regisrty on your machine

docker pull registry

docker run -d -p 5000:5000 --name localregistry registry
 
This will start local reistry in the background

Push to local registry:

Tag and push on local repos

docker tag alpine:latest localhost:5000/myalphineL:latest
docker push localhost:5000/myalphine:latest
