# Steps to build a jenkins dashboard

### Prerequisite

1. Python installed
2. Pip Installed
3. Docker is installed on the system.

### Clone the project

Clone the project using 
 
 
```
git clone https://github.com/lovoo/jenkins_exporter.git
git clone git@github.com:lovoo/jenkins_exporter.git
cd jenkins_exporter
pip install -r requirements.txt
```

Start your node exporter on your local system using

```
cd jenkins_exporter
python jenkins_exporter.py -j http://localhost:8080/  --user admin --password admin 
```

Ref: https://github.com/lovoo/jenkins_exporter


# Install prometheus

1.  Create a prometheus configuration file inside a directory in your system your

```
# A scrape configuration scraping a Node Exporter and the Prometheus server
# itself.
scrape_configs:
  # Scrape the Jenkins exporter every 5 seconds.
  - job_name: 'jenkins_exporter'
    scrape_interval: 2s
    metrics_path: '/'
    static_configs:
      - targets: ['be194503.ngrok.io']
```

2.  Install prometheus on your docker using the following command.

```
docker run -d -p 9090:9090 --link jenkins_exporter:jenkins_exporter  prom/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus  
```

this will start prometheus on port 9090.


3. Grafana installation steps 

```
docker run -d -p 3000:3000 -e "GF_SECURITY_ADMIN_PASSWORD=password" -v ~/grafana_db:/var/lib/grafana grafana/grafana
```

4. Linking Prometheus and grafana.

Add the Prometheus data source in grafana.

