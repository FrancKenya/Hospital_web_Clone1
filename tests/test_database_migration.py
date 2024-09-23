#!/usr/bin/python3

"""Used to test database migration"""


import unittest
from app import create_app, db
from app.models.service import Service

class TestDatabaseIntegration(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app.app_context().push()

        # Create all tables
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_service_creation(self):
        service = Service(name="Test Service", description="Test Description")
        db.session.add(service)
        db.session.commit()

        fetched_service = Service.query.first()
        self.assertEqual(fetched_service.name, "Test Service")

if __name__ == '__main__':
    unittest.main()
