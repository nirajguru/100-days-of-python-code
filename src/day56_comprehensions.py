#CODE1: Create a list with various elements and then define a list comprehension that filters on it
my_fruits_list = ["banana", "oranges", "grapes"]

yellow_fruit = [fruit for fruit in my_fruits_list if fruit == "banana"]

print(yellow_fruit)

#CODE2: Create a list with various names and then define a set comprehension that filters on it

my_fruits_list = ["banana", "oranges", "grapes"]
my_fruits_set = {fruit for fruit in my_fruits_list if fruit == "oranges"}
print(my_fruits_set)

#CODE3: Create a dict of square roots and then iterate of the items printing out each key-value pair
square_roots = {x: (x**0.5) for x in range(1,20)}
print(square_roots)
print(type(square_roots))

