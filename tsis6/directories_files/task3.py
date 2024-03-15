#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.

import os
path = r'C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function'

os.chdir(path)
    
print(os.getcwd())  

dirctr = os.listdir(os.getcwd())  
for i in dirctr:
    if os.path.isdir(i):
        print(i)
    elif os.path.isfile(i):
        print(i)