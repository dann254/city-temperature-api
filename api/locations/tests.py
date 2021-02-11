from rest_framework import status
from rest_framework.test import APITestCase, APIClient


client = APIClient()

class LocationsTest(APITestCase):
    """ Test module for Locations"""


    base_url = '/locations/'

    def setUp(self):
        pass

    def test_get_list_of_cities(self):
        """Test if user can get a list of cities"""
        response = client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_city_temp_details(self):
        """Test if user can get temperature details for a given city"""
        city = 'Nairobi'
        response = client.get(self.base_url + city+ '/' )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_city_temp_average_details(self):
        """Test if user can get average temperature details for a given city"""
        city = 'Nairobi'
        days = 3
        response = client.get(self.base_url + city + '/?days=' + str(days))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
