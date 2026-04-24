# Lab: Monitoreo con Prometheus y Grafana

Esta practica implementa monitoreo de **aplicacion** y **sistema** usando Docker Compose.

## Servicios incluidos

- `app`: Aplicacion Flask demo con metricas Prometheus (`/metrics`)
- `prometheus`: Recolecta metricas de todos los targets
- `grafana`: Visualizacion y dashboard preconfigurado
- `node-exporter`: Metricas del host/sistema
- `cadvisor`: Metricas de contenedores

## Estructura

- `docker-compose.yml`
- `app/`
- `prometheus/prometheus.yml`
- `grafana/provisioning/`
- `grafana/dashboards/lab-overview.json`

## Levantar la practica

```bash
docker compose up -d --build
```

## URLs

- App demo: http://localhost:5000/
- Prometheus: http://localhost:9090/
- Grafana: http://localhost:3000/

Credenciales Grafana por defecto:

- Usuario: `admin`
- Password: `admin`

## Verificacion rapida

1. Generar trafico en la app:

```bash
for i in {1..50}; do curl -s http://localhost:5000/ > /dev/null; done
```

2. En Prometheus, probar query:

```promql
sum(rate(demo_app_requests_total[1m]))
```

3. En Grafana, abrir dashboard `Lab Monitoring Overview`.

## Nota para Windows

Si usas Docker Desktop en Windows, es recomendable tener backend WSL2 habilitado para que `node-exporter` y `cadvisor` puedan exponer metricas del host correctamente.
