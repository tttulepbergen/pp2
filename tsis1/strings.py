#task1
x = "Hello World"
print(len(x))

#task2
txt = "Hello World"
x = txt[0]

#task3
txt = "Hello World"
x = txt[2:5]

#task4
txt = " Hello World "
x = "txt.strip()"

#task5
txt = "Hello World"
txt = txt.upper()

#task6
txt = "Hello World"
txt = txt.lower()

#task7
txt = "Hello World"
txt = txt.replace("H", "J")

#task8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#Examples
#1
print("Hello")
print('Hello')

#2
a = "Hello"
print(a)

#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#5
a = "Hello, World!"
print(a[1])

#6
for x in "banana":
  print(x)

#7
a = "Hello, World!"
print(len(a))

#8
txt = "The best things in life are free!"
print("free" in txt)

#9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#10
txt = "The best things in life are free!"
print("expensive" not in txt)

#11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#12
b = "Hello, World!"
print(b[2:5])

#13
b = "Hello, World!"
print(b[:5])

#14
b = "Hello, World!"
print(b[2:])

#15
b = "Hello, World!"
print(b[-5:-2])

#16
a = "Hello, World!"
print(a.upper())

#17
a = "Hello, World!"
print(a.lower())

#18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#19
a = "Hello, World!"
print(a.replace("H", "J"))

#20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#21
a = "Hello"
b = "World"
c = a + b
print(c)

#22
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#23
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#26
txt = "We are the so-called \"Vikings\" from the north."

#27
txt = "We are the so-called "Vikings" from the north."
