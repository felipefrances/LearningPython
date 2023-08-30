"""String Lengths.
Create a program that reads 2 strings and reports their contents followed by their length.
Also, indicate whether the two strings have the same length and if they are equal or different in content."""

content1 = str(input("Write the first content: "))
content2 = str(input("Write the second content: "))

print(content1, len(content1))
print(content1, len(content2))


if len(content1) == len(content2):
    print("The contents have the same length")
else:
    print("The contents haven't the same length")

if content1 == content2:
    print("The contents are equals")
else:
    print("The contents are different")

