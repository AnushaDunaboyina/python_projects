import random

print("Welcome to the Number Guessing Game!")

def easy_or_hard():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5

def game_condition(num, original_number):

        if num == original_number:
            print("Number matched, You win! \U0001F604")
            return True

        elif num > original_number:
            print("Too high.")
        
        elif num < original_number:
            print("Too low.")
        return False

def play_again():
     play_again = input("Play again 'y' or 'n': ").lower()
     if play_again == 'y':
          return True

while True:
    original_number = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")

    for i in range(easy_or_hard(), 0, -1):
        
        print(f"You have {i} attempts remaining to guess the number.")
        num = int(input("Make a guess: "))

        if game_condition(num, original_number):
            break
        if i == 1:
            print(f"You've run out of guesses. Number is {original_number}. You lose. \U0001F622")

    # Ask to play again after game ends
    if not play_again():
        break



    