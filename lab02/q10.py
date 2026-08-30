employees = [
    ("E101", "Ali", "IT", 85000),  ("E102", "Sara", "HR", 75000),  ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]
unique = set()
total = 0
highestSalary = 0
highestSalaryID = ""
count ={}
employeeID = {}
for employee in employees:
    if employee[2] == "IT":
        print("Employee ID:", employee[0] , " belongs to IT department")
    total += employee[3]
    if employee[3] > highestSalary:
        highestSalary = employee[3]
        highestSalaryID = employee[0]
    if employee[2] not in unique:
        unique.add(employee[2])
        count[employee[2]] = 1
    else:
        count[employee[2]] += 1
    employeeID[employee[0]] = employee #retrieve by employee id

avg = total/len(employees)
print("\nAverage salary:", avg)
print("\nHighest salary ID:", highestSalaryID, "with salary: ", highestSalary)
print("\nDepartments: ", unique)
print("\nemployee count in each depart: ", count)
print("\nEmployee ID: ", employeeID)