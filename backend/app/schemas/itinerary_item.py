from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, field_validator

class IteneraryItemBase(BaseModel):
    type: Literal["flight", "hotel", "poi"]

    title: str
    description: Optional[str] = None

    start_time: datetime
    end_time: Optional[datetime] = None

    cost:Optional[float] = None

class FlightFields(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    airline: Optional[str] = None
    flight_number: Optional[str] = None
    cabin_class: Optional[str] = None

class ItineraryItemCreate(IteneraryItemBase, FlightFields):
    pass

class ItineraryItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    cost: Optional[float] = None
    origin: Optional[str] = None
    destination: Optional[str] = None
    airline: Optional[str] = None
    flight_number: Optional[str] = None
    cabin_class: Optional[str] = None

class ItineraryItemResponse(IteneraryItemBase, FlightFields):
    id: int
    trip_id: int
    
    last_checked_price: Optional[float] = None
    last_checked_at: Optional[datetime] = None

    class Config:
        from_attributes = True

    