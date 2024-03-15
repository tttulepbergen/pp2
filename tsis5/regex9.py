#Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(s):
    strings = re.findall('[A-Z][^A-Z]*', s)  
    spaces = ' '.join(strings) 
    return spaces

input_string = input("Enter a CamelCase string: ")

spaced_string = insert_spaces(input_string)
print("String with spaces:", spaced_string)
