import random

level = input("Enter level (easy or hard): ").upper()

if level == "EASY":
    attempts = 10
elif level == "HARD":
    attempts = 5
else:
    print("Invalid level")

answer_to_game = random.randint(1, 4)
# print(answer_to_game)  This is the answer and the user wins the game if this matches the user entered number
guessed_number = input("Guess a number: ")

while attempts > 0:
    if answer_to_game == guessed_number:
        print(f"You won! Guessed number is {answer_to_game}")
        break
    else:
        guessed_number = int(input("Guess the number again: "))
        attempts -=1
