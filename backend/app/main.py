from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from app.core.init_db import init_db
from app.models.user import User
from app.routes import auth, trips, itinerary_items
from app.core.auth import get_current_user
from fastapi.openapi.models import SecurityScheme
from fastapi.openapi.utils import get_openapi
from app.core.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Travel Planner API",
    security=[{"HTTPBearer": []}]
)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(trips.router)
app.include_router(itinerary_items.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Travel Planner API",
        version="0.1.0",
        description="JWT-protected API",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    openapi_schema["security"] = [{"HTTPBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }