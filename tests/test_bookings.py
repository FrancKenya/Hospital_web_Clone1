#!/usr/bin/python3

""" This module contains the test cases for the booking model """

from app.models.basemodel import BaseModel
from app.models.branch import Branch
from app.models.booking import Booking
from app.models.service import Service
from app import create_app
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import unittest


class TestBookingModel(unittest.TestCase):
    """Test the Booking service model"""
    def setUp(self):
        """Sets up the test environment"""
        self.app = create_app()
        self.engine = create_engine('sqlite:///:memory:')
        BaseModel.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        """Cleans up the test environment"""
        self.session.close()
        BaseModel.metadata.drop_all(self.engine)

    def test_create(self):
        """Test the creation of the booking model"""
        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()
        service = Service(
            name='Consultation', description='General Consultation', branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        booking = Booking(
            patient_name='Francis Waihiga', patient_details='test',
            service_id=service.id)
        self.session.add(booking)
        self.session.commit()
        self.assertEqual(booking.patient_name, 'Francis Waihiga')
        self.assertEqual(booking.patient_details, 'test')
        self.assertIn(booking.service_id, service.id)

    def test_update(self):
        """Test the update of the booking model"""
        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()
        service = Service(
            name='Consultation', description='General Consultation', branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        booking = Booking(
            patient_name='John Ndungu', patient_details='test',
            service_id=service.id)
        self.session.add(booking)
        self.session.commit()
        booking.patient_name = 'John Doe'
        self.session.commit()
        self.assertEqual(booking.patient_name, 'John Doe')

    def test_delete(self):
        """Test the deletion of a booking"""
        branch = Branch(name="Main", location="150 Nyumba Moja road", contacts="0720268453", email="branch@example.com")
        self.session.add(branch)
        self.session.commit()
        service = Service(
            name='Consultation', description='General Consultation', branch_id=branch.id)
        self.session.add(service)
        self.session.commit()
        booking = Booking(
            patient_name='John Karis', patient_details='test',
            service_id=service.id)
        self.session.add(booking)
        self.session.commit()
        self.session.delete(booking)
        self.session.commit()
        self.assertEqual(self.session.query(Booking).count(), 0)


if __name__ == '__main__':
    unittest.main()
