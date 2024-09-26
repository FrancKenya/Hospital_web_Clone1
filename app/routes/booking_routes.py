#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.service import Service
from app.models.booking import Booking
from app.models.branch import Branch
from app import db
from datetime import datetime


booking_routes = Blueprint('bookings', __name__)

# Route to display the booking form
@booking_routes.route('/bookings', methods=['GET'])
def show_booking_form():
    """Show the booking form"""
    services = Service.query.all()  # Retrieve available services from the database
    branches = Branch.query.all()
    return render_template('booking_form.html', services=services, branches=branches)  # Render the form with service options

# Route to handle booking submission
@booking_routes.route('/bookings', methods=['POST'])
def submit_booking():
    """Collect data to be submitted for booking"""
    patient_name = request.form.get('patient_name')
    patient_age = request.form.get('patient_age')
    patient_gender = request.form.get('patient_gender')
    patient_details = request.form.get('patient_details')
    service_id = request.form.get('service_id')
    appointment_time = request.form.get('appointment_time')
    branch_id = request.form.get('branch_id')

    # Validate form inputs
    if not patient_name or not service_id or not appointment_time:
        flash('Please fill all the required fields', 'error')
        return redirect(url_for('bookings.show_booking_form'))

    # Check if service_id exists in the database
    if not service_id:
        flash('No service selected', 'error')
        return redirect(url_for('bookings.show_booking_form'))

    service = Service.query.get(service_id)
    if not service:
        flash('Invalid service selected', 'error')
        return redirect(url_for('bookings.show_booking_form'))

    if not branch_id or not patient_name:
        flash('Please fill all the required fields', 'error')
        return redirect(url_for('bookings.show_booking_form'))

    # Convert appointment_time to a datetime object
    print(f"Raw appointment time input: {appointment_time}")
    try:
        appointment_time = datetime.strptime(appointment_time, '%Y-%m-%dT%H:%M')
    except ValueError:
        flash('Invalid appointment time format', 'error')
        return redirect(url_for('bookings.show_booking_form'))

    # Check if the service is available at the requested time
    existing_booking = Booking.query.filter_by(service_id=service_id, branch_id=branch_id, appointment_time=appointment_time).first()
    if existing_booking:
        flash('This time slot is already booked', 'error')
        return redirect(url_for('bookings.show_booking_form'))

    # Save the new booking
    new_booking = Booking(
        patient_name=patient_name,
        patient_age=patient_age,
        patient_gender=patient_gender,
        patient_details=patient_details,
        service_id=service_id,
        appointment_time=appointment_time,
        branch_id=branch_id
    )

    try:
        db.session.add(new_booking)
        db.session.commit()
        service_name = service.name
        branch_name = Branch.query.get(branch_id).name
        flash('Booking successful!', 'success')
        return render_template('booking_confirmation.html',
                               patient_name=patient_name,
                               service_name=service_name,
                               branch_name=branch_name,
                               appointment_time=appointment_time)
        #return redirect(url_for('bookings.booking_confirmation'))
    except Exception as e:
        db.session.rollback()
        flash(f"Error booking appointment: {str(e)}", 'error')
        return render_template('booking_form.html')

@booking_routes.route('/booking_confirmation')
def booking_confirmation():
    return render_template('booking_confirmation.html')

@booking_routes.route('/doctor/bookings', methods=['GET'])
def doctor_view():
    # Get all the filter values from query parameters
    selected_date = request.args.get('date')
    selected_time = request.args.get('time')
    selected_service = request.args.get('service')
    selected_branch = request.args.get('branch')

    # Query for bookings
    bookings_query = Booking.query

    # Apply filters based on doctor selection
    if selected_date:
        bookings_query = bookings_query.filter(
            db.func.date(Booking.appointment_time) == selected_date)
    if selected_time:
        bookings_query = bookings_query.filter(
            db.func.time(Booking.appointment_time) == selected_time)
    if selected_service:
        bookings_query = bookings_query.filter(
            Booking.service_id == selected_service)
    if selected_branch:
        bookings_query = bookings_query.filter(
            Booking.branch_id == selected_branch)

    # Execute the query
    bookings = bookings_query.all()

    # Get services and branches for dropdown filters
    services = Service.query.all()
    branches = Branch.query.all()

    return render_template(
        'doctor_view.html', bookings=bookings, services=services,
        branches=branches, selected_date=selected_date,
        selected_time=selected_time, selected_service=selected_service,
        selected_branch=selected_branch)


# Set a secret word for doctor access (can be moved to a config file)
SECRET_WORD = "injil"

# Route to handle doctor access
@booking_routes.route('/doctor-login', methods=['POST'])
def doctor_login():
    entered_password = request.form.get('secret_word')

    # Check if the entered password matches the secret word
    if entered_password == SECRET_WORD:
        # Redirect to the doctor view page
        return redirect(url_for('bookings.doctor_view'))
    else:
        # Show an error message if the password is incorrect
        flash('Incorrect secret word. Please try again.', 'error')
        return redirect(url_for('home.home'))  # Redirect back to the homepage


populate_routes = Blueprint('populate_routes', __name__)

@populate_routes.route('/populate-db')
def populate_db():
    # Check if already populated (to avoid multiple insertions)
    if Branch.query.first() and Service.query.first():
        return "Database already populated."

    # Branches data
    branches_data = [
        {'name': 'Nairobi Branch', 'location': 'Nairobi, Kenya', 'contacts': '0722 000 111', 'email': 'nairobi@injeelhospital.com'},
        {'name': 'Mombasa Branch', 'location': 'Mombasa, Kenya', 'contacts': '0733 111 222', 'email': 'mombasa@injeelhospital.com'},
        {'name': 'Kisumu Branch', 'location': 'Kisumu, Kenya', 'contacts': '0744 222 333', 'email': 'kisumu@injeelhospital.com'}
    ]

    # Services data
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

    with db.app.app_context():  # Ensure this is running in the correct app context
        # Create all the tables if they don't exist
        db.create_all()

        # Populate Branches
        for branch_data in branches_data:
            branch = Branch(**branch_data)
            db.session.add(branch)

        db.session.commit()  # Commit branches to the database

        # Now that branches are committed, assign services to a branch (Nairobi Branch in this case)
        branch_nairobi = Branch.query.filter_by(name="Nairobi Branch").first()
        if branch_nairobi:
            for service_data in services_data:
                service = Service(**service_data, branch=branch_nairobi)
                db.session.add(service)

            db.session.commit()  # Commit services to the database

    return "Database populated successfully!"
