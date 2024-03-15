#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability 
#and executability of the specified path

import os

print('existence: ',os.access('C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function', os.F_OK))
print('readability: ', os.access('C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function', os.R_OK))
print('writability: ', os.access('C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function', os.W_OK)) 
print('executability: ', os.access('C:\Users\Acer\OneDrive\Рабочий стол\pp2\lab6_pp2\bultin_function', os.X_OK)) 
