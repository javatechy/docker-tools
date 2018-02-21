# Spring prometheus Grafana

Prometheus
------------------

1.  Add following deps in 
```
<!-- start prometheus -->
		<dependency>
			<groupId>io.prometheus</groupId>
			<artifactId>simpleclient_spring_boot</artifactId>
			<version>0.0.26</version>
		</dependency>
		<dependency>
			<groupId>io.prometheus</groupId>
			<artifactId>simpleclient_hotspot</artifactId>
			<version>0.0.26</version>
		</dependency>
		<dependency>
			<groupId>io.prometheus</groupId>
			<artifactId>simpleclient_servlet</artifactId>
			<version>0.0.26</version>
		</dependency>

		<!-- end prometheus -->
```

2. add bean in @Configuration Class

```

    @Bean
    public SpringBootMetricsCollector springBootMetricsCollector(Collection<PublicMetrics> publicMetrics) {
        SpringBootMetricsCollector springBootMetricsCollector = new SpringBootMetricsCollector(publicMetrics);
        springBootMetricsCollector.register();
        return springBootMetricsCollector;
    }

    @Bean
    public ServletRegistrationBean servletRegistrationBean() {
        DefaultExports.initialize();
        return new ServletRegistrationBean(new MetricsServlet(), "/prometheus");
    }

```
3.  add @EnablePrometheusEndpoint in your root Applicaiton class.



# Install Prometheus On Docker

1.  First, create a minimal Prometheus configuration file on the host filesystem at ~/prometheus.yml:
2. Add following content in the file:

```
# A scrape configuration scraping a Node Exporter and the Prometheus server
# itself.
scrape_configs:
  # Scrape Prometheus itself every 5 seconds.
  - job_name: 'prometheus'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']

  # Scrape the Node Exporter every 5 seconds.
  - job_name: 'node'
    scrape_interval: 5s
    static_configs:
      - targets: ['myserver:7070']
```

3. Start the Prometheus Docker container with the external configuration file:

```
docker run -d -p 9090:9090 -v ~/softwares/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus 
// -storage.local.memory-chunks=10000
```

4. Setting up Node Exporter
In this section, we will install the Prometheus Node Exporter. The Node Exporter is a server that exposes Prometheus metrics about the host machine (node) it is running on. This includes metrics about the machine's filesystems, networking devices, processor usage, memory usage, and more.

wget https://github.com/prometheus/node_exporter/releases/download/v0.15.2/node_exporter-0.15.2.darwin-amd64.tar.gz


5. Setting grafana

docker run -d -p 3000:3000 -e "GF_SECURITY_ADMIN_PASSWORD=password" -v ~/grafana_db:/var/lib/grafana grafana/grafana

docker ps -aq --no-trunc | xargs docker rm

####References:

https://www.digitalocean.com/community/tutorials/how-to-install-prometheus-using-docker-on-ubuntu-14-04
https://g00glen00b.be/monitoring-spring-prometheus-grafana/
https://prometheus.io/docs/introduction/first_steps/#installing-the-node-exporter

