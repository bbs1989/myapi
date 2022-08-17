from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from .models import User

class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()
        self.user_data = {
            'email':self.fake.email(),
            'username':self.fake.email().split('@')[0],
            'password':self.fake.email(),
        }
        return super().setUp()
    def tearDown(self):
        return self.tearDown()

class TestViews(TestSetup):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
    def test_user_can_register_correctly(self):
        res = self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)
    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(
            self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 401)
