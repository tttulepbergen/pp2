#Write a Python program with builtin function 
#that checks whether a passed string is palindrome or not.

str_input = input()
rts = str_input[::-1] 
if str_input == rts:  
    print("Palindrome")
else:
    print("Not Palindrome")


