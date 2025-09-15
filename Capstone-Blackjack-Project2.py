
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_cards(number_of_cards):
    return [random.choice(cards) for _ in range(number_of_cards)]

def calculate_score(cards_list):
    score = sum(cards_list)

    # Covert Ace from 11 to 1 if score is over 21

    while score > 21 and 11 in cards_list:
        cards_list[cards_list.index(11)] = 1
        score = sum(cards_list)
    return score

def win_or_lose(your_score, computer_score):
    if your_score > 21:
        print(f"You lose \U0001F622 ")
    elif computer_score > 21:
        print(f"You win \U0001F604")
    elif your_score <= 21 and computer_score <= 21:
        if (21 - your_score) < (21 - computer_score):
            print(f"You win \U0001F604")

        elif (21 - your_score) > (21 - computer_score):
            print("You lose \U0001F622")

        elif your_score == computer_score:
            print(f"It's a draw \U0001F610")

def ask_to_play_again():
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    return play_again == 'y'
           


while True:

    your_first_hand = pick_cards(2)
    sum_of_your_hands = calculate_score(your_first_hand)

    print(f"    Your cards: {your_first_hand}, current score: {sum_of_your_hands}")

    computer_first_hand = pick_cards(2)
    sum_of_comp_hand = calculate_score(computer_first_hand)

    print(f"    Computer's first card: {computer_first_hand[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if another_card == 'n':
        print(f"    Your final score: {sum_of_your_hands}")
        print(f"    Computer final score: {sum_of_comp_hand}")
        win_or_lose(sum_of_your_hands, sum_of_comp_hand)
            
        print("-----------------------------------------------")       

        if not ask_to_play_again():
            break


    elif another_card == 'y':
        your_final_hand = pick_cards(1)
        your_cards = your_first_hand + your_final_hand

        sum_of_your_final_score = sum(your_cards)

        computer_final_hand = pick_cards(1)
        computer_cards = computer_first_hand + computer_final_hand
        
        sum_of_computer_final_score = sum(computer_cards)

        print(f"    Your final hand: {your_cards}, final score: {sum_of_your_final_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {sum_of_computer_final_score}")

        win_or_lose(sum_of_your_final_score, sum_of_computer_final_score)

        print("________________________________________________")

        if not ask_to_play_again():
            break