Hospital Management Website
This is a web-based project for managing the services, bookings, and branches of a hospital. The project is designed to provide users with easy access to hospital information such as the available services, branches, and contact details. Additionally, it includes an intuitive front-end interface and integrated back-end management system.

Author
Francis Waihiga

Project Overview
This project is structured with the following key sections:

Front-End (HTML/CSS/JS):

Header Section: Contains social media links (Facebook, Instagram, TikTok, X), contact details (Email, Call Us), styled with CSS to fit the hospital's theme.
Navigation Bar: Provides access to major sections of the website (Home, Services, Contacts, Branches) with dropdown menus for some items.
Carousel: Displays images related to the hospital, with a zoom-out transition effect that transitions into a blue background.
Responsive Design: The project is styled to ensure compatibility with various screen sizes, especially on mobile devices.
Back-End (Flask/Python):

BaseModel Class: This class provides the foundation for all models in the project, including common methods and attributes like id, created_at, and updated_at.
Service Class: Represents the different services offered by the hospital. Each service has a name, description, and relationship with bookings.
Booking Class: Handles the booking of services by patients. Each booking is tied to a specific service.
Database Integration: SQLAlchemy is used for ORM, with an SQLite database for development purposes.

Front-End Design
Header:

The header contains links to social media icons (Facebook, Instagram, TikTok, and X) on the left side.
Contact details (Email, Call Us) are on the right side.
The header background is green, with the text and icons styled in white.
Navigation Menu:

The navigation menu is hidden by default under the header section but contains links to various sections of the hospital, such as Services, Contacts, and Branches.
Each menu item, such as "Branches," includes a dropdown with additional links.
Arrows are placed next to dropdown items to indicate more options.
Carousel:

A carousel section displays hospital-related images with a zoom-out transition effect. The empty space during the transition is filled with a blue background.
Back-End Overview
BaseModel:

Common attributes like id, created_at, and updated_at are stored here.
All other models inherit from BaseModel.
Service Model:

Represents the services offered by the hospital.
Contains a name, description, and relationships with the Booking class.
Booking Model:

Handles the booking information for the services.
Links patients with a specific hospital service.

Technologies Used
Front-End: HTML5, CSS3, JavaScript
Back-End: Flask, Python, SQLAlchemy
Database: SQLite (for development)
Future Improvements
Implement user authentication for secure booking.
Add more dynamic content and optimize performance.
Integrate with a production-grade database system (e.g., PostgreSQL).
