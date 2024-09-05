#!/usr/bin/python3

""" This module contains the test cases for the BaseModel class"""


from datetime import datetime
from app.models.basemodel import BaseModel, Base
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
import unittest
import uuid


class TestModel(BaseModel):
    """ Used to create an sqltable for the test cases"""
    __tablename__ = 'test_model'
    name = Column(String(128), nullable=False)


class TestBaseModel(unittest.TestCase):
    """This class contains the test cases for the BaseModel class"""

    def setUp(self):
        """Setup for the test cases"""
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def tearDown(self):
        """Teardown for the test cases"""
        self.session.close()
        Base.metadata.drop_all(self.session.bind)

    def test_init(self):
        """Test the initialization of the BaseModel class"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertEqual(bm.created_at, bm.updated_at)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

        id = str(uuid.uuid4())
        created_at = datetime(2024, 8, 29, 2, 9, 0)
        bm_kwargs = BaseModel(id=id, created_at=created_at)
        self.assertEqual(bm_kwargs.id, id)
        self.assertEqual(bm_kwargs.created_at, created_at)
        self.assertEqual(bm_kwargs.updated_at, created_at)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        test_model = TestModel(name="test")
        test_model.save(self.session)
        self.assertIn(test_model, self.session)
        old_updated_at = test_model.updated_at
        test_model.save(self.session)
        self.assertGreater(test_model.updated_at, old_updated_at)

    def test_delete(self):
        """Test the delete method of the BaseModel class"""
        test_model = TestModel(name="test")
        test_model.save(self.session)
        test_model.delete(self.session)
        self.assertNotIn(test_model, self.session)

    def test_repr(self):
        """Test the __repr__ method of the BaseModel class"""
        bm = BaseModel()
        result = f"<BaseModel(id={bm.id})>"
        self.assertEqual(repr(bm), result)

    def test_to_dict(self):
        """Test the to_dict of the BaseModel class"""
        test_model = TestModel(name="test")
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
