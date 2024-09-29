#!/usr/bin/python3

""" This module contains the test cases for the Booking model """

from app.models.service import Service
from app.models.branch import Branch
from app.models.booking import Booking
from app import create_app, db
import unittest
import datetime


class TestBookingModel(unittest.TestCase):
    """Testing the Booking model"""

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

    def test_create_booking(self):
        """Test the creation of a booking"""
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

        booking = Booking(
            patient_name='John Doe',
            patient_age=30,
            patient_gender='Male',
            patient_details='Regular check-up',
            appointment_time=datetime.datetime.now(),
            service_id=service.id,
            branch_id=branch.id
        )
        db.session.add(booking)
        db.session.commit()

        # Assertions to check if the booking is created correctly
        self.assertEqual(booking.patient_name, 'John Doe')
        self.assertEqual(booking.patient_age, 30)
        self.assertEqual(booking.patient_gender, 'Male')
        self.assertEqual(booking.patient_details, 'Regular check-up')
        self.assertEqual(booking.service_id, service.id)
        self.assertEqual(booking.branch_id, branch.id)

    def test_update_booking(self):
        """Test updating a booking"""
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

        booking = Booking(
            patient_name='Jane Doe',
            patient_age=28,
            patient_gender='Female',
            patient_details='Consultation',
            appointment_time=datetime.datetime.now(),
            service_id=service.id,
            branch_id=branch.id
        )
        db.session.add(booking)
        db.session.commit()

        # Update booking details
        booking.patient_name = 'Jane Smith'
        booking.patient_age = 29
        booking.patient_details = 'Updated consultation'
        db.session.commit()

        # Assertions to check if the booking is updated correctly
        self.assertEqual(booking.patient_name, 'Jane Smith')
        self.assertEqual(booking.patient_age, 29)
        self.assertEqual(booking.patient_details, 'Updated consultation')

    def test_delete_booking(self):
        """Test deleting a booking"""
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

        booking = Booking(
            patient_name='John Doe',
            patient_age=30,
            patient_gender='Male',
            patient_details='Consultation',
            appointment_time=datetime.datetime.now(),
            service_id=service.id,
            branch_id=branch.id
        )
        db.session.add(booking)
        db.session.commit()

        # Delete the booking
        db.session.delete(booking)
        db.session.commit()

        # Assert that the booking no longer exists
        self.assertEqual(db.session.query(Booking).count(), 0)


if __name__ == '__main__':
    unittest.main()
