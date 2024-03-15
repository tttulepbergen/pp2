#Write a Python program to count the number of lines in a text file.

import os

path = r'C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function'
os.chdir(path)
txt = input()  

result = open(txt, 'r') 
cnt = 0 

for str in result: 
    if str != "\n":  
        cnt += 1  
        print(cnt)  


