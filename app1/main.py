from fastapi import FastAPI
import redis
from datetime import datetime
import os

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor

# OpenTelemetry setup
resource = Resource(attributes={"service.name": "app1-fastapi"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://tempo:4318/v1/traces"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

RedisInstrumentor().instrument()

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

redis_host = os.getenv('REDIS_HOST', 'redis')
cache = redis.Redis(host=redis_host, port=6379)

@app.get("/ping")
def ping():
    return {"message": "App 1 - OK"}

@app.get("/time")
def get_time():
    cache_key = "app1_time"
    cached = cache.get(cache_key)
    if cached:
        return {"time": cached.decode('utf-8')}
    
    current_time = datetime.utcnow().isoformat()
    cache.setex(cache_key, 10, current_time)
    return {"time": current_time}
