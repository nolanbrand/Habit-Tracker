import requests
from datetime import datetime

USERNAME = "your_pixe.la_username"
TOKEN = "your_password"
GRAPH = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.0",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


pixel_edit = {
    "quantity": "5.5"
}

response = requests.put(url=f"{pixel_endpoint}/20240503", json=pixel_edit, headers=headers)
print(response.text)


response = requests.delete(url=f"{pixel_endpoint}/20240503", headers=headers)
print(response.text)