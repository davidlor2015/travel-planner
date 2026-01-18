from fastapi import FastAPI

app = FastAPI(title="Travel Planner API")

@app.get("/")
def health_check():
    return {"status": "ok"}
