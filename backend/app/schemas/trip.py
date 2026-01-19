from datetime import date
from typing import Optional

from pydantic import BaseModel

class TripBase(BaseModel):
    name: str
    destination: str
    start_date: date
    end_date: date
    budget: Optional[float] = None

class TripCreate(TripBase):
    pass

class TripUpdate(BaseModel):
    name: Optional[str] = None
    destionation: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[float] = None

class TripResponse(TripBase):
    id: int

    class Config:
        from_attributes = True