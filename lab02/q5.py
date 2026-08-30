employee = {}
num = int(input("Enter number of employees: "))
for i in range(num):
    idz = int(input("Enter id: "))
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))
    job_title = input("Enter job title: ")
    employee[idz] = [name, department, salary, job_title]

searchID = int(input("\nEnter search ID: "))
if searchID in employee:
    print(employee[searchID])
else:
    print("\nEmployee not found")

idz = int(input("\nEnter employee id to update salary: "))
if idz in employee:
    salary = int(input("Enter salary: "))
    employee[idz][2] = salary

idz = int(input("enter new employee id: "))
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = int(input("Enter salary: "))
job_title = input("Enter job title: ")
employee[idz] = [name, department, salary, job_title]

idz = int(input("\nEnter employee id to remove: "))
if idz in employee:
    del employee[idz]
print("All employees: ")
for i in employee:
    print(i, employee[i])