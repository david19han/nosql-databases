#Please note that in order for this script to work "requests" module must be installed. Thus, "pip install requests" will need to be done before running this script.
import requests
parameters = {"date": "2017-11-19"}
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=3hWwkDdZ1xdwjTNpKO2nmqkTHexZ7r9K8hyKS8Q4", params=parameters)
data = response.json()
print(data["url"])
