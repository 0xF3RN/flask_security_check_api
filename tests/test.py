import requests
import json
'''
not done yet
'''
json_data = {
    "username": "user",
    "password": "your_password22"
}
url = 'http://127.0.0.1:5000/api/v2/add_password'
url2 = 'http://127.0.0.1:5000/api/v2/check_password'
url3 = 'http://127.0.0.1:5000/api/v2/remove_password'
#response = requests.post(url, json=json_data, verify=False)
#response = requests.get(url2, json=json_data, verify=False)
response2 = requests.post(url3, json=json_data, verify=False)
print(response2.text)
