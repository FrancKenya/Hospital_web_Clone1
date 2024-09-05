#!/usr/bin/python3

""" This module contains the base model """

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
import uuid

Base = declarative_base()


class BaseModel(Base):
    """ This class defines all common attributes/methods for other classes """

    __abstract__ = True  # Not to create a table for base class

    id = Column(String(60), primary_key=True, default=lambda: str(
        uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, *args, **kwargs):
        """Initialization of base model"""
        super().__init__(*args, **kwargs)
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', self.created_at)

    def save(self, session):
        """ Save class instance to database """
        self.updated_at = datetime.now()
        session.add(self)
        session.commit()

    def delete(self, session):
        """Delete class instance from database"""
        session.delete(self)
        session.commit()

    def __repr__(self):
        """Return a string representation of the instance"""
        return f"<{self.__class__.__name__}(id={self.id})>"

    def to_dict(self):
        """Convert instance into dict format"""
        model_dict = {i.name: getattr(
            self, i.name) for i in self.__table__.columns}
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
