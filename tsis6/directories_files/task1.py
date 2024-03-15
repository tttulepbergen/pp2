#выводит список только директорий, файлов и всех директорий и файлов в указанном пути

import os  

path = input()   
os.chdir(path)  

dirctry = os.listdir(os.getcwd())  

for i in dirctry:   
    if os.path.isdir(i):    
        print(i)    
    elif os.path.isfile(i):  
        print(i)  

