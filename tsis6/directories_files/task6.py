#Write a Python program to generate 26 text files
#named A.txt, B.txt, and so on up to Z.txt

import os

path = r'C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function'
os.chdir(path)

for i in range(65, 91): 
    res = open(chr(i)+'.txt', 'w')   
