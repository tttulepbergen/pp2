#Write a Python program with builtin function that accepts a string
#and calculate the number of upper case letters and lower case letters

user_input = input()

lower=0
upper = 0

for char in user_input:  
    if char.isupper():   
        upper += 1
    elif char.islower():
        lower += 1

print(lower, upper)

