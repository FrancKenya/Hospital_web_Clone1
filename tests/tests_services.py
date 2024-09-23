#!/usr/bin/python3

""" This module contains the test cases for the service model """

from app.models.basemodel import BaseModel
from app.models.booking import Booking
from app.models.service import Service
from app.models.branch import Branch
from app import create_app
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest


class TestServiceModel(unittest.TestCase):
    """Testing the service model"""

    def setUp(self):
        """Setup for the test cases"""
        self.app = create_app()
        self.engine = create_engine('sqlite:///:memory:')
        BaseModel.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        """Teardown for the test cases"""
        self.session.close()
        BaseModel.metadata.drop_all(self.engine)

    def test_create(self):
        """"Test the creation of the service model"""

        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()

        service = Service(
            name="Consultation", description="General Consultation", branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        self.assertEqual(service.name, "Consultation")
        self.assertEqual(service.description, "General Consultation")
        self.assertEqual(service.branch_id, branch.id)

    def test_update(self):
        """Test the update of the service"""
        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()
        service = Service(
            name='Consultation', description='General Consultation', branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        service.description = "Updating the description"
        self.session.commit()
        self.assertEqual(service.description, "Updating the description")

    def test_delete(self):
        """Test the deletion of the service"""
        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()
        service = Service(
            name='Consultation', description='General Consultation', branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        self.session.delete(service)
        self.session.commit()
        self.assertEqual(self.session.query(Service).count(), 0)

    def test_booking_relationship(self):
        """Test the relationship between service and booking"""
        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()
        service = Service(
            name='Consultation', description='General Consultation', branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        booking = Booking(
            patient_name='John Doe', patient_details='test', service=service)
        self.session.add(booking)
        self.session.commit()
        self.assertEqual(len(service.bookings), 1)
        self.assertEqual(service.bookings[0].patient_name, 'John Doe')
        self.assertIn(booking, service.bookings)


if __name__ == '__main__':
    unittest.main()
