students = []
num = int(input("Number of students: "))
subj = int(input("Number of subjects: "))
for i in range(num):
    name = input("Enter Name: ")
    marks = []
    for j in range(subj):
        mark = int(input("Enter marks: "))
        marks.append(mark)
    students.append([name, marks])
average = []
highest= 0
highest_student =""

print("Students with avg abve 50")
for student in students:
    avg = sum(student[1]) / subj
    average.append(avg)
    if avg > highest:
        highest = avg
        highest_student = student[0]
    if avg > 50:
        print(student, avg)
print("Highest performing student: ",  highest_student,  "with average: ", highest)


