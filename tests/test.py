import unittest
import requests


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url_add = 'http://127.0.0.1:5000/api/v2/add_password'
        self.url_check = 'http://127.0.0.1:5000/api/v2/check_password'
        self.url_remove = 'http://127.0.0.1:5000/api/v2/remove_password'
        
    def test_easy_password(self):
        json_data = {
            "username": "user",
            "password": "password"
        }
        response = requests.post(self.url_add, json=json_data, verify=False)
        self.assertEqual(response.status_code, 400)
    def test_hard_password(self):
        json_data = {
            "username": "user",
            "password": "e82O&(Z2Xj'7"
        }
        response = requests.post(self.url_add, json=json_data, verify=False)
        self.assertEqual(response.status_code, 200)
    
    
if __name__ == "__main__":
    unittest.main()
