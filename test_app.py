import unittest
import json
from app import app


class FlaskAppTestCase(unittest.TestCase):
    """Test cases for the Flask application"""

    def setUp(self):
        """Set up test client before each test"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_hello_world(self):
        """Test the main endpoint returns 'Hello, World!'"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')
        print("✓ Test passed: GET / returns 'Hello, World!'")

    def test_health_endpoint(self):
        """Test the health check endpoint"""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['status'], 'healthy')
        print("✓ Test passed: GET /health returns healthy status")

    def test_404_error(self):
        """Test that invalid routes return 404"""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        print("✓ Test passed: Invalid route returns 404")


if __name__ == '__main__':
    print("\n" + "="*50)
    print("Running Flask Application Tests")
    print("="*50 + "\n")

    # Run tests with verbose output
    unittest.main(verbosity=2)
