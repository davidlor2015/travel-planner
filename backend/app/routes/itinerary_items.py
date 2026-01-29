from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.auth import get_current_user
from app.core.deps import get_db
from app.models.trip import Trip
from app.models.itinerary_item import ItineraryItem
from app.models.user import User
from app.schemas.itinerary_item import (
    ItineraryItemCreate,
    ItineraryItemResponse,
)

router = APIRouter(
    prefix="/trips/{trip_id}/items",
    tags=["Itinerary Items"],
)

@router.post(
    "/",
    response_model=ItineraryItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_item(
    trip_id: int,
    item_in: ItineraryItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    trip = (
        db.query(Trip)
        .filter(
            Trip.id == trip_id,
            Trip.user_id == current_user.id,
        )
        .first()
    )

    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    item = ItineraryItem(
        trip_id=trip.id,
        type=item_in.type,
        title=item_in.title,
        description=item_in.description,
        start_time=item_in.start_time,
        end_time=item_in.end_time,
        cost=item_in.cost,
        origin=item_in.origin,
        destination=item_in.destination,
        airline=item_in.airline,
        flight_number=item_in.flight_number,
        cabin_class=item_in.cabin_class,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item

@router.get("/", response_model=List[ItineraryItemResponse])
def list_items(
    trip_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    trip = (
        db.query(Trip)
        .filter(
            Trip.id == trip_id,
            Trip.user_id == current_user.id,
        )
        .first()
    )

    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    items = (
        db.query(ItineraryItem)
        .filter(ItineraryItem.trip_id == trip.id)
        .order_by(ItineraryItem.start_time)
        .all()
    )

    return items
