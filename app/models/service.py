#!/usr/bin/python3

""" Contains the service model for the service page"""

from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Service(BaseModel):
    """ This class represents the services offered by the hospital """

    __tablename__ = "services"
    name = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    #branch_id = Column(String(60), ForeignKey('branches.id'), nullable=False)
    bookings = relationship("Booking", back_populates="service")
    #branch = relationship("Branch", back_populates="service")

    def __init__(self, *args, **kwargs):
        """Initialization of service class"""
        super().__init__(*args, **kwargs)
