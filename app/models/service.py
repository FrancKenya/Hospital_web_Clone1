#!/usr/bin/python3

""" Contains the service model for the service page"""

from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app import db


class Service(BaseModel):
    """ This class represents the services offered by the hospital """

    __tablename__ = "services"
    name = db.Column(db.String(120), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    branch_id = db.Column(db.ForeignKey('branches.id', name='fk_services_branch_id'), nullable=False)
    bookings = db.relationship("Booking", back_populates="services")
    branch = db.relationship("Branch", back_populates="services")
