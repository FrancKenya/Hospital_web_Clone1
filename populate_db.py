#!/usr/bin/python3

from app import db, create_app
from app.models.branch import Branch
from app.models.service import Service

app = create_app()
# Create branch data
branches_data = [
    {'name': 'Nairobi Branch', 'location': 'Nairobi, Kenya'},
    {'name': 'Mombasa Branch', 'location': 'Mombasa, Kenya'},
    {'name': 'Kisumu Branch', 'location': 'Kisumu, Kenya'}
]

# Create service data
services_data = [
    {'name': 'General Consultation', 'description': 'Consultation with a general practitioner'},
    {'name': 'Surgical Services', 'description': 'Full range of surgeries'},
    {'name': 'Maternal and Child Health', 'description': 'Services for mothers and children'},
    {'name': 'Oncology', 'description': 'Cancer diagnosis and treatment'},
    {'name': 'Psychiatry and Mental Health', 'description': 'Mental health consultations and treatments'},
    {'name': 'Laboratory Services', 'description': 'Blood tests, cultures, etc.'},
    {'name': 'Radiology Services', 'description': 'X-rays, MRI, CT scans, Ultrasounds'},
    {'name': 'Pathology Services', 'description': 'Lab analysis of tissue samples'},
    {'name': 'Pharmacy Services', 'description': 'Pharmaceuticals and medications'},
    {'name': 'Dialysis Unit', 'description': 'Kidney-related treatments'},
    {'name': 'Dental and Eye Care Services', 'description': 'Dental and eye health services'},
    {'name': 'Ophthalmology', 'description': 'Eye surgeries and treatments'}
]

# Updated branch data in populate_db.py
branches_data = [
    {
        'name': 'Nairobi Branch',
        'location': 'Nairobi, Kenya',
        'contacts': '0722 000 111',
        'email': 'nairobi@injeelhospital.com'
    },
    {
        'name': 'Mombasa Branch',
        'location': 'Mombasa, Kenya',
        'contacts': '0733 111 222',
        'email': 'mombasa@injeelhospital.com'
    },
    {
        'name': 'Kisumu Branch',
        'location': 'Kisumu, Kenya',
        'contacts': '0744 222 333',
        'email': 'kisumu@injeelhospital.com'
    }
]

with app.app_context():
    # Create all the tables if they don't exist
    db.create_all()

    # Populate Branches
    for branch_data in branches_data:
        branch = Branch(**branch_data)
        db.session.add(branch)

    db.session.commit()  # Commit branches to the database

    # Now that branches are committed, we need to associate services with branches
    for service_data in services_data:
        # Assign services to a branch. For simplicity, let's assign all services to the first branch (Nairobi Branch).
        branch_nairobi = Branch.query.filter_by(name="Nairobi Branch").first()
        service = Service(**service_data, branch=branch_nairobi)
        db.session.add(service)

    db.session.commit()  # Commit services to the database

    print("Database populated successfully!")