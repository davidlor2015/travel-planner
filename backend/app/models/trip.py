from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    name = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    budget = Column(Float, nullable=True)

    # existing relationship
    user = relationship("User", back_populates="trips")

   
    items = relationship(
        "ItineraryItem",
        back_populates="trip",
        cascade="all, delete-orphan"
    )
