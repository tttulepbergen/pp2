#task1
print(10 > 9)

#task2
print(10 == 9)

#task3
print(10 < 9)

#task4
print(bool("abc"))

#task4
print(bool(0))


#Examples
#1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#3
print(bool("Hello"))
print(bool(15))

#4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7
class myclass():
      def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8
def myFunction() :
      return True

print(myFunction())

#9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#10
x = 200
print(isinstance(x, int))


