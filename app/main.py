from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Define a custom metric
REQUEST_COUNT = Counter('hello_world_requests_total', 'Total hello world requests')

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    return "Hello, Prometheus!"

if __name__ == "__main__":
    # Expose metrics at :8000/metrics
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)