from fastapi import FastAPI
from app.core.init_db import init_db
import app.models

app = FastAPI(title="Travel Planner API")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def health_check():
    return {"status": "ok"}
