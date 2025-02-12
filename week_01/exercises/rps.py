import random
from enum import Enum

line1 = "****************************"
line2 = "   Rock Paper Scissors   "
line3 = "****************************"

print(line1)
print(line2)
print(line3)

print("")

playerchoice = input('''Enter your choice: 
1 for Rock
2 for Paper
3 for Scissors
''')



player = int(playerchoice)

pythonchoice = random.randint(1, 3)

# handle invalid input

if player < 1 or player > 3:
    print("Invalid input. Please enter a number between 1 and 3.")
    exit()

print("")

# add relevent values

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(f"Your choice: {RPS(player).name}")
print(f"Python's choice: {RPS(pythonchoice).name}")


if player == 3 and pythonchoice == 1:
    print("You win!")
elif player == 1 and pythonchoice == 2:
    print("You win!")
elif player == pythonchoice:
    print("Draw!")
else:
    print("You lose!")

print("")

