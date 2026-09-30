import requests
url = "https://jsonplaceholder.typicode.com/users/1"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for key in data:
            print(key, ":", data[key])
    
    else:
        print("Error code:", response.status_code, ". API cant provide results")
except requests.exceptions.ConnectionError:
    print("Connection Error")
except requests.exceptions.Timeout:
    print("Timeout Error")
except requests.exceptions.HTTPError:
    print("Http Error")
except ValueError:
    print("Value Error")
except Exception as e:
    print(e)
