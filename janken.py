import random

def janken():
    choices = ["Rock", "Paper", "Scissors"]
    user = input("Rock, Paper, or Scissors? ")
    ai = random.choice(choices)
    print(f"Player: {user}, AI: {ai}")
    if user == ai:
        print("It's a tie.")
    elif (user == "Rock" and ai == "Scissors") or (user == "Scissors" and ai == "Paper") or (user == "Paper" and ai == "Rock"):
        print("You won!")
    else:
        print("You lost...")

if __name__ == "__main__":
    janken()