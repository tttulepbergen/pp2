#Write a Python program to copy the contents of a file to another file

import os

path = r'C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function'
os.chdir(path)

txt = input() 
path2 = input()  
txt2 = input()   

with open(txt,'r') as input, open(path2 + txt2,'a') as output:
    for line in input:  
        output.write(line) 