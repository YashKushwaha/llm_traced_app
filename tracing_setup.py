import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExporter, SpanExportResult
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Custom file exporter
class FileSpanExporter(SpanExporter):
    def __init__(self, filename: str):
        self.logger = logging.getLogger("otel_traces")
        self.logger.setLevel(logging.INFO)

        # Avoid adding duplicate handlers
        if not any(isinstance(h, logging.FileHandler) and h.baseFilename == filename
                   for h in self.logger.handlers):
            handler = logging.FileHandler(filename)
            handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
            self.logger.addHandler(handler)

    def export(self, spans):
        for span in spans:
            self.logger.info(f"[{span.name}] start={span.start_time}, end={span.end_time}, attrs={span.attributes}")
        return SpanExportResult.SUCCESS

    def shutdown(self):
        return

_tracer_initialized = False

def setup_tracer(app):
    global _tracer_initialized
    if _tracer_initialized:
        return  # Prevent multiple setup calls

    trace.set_tracer_provider(TracerProvider())
    tracer_provider = trace.get_tracer_provider()

    file_exporter = FileSpanExporter("traces.log")
    span_processor = SimpleSpanProcessor(file_exporter)
    tracer_provider.add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(app)

    _tracer_initialized = True