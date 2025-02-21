import random
from enum import Enum

line1 = "****************************"
line2 = "   Rock Paper Scissors   "
line3 = "****************************"

print(line1)
print(line2)
print(line3)
print("")

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

player_score = 0
python_score = 0

for i in range(3):
    playerchoice = int(input('''Enter your choice: 
1 for Rock
2 for Paper
3 for Scissors
'''))
    

    if playerchoice < 1 or playerchoice > 3:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue
    
    player = int(playerchoice)
    pythonchoice = random.randint(1, 3)
    
    print(f"\nRound {i+1}:")
    print(f"Your choice: {RPS(player).name}")
    print(f"Python's choice: {RPS(pythonchoice).name}")
    

    if (player == 1 and pythonchoice == 3) or (player == 2 and pythonchoice == 1) or (player == 3 and pythonchoice == 2):
        print("You win this round!")
        player_score += 1
    elif player == pythonchoice:
        print("This round is a draw!")
    else:
        print("Python wins this round!")
        python_score += 1
    print("")


print(f"Your score: {player_score}")
print(f"Python's score: {python_score}")

if player_score > python_score:
    print("Congratulations! You win!")
elif player_score < python_score:
    print("Python wins! Better luck next time.")
else:
    print("It's a tie!")
