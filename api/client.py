import requests

endpoint = "http://127.0.0.1:8000/api/"
json = {"link":"http://www.itsme.com"}

response= requests.post(endpoint, json = json)

print(response.text)