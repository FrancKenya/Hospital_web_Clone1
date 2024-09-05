#!/usr/bin/python3

""" This module contains the test cases for the branch model """

from app.models.basemodel import Base
from app.models.branch import Branch
from app.models.service import Service
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest

class TestBranchModel(unittest.TestCase):
      """Unit tests for the Branch model"""
    def setUp(self):
      """Setup for the test cases"""
    self.engine = create_engine('sqlite:///:memory:')
    #    Base.metadata.create_all(self.engine)
    #   Session = sessionmaker(bind=self.engine)
    #    self.session = Session()

    #def tearDown(self):
     #   """Teardown for the test cases"""
    #    Base.metadata.drop_all(self.engine)
      #  self.session.close()

   # def test_create(self):
    #    """Test the creation of the branch"""
    #    branch = Branch(
    #        name='Main', location='150 Nyumba Moja road', contact='0720268453', email='francusgwaihiga@gmail.com')
     #   self.session.add(branch)
     #   self.session.commit()
        #service = Service(
          #  name='Consultation', description='General Consultation',
         #   branch_id=branch.id)
        #self.session.add(service)
        #self.session.commit()
        #saved_service = self.session.query(Service).filter_by(id=service.id).first()
        #self.assertEqual(saved_service.name, 'Consultation')
        #self.assertEqual(saved_service.description, 'General Consultation')
        #self.assertEqual(saved_service.branch_id, branch.id)
        #self.assertEqual(branch.contact,'0720268453')
        #self.assertEqual(branch.email, 'francusgwaihiga@gmail.com')


if __name__ == '__main__':
  unittest.main()
