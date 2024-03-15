#task1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#task2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#task3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#task4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#task5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Examples
#1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#4
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#5
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#6
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#7
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#8
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#9
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#10
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#11
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#12
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#13
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#14
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#15
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)


