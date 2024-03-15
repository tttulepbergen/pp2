#Write a Python program to delete file by specified path.
#Before deleting check for access and whether a given path exists or not.

import os

path = r'C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function'

os.chdir(path)
dirctr = os.listdir(os.getcwd()) 

for i in dirctr: 
    if os.path.isdir(i): 
        print(f'dir: {i}')  
    elif os.path.isfile(i):  
        print(f'file: {i}') 

name = input() 
os.remove(name) 

