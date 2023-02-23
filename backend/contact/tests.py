from .models import Contact
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

class ContactTestCase(APITestCase):
    """
    Test cases for Contact
    """

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name":"ang",
            "message":"hello ninja",
            "email":"ninja@gmail.com"
        }
        self.url = "/contact/"
    
    def test_create_contact(self):
        """
        Test ContactViewSet post method
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(),1)
        self.assertEqual(Contact.objects.get().title,"ang")

    def test_create_contact_without_name(self):
        """
        Test ContactViewSet method when name is not in data
        """
        data = self.data
        data.pop("name")
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_without_message(self):
        """
        Test ContactViewSet method when message is not in data
        """
        data = self.data
        data.pop("message")
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_without_email(self):
        """
        Test ContactViewSet method when email is not in data
        """
        data = self.data
        data.pop("email")
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_email_is_blank(self):
        """
        Test ContactViewSet method when email field is blank
        """
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_email_equals_non_email(self):
        """
        Test ContactViewSet method when email is not email
        """
        data = self.data
        data["email"] = "none"
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    
