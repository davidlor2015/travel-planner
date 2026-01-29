# Travel Planner

A full-stack travel planning web application built with **FastAPI** and **Angular**, featuring **JWT authentication**, protected APIs, and CRUD functionality for managing trips and itinerary items.

This project demonstrates backend/frontend integration, secure authentication, and relational data modeling in a web stack.

---

##  Features

-  **JWT Authentication**
  - Secure login and registration
  - Protected API routes
  - Frontend route guards

-  **Trips Management**
  - Create, view, and delete trips
  - Trips scoped to authenticated users

-  **Itinerary Items**
  - Relational data modeling 
  - Designed for flights, hotels, and points of interest

-  **Frontend**
  - Angular 
  - Service-based API layer
  - JWT interceptor for authenticated requests

- **Backend**
  - FastAPI + SQLAlchemy
  - OAuth2-compatible login flow
  - CORS-enabled for SPA integration

---

## Tech Stack

### Backend
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **JWT / OAuth2**
- **SQLite / MySQL** 

### Frontend
- **Angular **
- **TypeScript**
- **SCSS**
- **HttpClient + Interceptors**

### Tooling
- Git & GitHub
- REST APIs


##  Authentication Flow

1. User logs in via Angular frontend
2. Credentials are sent using OAuth2-compatible form encoding
3. FastAPI issues a JWT access token
4. Token is stored client-side
5. Angular HTTP interceptor automatically attaches the JWT
6. Protected backend routes validate the token

---
 
### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

