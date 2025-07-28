# Prometheus and Grafana Mini Project


## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (if not included in Docker)


## How to Run

1. Clone the repo
2. Run `docker-compose up --build`
3. Access:
	- Python App: http://localhost:5000/
(Visit this in your browser several times to generate requests.)
	- Prometheus UI: http://localhost:9090/
	- Grafana: http://localhost:3000/
Default login: admin / admin (set a new password when prompted)


4. In Grafana, add Prometheus as a data source (http://prometheus:9090)
5. Create a dashboard and visualize `hello_world_requests_total`
6. After all tests, stop all services: `docker-compose down`



## 🖼️ Architecture Diagram
     +-------------------------+
     |    Python Flask App     |
     |  (http://app:8000/)    |
     |   Exposes /metrics     |
     +-----------+-------------+
                 |
       Scrape via HTTP
                 |
     +-----------v-------------+
     |      Prometheus         |
     |   (http://prometheus:9090/) |
     +-----------+-------------+
                 |
       Data Source for Grafana
                 |
     +-----------v-------------+
     |        Grafana          |
     |   (http://localhost:3000/)  |
     +-------------------------+