import requests
import json
import csv

url = "https://jsonplaceholder.typicode.com/posts"
userId = input("Enter user id: ")
id = { "userId": userId}

try:
    response = requests.get(url, params=id)
    if response.status_code == 200:
        data = response.json()
        processedData = []
        for post in data:
            postId = post["id"]
            title = post["title"]
            user = post["userId"]
            processedData.append({"id": postId, "title": title, "userId": user})
        print("Total posts:", len(processedData))
        highest = processedData[0]
        for post in processedData:
            if post["id"] > highest["id"]:
                highest = post
        print("Highest post ID:", highest["id"])
        print("Title:", highest["title"])

        with open("processed_data.json", "w") as file:
            json.dump(processedData, file)

        with open("processed_data.csv", "w", newline="") as file:
            fields = ["id", "title", "userId"]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(processedData)

        print("Data saved successfully.")

    else:
        print("API could not provide the requested data.")
        print("Error code:", response.status_code)

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.Timeout:
    print("Timeout Error")

except requests.exceptions.HTTPError:
    print("HTTP Error")

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid JSON data")

except Exception as e:
    print("Error:", e)

else:
    try:
        with open("processed_data.json") as file:
            jsonData = json.load(file)

        print("\nChecking JSON file:")
        print("Number of records:", len(jsonData))

        with open("processed_data.csv") as file:
            csvData = csv.reader(file)
            print("Checking CSV file:")
            for row in csvData:
                print(row)

    except FileNotFoundError:
        print("Saved file was not found.")

    except ValueError:
        print("Invalid JSON data in saved file.")
finally:
    print("Program finished.")