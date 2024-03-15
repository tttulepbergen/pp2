#task1
#generator

def ngen(N):
    i = 0
    while True:      #continues to return until the sq of N
        yield i*i
        if i == N:
            break
        else:
            i += 1
    
    
N = int(input())
print(*ngen(N))


#task2
#Write a program using generator to print the even numbers 
#between 0 and n in comma separated form 
#where n is input from console.

def evenums(n):
    nums = 0
    while True:
        if (nums % 2) == 0:
            yield nums
        if nums == n:   #endpoint
            break
        else: nums += 1

n = int(input())
print(*evenums(n), ' ')


#task3
#Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, 
#between a given range 0 and n.

def threefour(n):
    i = 0
    while True:
        if (i % 3 == 0) and (i % 4 == 0):
            yield i
        if i == n:
            break
        else: i += 1

n = int(input())
print(*threefour(n), ' ')


#task4
#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
#Test it with a "for" loop and print each of the yielded values.

a = int(input())
b = int(input())

def squares(a, b):
    for i in range(a, b+1):  
        yield i**2

print(*squares(a, b), ' ')


#tasj5
#Implement a generator that returns all numbers from (n) down to 0.

def retrn(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in retrn(n):
    print(i)





