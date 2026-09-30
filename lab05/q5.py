import requests
import json
import csv

url = "https://jsonplaceholder.typicode.com/comments"
postId = input("Enter post id: ")
id = {"postId": postId}
try:
    response = requests.get(url, params=id)
    data = response.json()

    if response.status_code == 200:
        specificData = []
        for values in data:
            body = values["body"]
            name = values["name"]
            email = values["email"]

            specificData.append({"name": name,"email": email,"body": body})
            print(specificData)

        with open("text_data.json", "w") as file:
            json.dump(specificData, file)
        with open("text_data.csv", "w", newline="") as file:
            fields = ["name","email","body"]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(specificData)
    else:
        print("API didnt work, Error code: ", response.status_code)
except requests.exceptions.ConnectionError:
    print("Connection error")
except ValueError:
    print("Value error")
except requests.Timeout:
    print("Timeout error")

except Exception as e:
    print("Error code: ", e)
