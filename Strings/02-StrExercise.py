"""Reverse Uppercase Name.
Create a program that allows the user to enter their name
and then displays the user´s name backwards using only uppercase letters.
Hint: remember that when entering the name, the user can type uppercase or lowercase letters."""

name = str.upper(input("Enter your name:"))

print(name[::-1])

""" 
The syntax [start:stop:step] is used to create a slice of the sequence
What's special about [::] is that it takes all values of the sequence. 
When you use [::-1], the start and stop are blank, indicating that you're taking all elements of the sequence, 
but the step is set to -1, which means you're traversing the sequence from back to front."""