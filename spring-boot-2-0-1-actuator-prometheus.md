# Adding acctutor and micrometer-prometheus in spring boot 2.0.1


## add endpoints

management.endpoint.prometheus.enabled=true
management.endpoints.web.exposure.include: health,prometheus,info,metrics,threaddump
management.metrics.export.prometheus.enabled=true



## add pom changes

```
<!-- https://mvnrepository.com/artifact/io.micrometer/micrometer-registry-prometheus -->
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
    <version>1.0.3</version>
</dependency>
		<!-- https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-actuator -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
		

```

## testing

Endpoints - for thread dump

- /actuator/threaddump
- /actuator/info
- /actuator/prometheus
- /actuator/health