import random

game = ["rock", "paper", "scissors"]

index = int(input("select 0 for rock, 1 for Paper, 2 for scissors: "))

user = game[index]
print(f"me: {user}")

computer = random.choice(game)
print(f"computer: {computer}")

if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print("You win")
elif (user == "rock" and computer == "rock") or (user == "paper" and computer == "paper") or (user == "scissors" and computer == "scissors"):
    print("tie")
else:
    print("You lose")
   
