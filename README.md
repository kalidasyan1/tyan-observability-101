# Prometheus Mini Project

## How to Run

1. Clone the repo
2. Run `docker-compose up --build`
3. Access:
   - App: http://localhost:5000
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000

4. In Grafana, add Prometheus as a data source (http://prometheus:9090)
5. Create a dashboard and visualize `hello_world_requests_total`