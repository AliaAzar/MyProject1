import unittest
import requests

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000'

    # def test_signup(self):
    #     data = {'username': 'test_user', 'password': 'test_password','confirm-password':'test_password', 'mail':'mail@gmail.com'}
    #     response = requests.post(f'{self.url}/signup', data= data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['message'], 'Ви зареєстровані!!!!!!!!')
    #
    # def test_login(self):
    #     data = {'username': 'test_user', 'password': 'test_password'}
    #     response = requests.post(f'{self.url}/login', data=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['message'], 'Ви увійшли в акаунт!!!!!!')
    #     self.assertTrue(response.json()['message'])

    # def test_city(self):
    #     data = {'city': 'test_city'}
    #     response = requests.post(f'{self.url}/', data=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(response.text)

    # def test_history(self):
    #     data = {'history': 'test_history'}
    #     response = requests.post(f'{self.url}/history', data=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(response.session2)



if __name__ == '__main__':
    unittest.main()
