from fastapi import FastAPI
from tracing_setup import setup_tracer
from llm_chain import run_llm_pipeline
from opentelemetry import trace

from pathlib import Path

app = FastAPI()
setup_tracer(app)
tracer = trace.get_tracer(__name__)

@app.get("/chat")
def chat(prompt: str):
    with tracer.start_as_current_span("llm_chain"):
        response = run_llm_pipeline(prompt)
        return {"response": response}

@app.get("/")
def chat():
    return {"response": "Hi"}

if __name__ == "__main__":
    import uvicorn
    app_path = Path(__file__).resolve().with_suffix('').name  # gets filename without .py
    uvicorn.run(f"{app_path}:app", host="0.0.0.0", port=7000, reload=True)