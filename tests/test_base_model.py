#!/usr/bin/python3

""" This module contains the test cases for the BaseModel class"""

from datetime import datetime
from app import db, create_app
from app.models.basemodel import BaseModel
from sqlalchemy import Column, String
import unittest
import uuid


class TestModel(BaseModel):
    """ Used to create an SQL table for the test cases"""
    __tablename__ = 'test_model'
    name = db.Column(String(128), nullable=False)


class TestBaseModel(unittest.TestCase):
    """This class contains the test cases for the BaseModel class"""

    def setUp(self):
        """Setup for the test cases"""
        # Create a test app and set up the database in memory
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Teardown for the test cases"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_save(self):
        """Test the save method of the BaseModel class"""
        test_model = TestModel(name="test")
        test_model.save()
        self.assertIn(test_model, db.session)
        old_updated_at = test_model.updated_at
        test_model.save()
        self.assertGreater(test_model.updated_at, old_updated_at)

    def test_delete(self):
        """Test the delete method of the BaseModel class"""
        test_model = TestModel(name="test")
        test_model.save()
        test_model.delete()
        self.assertNotIn(test_model, db.session)

    def test_repr(self):
        """Test the __repr__ method of the BaseModel class"""
        bm = BaseModel()
        result = f"<BaseModel(id={bm.id})>"
        self.assertEqual(repr(bm), result)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        test_model = TestModel(name="test")

        # Save the instance to ensure created_at and updated_at are set
        test_model.save()

        result = test_model.to_dict()
        self.assertEqual(result['id'], test_model.id)
        self.assertEqual(
            result['created_at'], test_model.created_at.isoformat())
        self.assertEqual(
            result['updated_at'], test_model.updated_at.isoformat())

        test_model.extra_attr = "extra"
        self.assertNotIn("extra_attr", result)


if __name__ == '__main__':
    unittest.main()
