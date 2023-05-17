from random import randint

select = ["Rock", "Paper", "Scissors"]
pick = select[randint(0,2)]


Player = False

while Player == False:
    player = input("Enter your choice (Rock, Paper, Scissors), or enter 'quit' to stop: ")

    if player == "quit":
        break

    while player in select:
        if player == pick:
            print(f"Tie the computer picked {pick}")
            break
        elif player == "Rock":
            if pick == "Paper":
                print(f"You lose the computer picked {pick}")
                Player = True
                break
            else:
                print(f"You win the computer picked {pick}")
                Player = True
                break
        elif player == "Paper":
            if pick == "Scissors":
                print(f"You lose the computer picked {pick}")
                Player = True
                break
            else:
                print(f"You win the computer picked {pick}")
                Player = True
                break
        elif player == "Scissors":
            if pick == "Rock":
                print(f"You lose the computer picked {pick}")
                Player = True
                break
            else:
                print(f"You win the computer picked {pick}")
                Player = True
                break
