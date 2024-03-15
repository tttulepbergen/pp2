#Write a Python program to split a string at uppercase letters.

def split_up(s):
    strings = []  # an empty list to store strings
    index = 0  # pointer -> first char of split string
    
    for i in range(1, len(s)):  # iterate over the characters
        if s[i].isupper():
            strings.append(s[index:i])
            index = i  # start index to current char
    
    strings.append(s[index:])  # last split string to the list
    
    return strings

# Take input from the user
input_string = input("Enter a string to split at uppercase letters: ")

# Call the function and print the result
split_strings = split_up(input_string)
print("Split strings:", split_strings)
