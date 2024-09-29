#!/usr/bin/python3

""" This module contains the test cases for the Branch model """

from app.models.branch import Branch
from app.models.service import Service
from app.models.booking import Booking
from app import create_app, db
import unittest
import datetime


class TestBranchModel(unittest.TestCase):
    """Testing the Branch model"""

    def setUp(self):
        """Setup for the test cases"""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create an in-memory SQLite database for testing
        db.create_all()

    def tearDown(self):
        """Teardown for the test cases"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create(self):
        """Test the creation of the Branch model"""

        branch = Branch(
            name="Nairobi Branch",
            location="150 Nyumba Moja road",
            contacts="0720268453",
            email="nairobi@example.com"
        )
        db.session.add(branch)
        db.session.commit()

        self.assertEqual(branch.name, "Nairobi Branch")
        self.assertEqual(branch.location, "150 Nyumba Moja road")
        self.assertEqual(branch.contacts, "0720268453")
        self.assertEqual(branch.email, "nairobi@example.com")

    def test_update(self):
        """Test the update of the Branch model"""
        branch = Branch(
            name="Nairobi Branch",
            location="150 Nyumba Moja road",
            contacts="0720268453",
            email="nairobi@example.com"
        )
        db.session.add(branch)
        db.session.commit()

        # Update the branch information
        branch.name = "Mombasa Branch"
        branch.location = "200 Kilifi Road"
        db.session.commit()

        self.assertEqual(branch.name, "Mombasa Branch")
        self.assertEqual(branch.location, "200 Kilifi Road")

    def test_delete(self):
        """Test the deletion of the Branch model"""
        branch = Branch(
            name="Nairobi Branch",
            location="150 Nyumba Moja road",
            contacts="0720268453",
            email="nairobi@example.com"
        )
        db.session.add(branch)
        db.session.commit()

        db.session.delete(branch)
        db.session.commit()

        self.assertEqual(db.session.query(Branch).count(), 0)

    def test_service_relationship(self):
        """Test the relationship between Branch and Service"""
        branch = Branch(
            name="Nairobi Branch",
            location="150 Nyumba Moja road",
            contacts="0720268453",
            email="nairobi@example.com"
        )
        db.session.add(branch)
        db.session.commit()

        service = Service(
            name="Consultation",
            description="General Consultation",
            branch_id=branch.id
        )
        db.session.add(service)
        db.session.commit()

        self.assertEqual(len(branch.services), 1)
        self.assertEqual(branch.services[0].name, "Consultation")

    def test_booking_relationship(self):
        """Test the relationship between Branch and Booking"""
        branch = Branch(
            name="Nairobi Branch",
            location="150 Nyumba Moja road",
            contacts="0720268453",
            email="nairobi@example.com"
        )
        db.session.add(branch)
        db.session.commit()

        # Create a service for the booking
        service = Service(
            name="Consultation",
            description="General Consultation",
            branch_id=branch.id
        )
        db.session.add(service)
        db.session.commit()

        # Now create a booking linked to both branch and service
        booking = Booking(
            patient_name='John Doe',
            patient_age=30,
            patient_gender='Male',
            patient_details='test',
            appointment_time=datetime.datetime.now(),
            service_id=service.id,  # Link booking to the service
            branch_id=branch.id
        )
        db.session.add(booking)
        db.session.commit()

        self.assertEqual(len(branch.bookings), 1)
        self.assertEqual(branch.bookings[0].patient_name, 'John Doe')


if __name__ == '__main__':
    unittest.main()
