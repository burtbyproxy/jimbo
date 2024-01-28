import requests

url = "https://government_database.com"
params = {
    "username": "admin",
    "password": "password"
}

response = requests.post(url, data=params)
data = response.json()
print(data)