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

