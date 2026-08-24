phy = int( input("ENter Marks In Physics:"))
chem = int( input("ENter Marks In Chemistry:"))
math= int( input("ENter Marks In Maths:"))
marks = {"Physics": phy, "Chemistry": chem, "Maths": math}
avg = sum(marks.values())
avg = avg/3
print("Average Marks:", avg)
highest_marks = 0

for subject in marks:
    if marks[subject] > highest_marks:
        highest_marks = marks[subject]
        highest_subject = subject

print("Subject with highest marks:", highest_subject)