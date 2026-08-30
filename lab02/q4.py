courseA = set()
courseB = set()
num = int(input("Enter number of students in A: "))
for i in range(num):
    idz = input("Enter student id: ")
    courseA.add(idz)
num = int(input("Enter number of students in B: "))
for i in range(num):
    idz = input("Enter student id: ")
    courseB.add(idz)

print("\nStudents in all courses: ", courseA.union(courseB))
print("\nStudents in both courses:", courseA.intersection(courseB))
print("\nStudents only in Course A:", courseA.difference(courseB))
print("\nStudents only in Course B:", courseB.difference(courseA))