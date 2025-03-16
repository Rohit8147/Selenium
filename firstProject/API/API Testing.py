from http.client import responses

import requests
import json
url="https://fakerestapi.azurewebsites.net/api/v1/Activities/5"
response=requests.get(url)
print(response.status_code)
assert response.status_code == 200



