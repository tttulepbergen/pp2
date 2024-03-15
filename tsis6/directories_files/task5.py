#Write a Python program to write a list to a file.

import os

path = r'C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function'

os.chdir(path)
txt = input()

output = open(txt, 'w') 
output.write(str(list(map(int, input().split()))))  
output.close()  


