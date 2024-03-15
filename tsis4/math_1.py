#task1
#Write a Python program to convert degree to radian.

import math

n = int(input())

print(math.radians(n))


#task2
#Write a Python program to calculate the area of a trapezoid.

h = float(input())
a = float(input())
b = float(input())

area = 0.5*((a + b)*h)   #Calculate the area of the trapezoid

print("area:", area)   #Print the result


#task3
#Программа для вычисления площади правильного многоугольника

import math

n = int(input())
s = float(input())

area = (n * s**2) / (4 * math.tan(math.pi/n))

print("area", area)


#task4
#Write a Python program to calculate the area of a parallelogram.

import math

b = float(input())
h = float(input())

area = b * h

print("area", area)








