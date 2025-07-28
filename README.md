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

## 🚨 Testing Prometheus Alerts

6. **Trigger the Alert**: The system has a configured alert that fires when request rate > 1 req/min for 1 minute.
   
   To trigger it, rapidly visit the app multiple times:
   ```bash
   # Method 1: Use curl in a loop
   for i in {1..80}; do curl http://localhost:5000/ && sleep 0.2; done
   
   # Method 2: Use browser - quickly refresh http://localhost:5000/ 70+ times
   ```

7. **Monitor the Alert**:
   - Go to Prometheus UI: http://localhost:9090/alerts
   - Watch for `HighRequestRate` alert to change from **Inactive** → **Pending** → **Firing**
   - The alert should fire after maintaining >1 req/min for 1 minute

8. **View Alert in Grafana** (Optional):
   - In Grafana, you can also configure alerting to receive notifications
   - Or create a panel to visualize alert states

9. After all tests, stop all services: `docker-compose down`



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