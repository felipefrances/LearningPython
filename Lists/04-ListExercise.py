# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

myList = []
vocals = 'aeiou'
consonantsCounter = 0

for i in range(10):
    letter = input("Enter a letter: ")
    if letter not in vocals:
        myList.append(letter)


print(len(myList))
print(myList)






