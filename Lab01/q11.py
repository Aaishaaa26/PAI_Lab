subj1 = int( input("Enter Marks In subj1:"))
subj2 = int( input("Enter Marks In subj2:"))
subj3= int( input("Enter Marks In subj3:"))
marks = {"subject1": subj1, "subject2": subj2, "subject3": subj3}
avg = sum(marks.values())
avg = avg/3
print("Average Marks:", avg)

percentage = (sum(marks.values()) / 300 ) * 100
print ("Total percentage: " , percentage, "%" )
