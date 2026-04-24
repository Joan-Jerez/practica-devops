from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "demo_app_requests_total",
    "Total de requests recibidas por la app demo",
    ["method", "endpoint", "http_status"],
)
REQUEST_LATENCY = Histogram(
    "demo_app_request_duration_seconds",
    "Latencia de requests de la app demo",
    ["endpoint"],
)


@app.route("/")
def home():
    start = time.time()
    simulated_delay = random.uniform(0.01, 0.2)
    time.sleep(simulated_delay)
    REQUEST_COUNT.labels("GET", "/", "200").inc()
    REQUEST_LATENCY.labels("/").observe(time.time() - start)
    return {
        "message": "Demo app con metricas para Prometheus",
        "delay_seconds": round(simulated_delay, 4),
    }


@app.route("/health")
def health():
    REQUEST_COUNT.labels("GET", "/health", "200").inc()
    return {"status": "ok"}


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
