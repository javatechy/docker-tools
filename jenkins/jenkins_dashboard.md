# Steps to build a jenkins dashboard

### Update prometheus.yml file 

```
# A scrape configuration scraping a Node Exporter and the Prometheus server
# itself.
scrape_configs:
  # Scrape the Jenkins exporter every 5 seconds.
  - job_name: 'jenkins_exporter'
    scrape_interval: 5s
    metrics_path: '/metrics'
    static_configs:
      - targets: ['jenkins_exporter:9118']
```
 
### Change your settings acordingly

```
docker-compose -f dashboard_docker_compose.yml up
```
 