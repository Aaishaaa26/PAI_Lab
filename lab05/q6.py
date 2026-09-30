import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url + "/1") #/1 means asking for posyId 1
    print("GET")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()

    newData = {"title": "Image Prediction", "body": "Cat detected", "userId": 1}

    response = requests.post(url, json=newData)
    print("POST")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()

    updateData = { "id": 1, "title": "Updated Prediction", "body": "Dog detected", "userId": 1}

    response = requests.put(url + "/1", json=updateData)
    print("PUT")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()

    response = requests.delete(url + "/1")
    print("DELETE")
    print("Status Code:", response.status_code)
    print("Response:", response.text)

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.Timeout:
    print("Timeout Error")

except requests.exceptions.HTTPError:
    print("HTTP Error")

except ValueError:
    print("Invalid JSON response")

except Exception as e:
    print("Error:", e)