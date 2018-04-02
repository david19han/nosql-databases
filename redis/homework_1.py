import requests
parameters = {"date": "1995-11-19"}
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=3hWwkDdZ1xdwjTNpKO2nmqkTHexZ7r9K8hyKS8Q4", params=parameters)
data = response.json()
print(data["url"])
