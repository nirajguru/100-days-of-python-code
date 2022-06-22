import random

#1 means Heads 0 means Tails

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")