from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_register_page_status_code(self):
        response_status = self.client.get('/register/')
        self.assertEqual(response_status.status_code, 404)

    def test_login_page_status_code(self):
        response_status = self.client.get('/login/')
        self.assertEqual(response_status.status_code, 404)

    def test_dashboard_page_status_code(self):
        response_status = self.client.get('/dashboard/')
        self.assertEqual(response_status.status_code, 404)
