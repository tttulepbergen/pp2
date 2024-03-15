#1.Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s
import re

txt = input()
x = re.findall(r'ab*', txt)
print(x)


#2.Write a Python program that matches a string that has an "a" followed by two to three "b".

import re

txt = input()
x = re.findall(r'ab{2,3}', txt)
print(x)


#3.Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

txt = input()
x = re.findall(r'[a-z]+_[a-z]+', txt)
print(x)


#4.Write a Python program to find the sequences of one upper case
#letter followed by lower case letters.
import re

txt = input()
x = re.findall(r'[A-Z][a-z]+', txt)
print(x)


#5.Write a Python program that matches a string that has an 'a' followed by anything, 
#ending in 'b'.

import re

txt = input()
x = re.findall(r'a.*b$', txt)
print(x)


#6.Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

txt = input()
y = re.compile(r'[ ,.]')
x = re.sub(y, ":", txt)
print(x)


#7.Write a python program to convert snake case string to camel case string.
txt = input()

def snake_to_camel(txt):
    temp = txt.split('_')
    return temp[0] + ''.join(ele.title() for ele in temp[1:])

print(snake_to_camel(txt))

#8.Write a Python program to split a string at uppercase letters.
import re

txt = input()
x = re.findall("[A-Z][a-z]*", txt)
print(x)


#9.Write a Python program to insert spaces between words starting with capital letters.

import re

def insert_spaces(s):
    strings = re.findall('[A-Z][^A-Z]*', s) #for splitting string at capital letters
    
    spaces = ' '.join(strings) #join the split strings with spaces
    
    return spaces


#10.Write a Python program to convert a given camel case string to snake case.
import re

def camtosnake(s):
    camel = re.findall('[A-Za-z][^A-Z]*', s) 
    snake = '_'.join(camel).lower() 
    
    return snake