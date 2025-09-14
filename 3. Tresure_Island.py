print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
choose1 = input("You're at a cross road. Where do you want to go? \n 'left' or 'right' \n").lower()
if choose1 == "right":
    print("Fall into a hole.\nGame Over.")
else:
    choose2 = input("You've come to a lake. There is an island in the middle of the lake. \n   Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    
    if choose2 == "swim":
        print("Attacked by trout. Game Over")
    else:
        choose3 = input("Which door? \n     'red' , 'blue' or 'yellow'\n").lower()
        
        if choose3 == "blue":
            print("Eaten by beasts. \nGame Over")
        elif choose3 == "red":
            print("Burned by fire. \n Game Over")
        elif choose3 == "yellow":
            print("You win!")
        else:
            print("Game Over.")
        