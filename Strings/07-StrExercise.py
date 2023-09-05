"""Counting Spaces and Vowels. Given a string with a sentence entered by the user (including white spaces), count:

1. How many white spaces are in the sentence.
2. How many times the vowels a, e, i, o, u appear."""


sentence = str.lower(input("Enter a sentence: ")) #input converted to lowercase to count all vowels
a = sentence.count("a")
e = sentence.count("e")
i = sentence.count("i")
o = sentence.count("o")
u = sentence.count("u")

vowelsTotal = a + e + i + o + u

space = 0
for char in sentence:
    if char.isspace():
        space += 1

print(f"Total of vowels: {vowelsTotal}\nOccurrence of vowels: \na = {a} \ne = {e} \ni = {i} \no = {o} \nu = {u}")
print("Total of whitespaces =", space)


print('__' * 50)


# chat GPT answer

# # Get input from the user
# sentence = input("Please enter a sentence: ")

# Initialize counters
space_count = 0
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Iterate through the characters in the sentence
for char in sentence:
    if char.isspace():
        space_count += 1
    elif char.lower() in vowel_count:
        vowel_count[char.lower()] += 1

# Print the results
print("Number of white spaces in the sentence:", space_count)

print("Occurrences of vowels:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
