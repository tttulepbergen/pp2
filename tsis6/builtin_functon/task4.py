#Write a Python program that invoke square root function 
#after specific milliseconds.

print('Sample Input:')
inp = int(input())
ms = int(input())  
result = abs(ms / 1000)  
print('Sample Output:')
print(f'Square root of {inp} after {ms} milliseconds is {inp**0.5}')
print(f'Absolute value of {ms} / 1000 is {result}')
