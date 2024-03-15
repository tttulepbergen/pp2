#Write a Python program to split a string at uppercase letters.

def split_up(s):
    strings = []  
    index = 0  
    
    for i in range(1, len(s)):  
        if s[i].isupper():
            strings.append(s[index:i])
            index = i  
    
    strings.append(s[index:]) 
    
    return strings

input_string = input("Enter a string to split at uppercase letters: ")

split_strings = split_up(input_string)
print("Split strings:", split_strings)
