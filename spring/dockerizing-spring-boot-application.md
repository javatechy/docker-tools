###Dockerizing Spring boot  Applicaiton

add docker-maven-plugin plugin in your pom

```
		    <plugin>
				<groupId>com.spotify</groupId>
				<artifactId>docker-maven-plugin</artifactId>
				<configuration>
					<imageName>codegen</imageName>
					<baseImage>java:8</baseImage>
					<entryPoint>["java", "-jar", "/${project.build.finalName}.jar"]</entryPoint>
					<!-- copy the service's jar file from target into the root directory 
						of the image -->
					<resources>
						<resource>
							<targetPath>/</targetPath>
							<directory>${project.build.directory}</directory>
							<include>${project.build.finalName}.jar</include>
						</resource>
					</resources>
				</configuration>
			</plugin>
```


### Build Using this command

```
mvn docker:build
```

### Run built image on docker

```
docker run -it -p {destincation_port}:${application_port} codegen
```