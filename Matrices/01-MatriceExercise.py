"""
Build a 3x3 matrix by asking the user for its elements, and in the end, you should present:

1- The sum of all elements in the matrix.
2- The largest and smallest element in the matrix.
3- The average of the elements in the matrix.
4- The sum of the elements in the main diagonal.
"""

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
i = 0
j = 0
sum = 0
sumd = 0
average = 0
largest = 0
smallest = 0

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f"Enter the {[i]} {[j]} element for the matrix: "))

        sum += matrix[i][j]

        if smallest == 0: smallest = matrix[i][j]

        elif matrix[i][j] < smallest: smallest = matrix[i][j]

        if matrix[i][j] > largest: largest = matrix[i][j]

average = sum / 9

sumd = matrix[0][0] + matrix[1][1] + matrix[2][2]

print("The sum of all elements is: ", sum)
print("The largest element in the matrix is: ", largest)
print("The smallest element in the matrix is: ", smallest)
print("The average of the elements in the matrix is: ", average)
print("The sum of the elements in the main diagonal is: ", sumd)