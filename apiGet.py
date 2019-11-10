import requests
import json

response = requests.get("https://api.noopschallenge.com/hexbot")

if response.status_code == 200:
    print("Success in connecting to API")
else:
    print("Error in making API call")

print(response.content.decode("utf-8"))

#print(type(response.json()))

data = response.json()
print(data["colors"])

#print(response.headers)

#parsed = json.loads(data)

