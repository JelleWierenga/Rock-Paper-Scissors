from random import choice
from random import randint

select = ["Rock", "Paper", "Scissors"]
rounds = 1

for _ in range(rounds):
    pick = select[randint(0,2)]
    player = input("Enter your choice (Rock, Paper, Scissors): ")
    
    if player == pick:
        print(f"Tie! The computer picked {pick}")
    elif (
        (player == "Rock" and pick == "Paper") or
        (player == "Paper" and pick == "Scissors") or
        (player == "Scissors" and pick == "Rock")
    ):
        print(f"You lose! The computer picked {pick}")
    else:
        print(f"You win! The computer picked {pick}")
