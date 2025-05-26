# 📊 Observability with OpenTelemetry

This project demonstrates how to integrate **OpenTelemetry** with a Python-based **FastAPI** application to enable observability and tracing for calls to a simulated Large Language Model (LLM).

It uses the [OpenTelemetry Python SDK](https://opentelemetry.io/docs/languages/python/) to generate traces and logs, which are exported to [Jaeger](https://www.jaegertracing.io/) for visualization. Jaeger is containerized and run via Docker Compose.

---

## 🚀 Project Overview

- ✅ FastAPI application that mimics an LLM service  
- ✅ OpenTelemetry instrumentation for automatic and custom traces  
- ✅ Exporting traces to Jaeger UI for distributed tracing visualization  
- ✅ Dockerized Jaeger instance using `docker-compose`  
- ✅ Dependency and environment management with Poetry  

---

## 🗂️ Project Structure

```
yashkushwaha-llm_traced_app/
├── README.md                # Project documentation
├── app.py                   # Main FastAPI application
├── llm_chain.py             # Simulated LLM logic
├── tracing_setup.py         # OpenTelemetry tracing setup
├── pyproject.toml           # Poetry configuration file
├── poetry.lock              # Locked dependency versions
├── requirements.txt         # Optional: pip-based dependencies
└── docker/
    └── docker-compose.yml   # Docker Compose config for Jaeger
```

---

## 📦 Setup (with Poetry)

This project uses [Poetry](https://python-poetry.org/) for dependency and environment management.

### 📥 Install Dependencies

1. **Install Poetry** (if not already installed):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install project dependencies:**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```

---

## ▶️ Running the FastAPI App

Once inside the Poetry shell, start the FastAPI app:

```bash
uvicorn app:app --reload
```

Visit `http://localhost:8000` to interact with the API. Each endpoint call is traced via OpenTelemetry and sent to Jaeger.

---

## 🐳 Running Jaeger with Docker

Use Docker Compose to spin up the Jaeger UI:

```bash
cd docker
docker-compose up -d
```

The Jaeger interface should now be accessible at:  
➡️ **http://localhost:16686**

---

## 🔍 Observing Traces

1. Call the FastAPI endpoint (e.g., via browser or curl).
2. Open the **Jaeger UI** at `http://localhost:16686`
3. Search for the service name defined in `tracing_setup.py`
4. Explore trace data and span timelines.

---

## 📚 References

- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
- [Jaeger Tracing](https://www.jaegertracing.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [FastAPI](https://fastapi.tiangolo.com/)

---
