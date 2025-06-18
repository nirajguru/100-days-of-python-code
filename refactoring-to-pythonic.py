# Exercise 1: Loop Refactoring
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n * n)    
print(squares)
    
# Refactored Exercise 1- Loop Refactoring > List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [ n*n for n in numbers]
print(squares)


#  Exercise 2: Loop with Index
items = ['a', 'b', 'c']
for i in range(len(items)):
    print(i, items[i])

    
#  Refactored Exercise 2: Loop with Index > Enumerate

items = ['a', 'b', 'c']
for i, item in enumerate(items):
    print(i, item)
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# enumerate() is the canonical way to iterate with index in Python.


# Exercise 3: Swap Variables
x = 10
y= 20
temp = x
x = y
y = temp
print(x, y)

# Refactored Exercise 3: Swap Variables
x, y = y, x
print(x, y)
#

