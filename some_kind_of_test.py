import unittest
import requests

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000'

    def test_signup(self):
        data = {'username': 'test_user', 'password': 'test_password'}
        response = requests.post(f'{self.url}/signup', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Ви зареєстровані')

    def test_login(self):
        data = {'username': 'test_user', 'password': 'test_password'}
        response = requests.post(f'{self.url}/login', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Ви увійшли в акаунт')
