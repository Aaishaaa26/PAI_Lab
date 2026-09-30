import json

filename = "model_results.json"

def display(filename):
    with open(filename) as file:
        data = json.load(file)
        for model in data:
            print(model)

def highAccuracy():
    with open(filename) as file:
        data = json.load(file)
    highest = data[0]

    for model in data:
        if model["accuracy"] > highest["accuracy"]:
            highest = model
    print("Highest accuracy: ", highest)

def highestF1():
    with open(filename) as file:
        data = json.load(file)
    highest = data[0]
    for model in data:
        if model["f1"] > highest["f1"]:
            highest = model
    print("Highest F1 score: ", highest)

def add(name, accuracy, precision, recall, f1):
    with open(filename, "r") as file:
        data = json.load(file)
        newModel = {"name": name, "accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
        data.append(newModel)
    with open(filename, "w") as file:
        json.dump(data, file)

def update(name, accuracy, precision, recall, f1):
    with open(filename, "r") as file:
        data = json.load(file)
        for model in data:
            if model["name"] == name:
                model["accuracy"] = accuracy
                model["precision"] = precision
                model["recall"] = recall
                model["f1"] = f1
    with open(filename, "w") as file:
            json.dump(data, file)
            print("Updated")

def delete(name):
    with open(filename, "r") as file:
        data = json.load(file)
        newData = []
        for model in data:
            if model["name"] != name:
                newData.append(model)
    with open(filename, "w") as file:
        json.dump(newData, file)
        print("Deleted")

data = [ { "name": "CNN", "accuracy": 0.91, "precision": 0.89, "recall": 0.92, "f1": 0.90 }, { "name": "RNN", "accuracy": 0.87, "precision": 0.85, "recall": 0.88, "f1": 0.86 }, { "name": "Random Forest", "accuracy": 0.94, "precision": 0.93, "recall": 0.91, "f1": 0.92 } ]
file = open(filename, "w")
json.dump(data, file)
file.close()
update("CNN", 0.98, 0.9, 0.83, 0.93)
add("SVM", 0.89, 0.88, 0.90, 0.89)
highAccuracy()
highestF1()
display(filename)
delete("Random Forest")
display(filename)