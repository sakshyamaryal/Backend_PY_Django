import django.db
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from playground.models import Post, Category
from django.contrib.auth.models import User

# Create your tests here.
class PostTest(APITestCase):

    def test_view_post(self):
        url = reverse('dev_api:listcreate')
        response = self.client.get(url, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK) # compareing with respone var with the status code
        # client refer to simulating a browser 

    def create_post(self):
        self.test_category = Category.objects.create(name = 'django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='123456789')

        data = {"title":"new",
                "author":1,
                "excerpt":"new",
                "content":"new",
                }
        url = reverse('dev_api:listcreate')
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # compareing with respone var with the status code
