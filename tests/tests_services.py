#!/usr/bin/python3

""" This module contains the test cases for the service model """

from app.models.basemodel import BaseModel
from app.models.booking import Booking
from app.models.service import Service
from app.models.branch import Branch
from app import create_app, db
import datetime
import unittest


class TestServiceModel(unittest.TestCase):
    """Testing the service model"""

    def setUp(self):
        """Setup for the test cases"""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create all tables in the actual database (in-memory SQLite)
        db.create_all()

    def tearDown(self):
        """Teardown for the test cases"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create(self):
        """"Test the creation of the service model"""

        branch = Branch(
            name="Main", location="150 Nyumba Moja road",
            contacts="0720268453", email="branch@example.com")
        db.session.add(branch)
        db.session.commit()

        service = Service(
            name="Consultation", description="General Consultation",
            branch_id=branch.id)
        db.session.add(service)
        db.session.commit()
        self.assertEqual(service.name, "Consultation")
        self.assertEqual(service.description, "General Consultation")
        self.assertEqual(service.branch_id, branch.id)

    def test_update(self):
        """Test the update of the service"""
        branch = Branch(
            name="Main", location="150 Nyumba Moja road",
            contacts="0720268453", email="branch@example.com")
        db.session.add(branch)
        db.session.commit()
        service = Service(
            name='Consultation', description='General Consultation',
            branch_id=branch.id)
        db.session.add(service)
        db.session.commit()
        service.description = "Updating the description"
        db.session.commit()
        self.assertEqual(service.description, "Updating the description")

    def test_delete(self):
        """Test the deletion of the service"""
        branch = Branch(
            name="Main", location="150 Nyumba Moja road",
            contacts="0720268453", email="branch@example.com")
        db.session.add(branch)
        db.session.commit()
        service = Service(
            name='Consultation', description='General Consultation',
            branch_id=branch.id)
        db.session.add(service)
        db.session.commit()
        db.session.delete(service)
        db.session.commit()
        self.assertEqual(Service.query.count(), 0)

    def test_booking_relationship(self):
        """Test the relationship between service and booking"""
        branch = Branch(name="Main", location="150 Nyumba Moja road",
                        contacts="0720268453", email="branch@example.com")
        db.session.add(branch)
        db.session.commit()
        service = Service(
            name='Consultation', description='General Consultation',
            branch_id=branch.id)
        db.session.add(service)
        db.session.commit()

        # Provide all required fields
        booking = Booking(
            patient_name='Francis Waihiga',
            patient_age=30,  # Ensure the patient_age is provided
            patient_gender='Male',  # Ensure the patient_gender is provided
            patient_details='test',
            appointment_time=datetime.datetime.now(),
            service_id=service.id,
            branch_id=branch.id
        )

        db.session.add(booking)
        db.session.commit()

        self.assertEqual(len(service.bookings), 1)
        self.assertEqual(service.bookings[0].patient_name, 'Francis Waihiga')
        self.assertIn(booking, service.bookings)


if __name__ == '__main__':
    unittest.main()
