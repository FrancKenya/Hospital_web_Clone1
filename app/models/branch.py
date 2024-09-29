#!/usr/bin/python3

""" This module contains the branch model  for the branch page"""

from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app import db


class Branch(BaseModel):
    """ This class represents the branches of the hospital """
    __tablename__ = "branches"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    contacts = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    services = db.relationship(
        "Service", back_populates="branch")
    bookings = db.relationship(
        "Booking", back_populates="branch")
