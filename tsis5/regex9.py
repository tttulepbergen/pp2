#Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(s):
    strings = re.findall('[A-Z][^A-Z]*', s)  # for splitting string at capital letters
    spaces = ' '.join(strings)  # join the split strings with spaces
    return spaces

# Take input from the user
input_string = input("Enter a CamelCase string: ")

# Call the function and print the result
spaced_string = insert_spaces(input_string)
print("String with spaces:", spaced_string)
