from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Codes, ICD


# Create your tests here.

class CODEAPITestCase(APITestCase):
    def test_api_calls(self):
        response = self.client.get("/all/codes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
