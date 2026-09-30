import csv
filename = "ppatient.csv"

def display():
    with open(filename) as file:
        data = csv.DictReader(file)
        for row in data:
            print(row)

def numOfCases():
    with open(filename) as file:
        line = csv.DictReader(file)
        neg = 0
        pos= 0
        for row in line:
            if row["prediction"] == "+":
                pos += 1
            else:
                neg += 1
        print("Positivie cases: ", pos)
        print("Negativie cases: ", neg)

def highGlucose(threshold):
    with open(filename) as file:
        line = csv.DictReader(file)
        for row in line:
            if float(row["Glucose"]) > threshold:
                print("Glucose level higher than threshols: ",row)

def avg():
    with open(filename) as file:
        line = csv.DictReader(file)
        totalBMI = 0
        totalGlucose = 0
        count = 0
        for row in line:
            totalBMI += float(row["BMI"])
            totalGlucose += float(row["Glucose"])
            count += 1

        print("Avg BMI: ", totalBMI/count)
        print("Avg Glucose: ", totalGlucose/count)

def add(id,age, bmi, bp, glucose, predict):
    with (open(filename,"a", newline="") as file):
        line = csv.writer(file)
        line.writerow([id,age,bmi,bp,glucose, predict])

def update(id, age, bmi, bp, glucose, predict):
    with open(filename) as file:
        line = csv.DictReader(file)
        newRows = []
        for row in line:
            if row["ID"] == str(id):
                row["age"] = age
                row["BMI"] = bmi
                row["bp"] = bp
                row["Glucose"] = glucose
                row["prediction"] = predict
            newRows.append(row)
    with open(filename, "w", newline="") as file:
        fields = ["ID", "age", "BMI", "bp", "Glucose", "prediction"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newRows)

with open(filename, "w", newline ="") as file:
    fields = ["ID", "age", "BMI", "bp", "Glucose", "prediction"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerow({    "ID": 101,    "age": 45,    "BMI": 28.5,    "bp": 80,    "Glucose": 140,    "prediction": "+"})
    writer.writerow({    "ID": 102,    "age": 32,    "BMI": 24.2,   "bp": 75,    "Glucose": 95,    "prediction": "-" })
    writer.writerow({    "ID": 103,    "age": 50,    "BMI": 31.4,    "bp": 85,    "Glucose": 180,    "prediction": "+"})
display()
numOfCases()
highGlucose(130)
avg()
add(104, 56, 25.5, 80, 150, "-")
update(101,45, 28.5, 90, 140, "-" )
display()