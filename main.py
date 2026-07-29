import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the list of cards."""
    return random.choice(cards)

def calculate_score(card_list):
    """Returns the sum of all cards in a card list as the score. However, in case
    of a blackjack (Ace + 10), where Ace = 11, 0 is returned as the score. If there
    is an Ace (11) in the card list and the total score is above 21, Ace will be
    counted as 1 by removing and replacing 11 with 1."""
    if 11 in card_list and 10 in card_list and len(card_list) == 2:
        return 0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(user_s, computer_s):
    """Returns the result whether the user has won or lost against the computer
    based on their scores."""
    if user_s == computer_s:
        return "You and your opponent have an equal score. It's a draw 🤔"
    elif computer_s == 0:
        return "Your opponent has a Blackjack. You lose 😱"
    elif user_s == 0:
        return "You have a Blackjack. You win 😎"
    elif user_s > 21:
        return "You went over. You lose 😭"
    elif computer_s > 21:
        return "Your opponent went over. You win 😎"
    elif user_s > computer_s:
        return "You win 😃"
    else:
        return "You lose 😭"

def play_game(user_score, computer_score):
    """Blackjack game is played between the user and computer."""
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_choice == 'y':
        print("\n" * 200)
        print(art.logo)

        for card in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        continue_game = False
        while not continue_game:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score == 0 or computer_score == 0 or user_score > 21:
                continue_game = True
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if another_card == 'y':
                    user_cards.append(deal_card())
                else:
                    continue_game = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    else:
        print("\n" * 200)
        play_game(user_score, computer_score)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    play_game(user_score, computer_score)

user_current_score = -1
computer_current_score = -1
play_game(user_score=user_current_score, computer_score=computer_current_score)