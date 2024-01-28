import requests

def establish_spy_network(url):
    response = requests.get(url)
    if response.status_code == 200:
        return "Spy network established successfully."
    else:
        return "Failed to establish spy network."

network_url = "https://example.com/spy-network"
result = establish_spy_network(network_url)
print(result)