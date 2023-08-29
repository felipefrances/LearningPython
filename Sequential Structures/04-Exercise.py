# Make a program that asks for 4 grades and shows the average.

grade1 = float(input("Enter the student´s 1st grade: "))
grade2 = float(input("Enter the student´s 2nd grade: "))
grade3 = float(input("Enter the student´s 3rd grade: "))
grade4 = float(input("Enter the student´s 4th grade: "))

finalGrade = (grade1 + grade2 + grade3 + grade4) /4

print("Student´s final grade is: ", finalGrade)
