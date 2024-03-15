#task1
carname = "Volvo"

#task2
x = 50

#task3
x = 5
y = 10
print(x + y)

#task4
x = 5
y = 10
z = x + y
print(z)

#task5
x, y, z = "Orange", "Banana", "Cherry"

#task6
x = y = z = "Orange"

#task7
def myfunc():
    global x
    x = "fantastic"


#EXAMPLES
#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#4
x = 5
y = "John"
print(type(x))
print(type(y))

#5
x = "John"
# is the same as
x = 'John'

#6
a = 4
A = "Sally"
#A will not overwrite a

#7, Variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#8
2myvar = "John"
my-var = "John"
my var = "John"

#9, Camel case 
myVariableName = "John"

#10, Pascal case
MyVariableName = "John"

#11, Snake case
my_variable_name = "John"

#12, Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#13
x = y = z = "Orange"
print(x)
print(y)
print(z)

#14
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#15, Output Variables
x = "Python is awesome"
print(x)

#16
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#17
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#18
x = 5
y = 10
print(x + y)

#19
x = 5
y = "John"
print(x + y)
#Output: error

#20
x = 5
y = "John"
print(x, y)


#21
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#22
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#23
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)





