from fastapi import FastAPI
import redis
from datetime import datetime
import os

app = FastAPI()

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
    cache.setex(cache_key, 10, current_time)  # Cache 10 segundos
    return {"time": current_time}
