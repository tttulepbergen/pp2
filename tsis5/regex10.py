#Write a Python program to convert a given camel case string to snake case.

import re

def camtelosnake(s):
    camel = re.findall('[A-Za-z][^A-Z]*', s) # to split string at capital letters
    snake = '_'.join(camel).lower() # convert to lowercase from underscores Полученные подстроки объединяются с символами подчеркивания.
    return snake

# Take input from the user
input_string = input("CamelCase string: ")

# Call the function and print the result
snake_case_string = camtelosnake(input_string)
print("Snake case:", snake_case_string)
