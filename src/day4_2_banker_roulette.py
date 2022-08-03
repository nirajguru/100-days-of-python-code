import random
#  write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

person_who_pays_bill = random.choice(names)
print(f"{person_who_pays_bill} is going to buy the meal today!")
