add logs.dir path in application.properties

add logback-spring.xml 
```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	<include resource="org/springframework/boot/logging/logback/base.xml" />

	<appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
		<layout class="ch.qos.logback.classic.PatternLayout">
			<Pattern>%d%thread] %-5level %logger - %msg%n</Pattern>
		</layout>
	</appender>

	<appender name="request"
		class="ch.qos.logback.core.rolling.RollingFileAppender">
		<file>${logs.dir}/application.log</file>
		<append>true</append>
		<rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
			<!-- <fileNamePattern>${logs.dir}/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern> -->
			<fileNamePattern>/Users/deepak/projects/fab/fab-backend/applicationlog/application.%d{yyyy-MM-dd}.%i.log</fileNamePattern> 
			 
			<timeBasedFileNamingAndTriggeringPolicy
				class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
				<!-- or whenever the file size reaches 100MB -->
				<maxFileSize>200MB</maxFileSize>
			</timeBasedFileNamingAndTriggeringPolicy>
		</rollingPolicy>
		<encoder>
			<pattern>%d[%thread] %-5level %logger - %msg%n</pattern>
		</encoder>
	</appender>

	<root level="INFO">
		<appender-ref ref="request" />
	</root>
</configuration>

```