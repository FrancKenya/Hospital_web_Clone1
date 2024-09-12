#!/usr/bin/python3

""" This module contains booking class for the hospital clone"""

from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Booking(BaseModel):
    """ The Booking made by client """
    __tablename__ = 'bookings'
    patient_name = Column(String(120), nullable=False)
    patient_details = Column(Text, nullable=False)
    service_id = Column(String(60), ForeignKey('services.id'), nullable=False)
    service = relationship("Service", back_populates="bookings")

    def __init__(self, *args, **kwargs):
        """Initialization of booking class"""
        super().__init__(*args, **kwargs)
