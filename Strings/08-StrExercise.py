"""Palindrome.
A palindrome is a sequence of characters that reads the same forward and backward.
For example, "OSSO" and "OVO" are palindromes.
In more complex texts, spaces and punctuation are ignored.
The phrase "SUBI NO ONIBUS" is an example of a palindrome sentence where spaces were ignored.
Create a program that reads a sequence of characters, displays it, and determines if it is a palindrome or not."""

import unicodedata

# Get input from the user
sentence = input("Please enter a sentence: ")

# Remove spaces and punctuation
cleanedSentence = ''.join(char for char in sentence if char.isalnum() or unicodedata.category(char)[0] == 'M')

# Check if the cleaned sentence is a palindrome
if cleanedSentence.lower() == cleanedSentence[::-1].lower():
    print(f'"{sentence}" is a palindrome.')
else:
    print(f'"{sentence}" is not a palindrome.')

print('__' * 50)

# import unicodedata
#
# # Get input from the user
# sentence = input("Please enter a sentence: ")
#
# # Initialize an empty string to store the cleaned sentence
# cleaned_sentence = ""
#
# # Iterate through the characters in the input sentence
# for char in sentence:
#     # Check if the character is alphanumeric or its category starts with 'M'
#     if char.isalnum() or unicodedata.category(char)[0] == 'M':
#         # If it is, add it to the cleaned sentence
#         cleaned_sentence += char
#
# # Check if the cleaned sentence is a palindrome
# if cleaned_sentence.lower() == cleaned_sentence[::-1].lower():
#     print(f'"{sentence}" is a palindrome.')
# else:
#     print(f'"{sentence}" is not a palindrome.')
