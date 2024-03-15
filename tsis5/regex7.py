#Write a python program to convert snake case string to camel case string.

def stoc(s):
    words = s.split('_')  
    cap_words = [words[0]] + [word.capitalize() for word in words[1:]]  
    camel_case = ''.join(cap_words)  
    return camel_case

input_snake_case = input("Enter a snake_case string: ")

camel_case_string = stoc(input_snake_case)
print("CamelCase:", camel_case_string)
