#!/usr/bin/python3

""" This module contains the branch model  for the branch page"""

from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

class Branch(BaseModel):
    """ This class represents the branches of the hospital """
    __tablename__ = "branches"
    name  = Column(String(120), nullable=False)
    location = Column(Text, nullable=False)
    contacts = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    services = relationship(
        "Service", back_populates="branch", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """Initialization of branch class"""
        super().__init__(*args, **kwargs)