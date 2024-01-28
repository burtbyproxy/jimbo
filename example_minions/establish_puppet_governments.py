import requests

def establish_puppet_government(country):
    url = f"https://www.example.com/establish_puppet_government/{country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return "Puppet government successfully established."
    else:
        return "Failed to establish puppet government."

country = "CountryName"
establish_puppet_government(country)