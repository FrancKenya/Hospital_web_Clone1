#!/usr/bin/python3

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db

class BaseModel(db.Model):
    __abstract__ = True  # Don't create a table for this class

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        """Save the current instance to the database"""
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the current instance from the database"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Return a string representation of the instance"""
        return f"<{self.__class__.__name__}(id={self.id})>"

    def to_dict(self):
        """Convert instance into dict format"""
        model_dict = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
