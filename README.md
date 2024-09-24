Injeel Hospital - Hospital Management System

Introduction

Injeel Hospital is a modern hospital management system designed to streamline the booking of medical services, allowing doctors and patients to interact seamlessly. The application enables patients to book services at different branches, manage their appointments, and access medical history. Doctors can view appointments and provide diagnoses, prescriptions, and referrals directly within the system.

The project was developed as a full-stack web application using Flask for the backend and a custom frontend.

A link for a demo to be added

Check out the final project blog post here.
linkedin.com

Author
Francis Waihiga
LinkedIn Profile

Table of Contents
Project Name
Introduction
Features
Installation
Usage
Contributing
Related Projects
Licensing
Screenshot

Features

Service Booking: Patients can book medical services such as general consultations, pharmacy services, laboratory tests, and more.

Branch Selection: Patients can select specific branches (Nairobi, Mombasa, Kisumu) during booking.

Doctor View: Doctors can filter bookings by date, time, service, and branch.

Secret Password Access: Doctors can access their view using a secret word known to them.

Medical History: Doctors can add diagnoses, prescriptions, and referrals for patients.

Service Categories: Services are categorized into outpatient, inpatient, and specialty clinics for easy navigation.

Installation
To get the project running locally, follow these steps:

Prerequisites
Ensure you have the following installed:

Python 3.x
Git
Virtualenv (optional but recommended)

Steps

Clone the repository:

git clone <https://github.com/francis-waihiga/Hospital_web_clone1.git>
Navigate to the project directory:
cd Hospital_web_clone1

Create and activate a virtual environment (optional):
python3 -m venv venv
source venv/bin/activate  # For Windows, use venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Set environment variables (create a .env file in the root directory):
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///hospital.db

Run database migrations:
flask db upgrade
Run the application:
flask run

Visit the app in your browser at:
<http://127.0.0.1:5000>

Usage

For Patients
Book an Appointment: Select your desired service and branch, then book a session based on availability.
Check Booking Status: Patients can view their current booking status and rebook if necessary.

For Doctors
Doctor's View: Log in with the secret password at the bottom of the homepage to access patient bookings. Filter by service, branch, or date to view appointment details.
Update Patient Records: Add diagnoses, prescriptions, or referrals during or after patient visits.

Contributing
Contributions to this project are welcome. To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch-name).
Make your changes and commit them (git commit -m "description of changes").
Push to the branch (git push origin feature-branch-name).
Submit a pull request.

Related Projects
Check out similar projects:

Hospital Management System
Medical Booking System
Licensing
This project is licensed under the MIT License. See the LICENSE file for details.

Screenshot
![alt text](<../Hospital_web_Clone1/docs/assets/images/filtering.jpg>)
![alt text](<../Hospital_web_Clone1/docs/assets/images/filtering2.jpg>)
