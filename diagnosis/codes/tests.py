from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from .views import CodeListViewSet


# Create your tests here.

class CODEAPITestCase(APITestCase):

    def test_all_codes_api_calls(self):
        response = self.client.get("/codes/all")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_codes_with_WRONGICD(self):
        response = self.client.get('/codes/all?ICD=ICD-65')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_pagination_withICD(self):
        factory = APIRequestFactory()
        view = CodeListViewSet.as_view({'get': 'list'})
        request = factory.get("/codes/all?ICD=ICD-10&page=2")
        response = view(request)
        response.render()
        print(response.content)

    def test_api_new_call(self):
        self.client = APIClient()
        response = self.client.get("/codes/all")
        print(response.content)
