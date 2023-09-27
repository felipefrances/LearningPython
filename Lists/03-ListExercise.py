# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

gradeList = []
avg = 0

for i in range(4):
    grade = float(input(f"Enter the {i+1} grade: "))
    gradeList.append(grade)

    avg += grade

for i in range(4):
    print(gradeList[i])

print("Average grade is:", avg/4)



