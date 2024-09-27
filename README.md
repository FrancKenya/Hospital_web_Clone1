Injil Hospital - Hospital Management System

Introduction

Injil Hospital is a modern hospital management system designed to streamline the booking of medical services, allowing healthcare worers and patients to interact seamlessly. The application enables patients to book services at different branches, manage their appointments, and access medical history. Healthcare workers can view appointments and provide diagnoses, prescriptions, and referrals directly within the system.

The project was developed as a full-stack web application using Flask for the backend and a custom frontend developed using HTML, CSS and JavaScript

Check out the final project blog post here.
<https://www.linkedin.com/pulse/project-overview-injeel-hospital-management-system-francis-waihiga-bodhf>

Author
Francis Waihiga
LinkedIn URL: <https://www.linkedin.com/in/francis-waihiga-476198209/>

Table of Contents

1. Project Name
2. Introduction
3. Features
4. Installation
5. Usage
6. Contributing
7. Related Projects
8. Licensing
9. Screenshot

Features

Service Booking: Patients can book medical services such as general consultations, pharmacy services, laboratory tests, and more.

Branch Selection: Patients can select specific branches (Nairobi, Mombasa, Kisumu) during booking.

Doctor View: Doctors can filter bookings by date, time, service, and branch.

Secret Password Access: Doctors can access their view using a secret word known to them.

Service Categories: Services are categorized into outpatient, inpatient, and specialty clinics for easy navigation.

Live demo: <https://flonnect.com/video/976ed2dbe1e4-4095-ac7c-e9987510ae0f>

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
This project is open source and welcomes contributions from the community! Whether you're fixing a bug, improving documentation, or adding a new feature, your efforts are appreciated.

Screenshot
![alt text](<../Hospital_web_Clone1/docs/assets/images/filtering.jpg>)
![alt text](<../Hospital_web_Clone1/docs/assets/images/filtering2.jpg>)
