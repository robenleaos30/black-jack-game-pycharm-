from art import logo
print(logo)
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'It a draw.'
    elif computer_score == 21:
        return 'Computer has a black-jack.You lose!'
    elif user_score == 21:
        return 'You has a black-jack.You win!'
    elif user_score > 21:
        return 'You lose!You have greather than 21 number.'
    elif computer_score > 21:
        return 'You win!Computer have greather than 21 number.'
    elif user_score > computer_score:
        return 'You win!'
    elif user_score < computer_score:
        return 'You lose!'
def play_game():
    def deal_card():
        return random.choice(cards)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        def calculate_score(cards):
            if sum(cards) == 21 and len(cards) == 2:
                return 0
            if 11 in cards and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)
                return sum(cards)
            return sum(cards)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your score is {user_cards},current score {user_score}")
        print(f"Computer score is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("You put another card, y or n\n")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final cards is {user_cards},final score {user_score}.")
    print(f"Computer final cards is {computer_cards},final score {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play another game? y or n\n") == 'y':
    play_game()
else:
    print('Thanks for playing the game.')