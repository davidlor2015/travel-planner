from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)

    type = Column(String(20), nullable=False)

    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)

    cost = Column(Float, nullable=True)

    origin = Column(String(10), nullable=True)
    destination = Column(String(10), nullable=True)
    airline = Column(String(10), nullable=True)
    flightnumber = Column(String(10), nullable=True)
    cabin_class = Column(String(20), nullable=True)

    last_checked_price = Column(Float, nullable=True)
    last_checked_at = Column(DateTime, nullable=True)

    trip = relationship("Trip", back_populates="items")
