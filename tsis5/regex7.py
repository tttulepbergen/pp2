#Write a python program to convert snake case string to camel case string.

def stoc(s):
    words = s.split('_')  # split string into words separated by underscore
    cap_words = [words[0]] + [word.capitalize() for word in words[1:]]  # capitalize first letter of each word except the first one

    camel_case = ''.join(cap_words)  # join the words back together into a single string
    return camel_case

# Take input from the user
input_snake_case = input("Enter a snake_case string: ")

# Call the function and print the result
camel_case_string = stoc(input_snake_case)
print("CamelCase:", camel_case_string)
