import unittest
from app import create_app

class TestBookingRoutes(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.app = create_app()  # Make sure this points to your Flask app factory
        self.client = self.app.test_client()  # Use test client to simulate HTTP requests
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Tear down test environment"""
        self.app_context.pop()

    def test_get_available_services(self):
        """Test retrieving the list of available services"""
        response = self.client.get('/bookings/services')  # Adjust this route based on booking_routes.py

        # Assert that the request was successful
        self.assertEqual(response.status_code, 200)

        # Optionally: Check if the response contains expected HTML content
        self.assertIn(b'Select a Service', response.data)  # Example check for text in the HTML

    def test_create_booking(self):
        """Test creating a booking for a specific service"""
        payload = {
            'patient_name': 'Francis Waihiga',
            'service_id': 'General Consultation',  # Replace with a valid service ID
            'appointment_time': '2024-09-25T14:00:00'
        }

        response = self.client.post(
            '/bookings',
            data=payload,  # Send the form data as a dictionary
            content_type='application/x-www-form-urlencoded'  # Typical for HTML form submissions
        )

        # Assert that the booking was successfully created (redirects to confirmation page or shows success)
        self.assertEqual(response.status_code, 200)

        # Optionally: Check if the response contains expected HTML content
        self.assertIn(b'Booking Successful', response.data)  # Example check for success message



if __name__ == '__main__':
    unittest.main()
