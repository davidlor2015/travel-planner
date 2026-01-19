from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.auth import get_current_user
from app.core.deps import get_db
from app.models.trip import Trip
from app.models.user import User
from app.schemas.trip import TripCreate, TripResponse

router = APIRouter(
    prefix="/trips",
    tags=["Trips"]
)

@router.post("/", response_model=TripResponse, status_code=status.HTTP_201_CREATED)
def create_trip(
    trip_in: TripCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    trip = Trip(
        user_id=current_user.id,
        name=trip_in.name,
        destination=trip_in.destination,
        start_date=trip_in.start_date,
        end_date=trip_in.end_date,
        budget=trip_in.budget,
    )

    db.add(trip)
    db.commit()
    db.refresh(trip)

    return trip

@router.get("/", response_model=List[TripResponse])
def list_trips(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    trips = (
        db.query(Trip)
        .filter(Trip.user_id == current_user.id)
        .order_by(Trip.start_date)
        .all()
    )

    return trips