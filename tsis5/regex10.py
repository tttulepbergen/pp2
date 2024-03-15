#Write a Python program to convert a given camel case string to snake case.

import re

def camtelosnake(s):
    camel = re.findall('[A-Za-z][^A-Z]*', s) 
    snake = '_'.join(camel).lower() 
    return snake

input_string = input("CamelCase string: ")

snake_case_string = camtelosnake(input_string)
print("Snake case:", snake_case_string)
