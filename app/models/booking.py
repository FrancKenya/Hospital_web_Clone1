#!/usr/bin/python3

""" This module contains booking class for the hospital clone"""

from app.models.basemodel import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.models.service import Service
from app.models.branch import Branch
from app import db


class Booking(BaseModel):
    """ The Booking made by client """
    __tablename__ = 'bookings'
    patient_name = db.Column(db.String(120), nullable=False)
    patient_age = db.Column(db.Integer, nullable=False)
    patient_gender = db.Column(db.String(10), nullable=False)
    patient_details = db.Column(db.Text, nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey(
        'services.id', name='fk_bookings_service_id'), nullable=False)
    services = db.relationship("Service", back_populates="bookings")
    branch_id = db.Column(
        db.Integer, db.ForeignKey(
            'branches.id', name='fk_bookings_branch_id'), nullable=False)
    branch = db.relationship("Branch", back_populates="bookings")

    def __init__(self, *args, **kwargs):
        """Initialization of booking class"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Convert instance into dict format for frontend purposes"""
        return {
            'id': self.id,
            'patient_name': self.patient_name,
            'patient_age': self.patient_age,
            'patient_gender': self.patient_gender,
            'patient_details': self.patient_details,
            'appointment_time': self.appointment_time.isoformat(),
            'service_id': self.service_id,
            'branch_id': self.branch_id
        }
