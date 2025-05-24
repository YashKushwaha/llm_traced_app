import time
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def run_llm_pipeline(prompt: str) -> str:
    with tracer.start_as_current_span("generate_embedding"):
        time.sleep(0.2)  # simulate delay

    with tracer.start_as_current_span("query_vector_store"):
        time.sleep(0.1)

    with tracer.start_as_current_span("generate_response") as span:
        time.sleep(0.3)
        span.set_attribute("llm_model", "gpt-4")
        return f"Simulated response to: '{prompt}'"
