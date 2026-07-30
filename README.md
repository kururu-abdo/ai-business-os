# AI Business OS (ai-business-os)

Production-ready backend architecture template utilizing modern asynchronous layers.

## Prerequisite
* Docker Engine 23.0+
* Docker Compose v2.0+

## Local Initialization

```bash
# Clone repository configuration files
cp backend/.env.example backend/.env

# Build and execute cluster instance topology
docker compose up --build
```

## System Interfaces
* Swagger Engine UI: `http://localhost:8000/docs`
* Production Health Matrix Metrics: `http://localhost:8000/health`

## Structural DB Evolutions
```bash
# To generate a new migration footprint locally
docker compose exec backend alembic revision --autogenerate -m "migration_description"
```
