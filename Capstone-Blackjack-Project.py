
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:

    your_first_hand = [random.choice(cards) for _ in range(2)]
    sum_of_your_hands = sum(your_first_hand)

    print(f"    Your cards: {your_first_hand}, current score: {sum_of_your_hands}")

    computer_first_hand = [random.choice(cards) for card in range(2)]
    sum_of_comp_hand = sum(computer_first_hand)

    print(f"Computer's first card: {computer_first_hand[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'n':
        print(f"    Your final score: {sum_of_your_hands}")
        print(f"    Computer final score: {sum_of_comp_hand}")
        if sum_of_your_hands > 21:
            print("You went over. You lose")
        elif sum_of_comp_hand > 21:
            print("Computer went over. You win")
        elif sum_of_your_hands == sum_of_comp_hand:
            print("It's a draw")
        elif (21 - sum_of_your_hands) < (21 - sum_of_comp_hand):
            print("You win")
        else:
            print("You lose")
            
        print("-----------------------------")

        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_again != 'y':
            break


    elif another_card == 'y':
        your_final_hand = ([random.choice(cards) for _ in range(1)])
        your_cards = your_first_hand + your_final_hand

        sum_of_your_final_score = sum(your_cards)

        computer_final_hand = ([random.choice(cards) for _ in range(1)])
        computer_cards = computer_first_hand + computer_final_hand
        
        sum_of_computer_final_score = sum(computer_cards)

        print(f"    Your final hand: {your_cards}, final score: {sum_of_your_final_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {sum_of_computer_final_score}")

        if (sum_of_your_final_score > 21):
            print(f"You went over. You lose")

        elif (21 - sum_of_your_final_score) < (21 - sum_of_computer_final_score):
            print("You win")
        elif (sum_of_your_final_score) == (sum_of_computer_final_score):
            print("It's a draw")

        print("______________________________")

        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_again != 'y':
            break


    




