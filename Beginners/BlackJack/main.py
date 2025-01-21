import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

cards = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
         'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


def calculate_score(input_list):
    score = 0
    ace_count = input_list.count('Ace')

    for j in input_list:
        score += cards[j]

    while ace_count != 0 and score > 21:
        score -= 10
        ace_count -= 1

    return score


user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(random.choice(list(cards.keys())))
    computer_cards.append(random.choice(list(cards.keys())))

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"User cards : {user_cards} and score is {user_score}")
print(f"Computer cards : {computer_cards} and score is {computer_score}")

pick_card = True

while pick_card:
    user_choice = input("Enter 'Hit' or 'Stand': ")

    if user_choice.lower() == 'hit':
        user_cards.append(random.choice(list(cards.keys())))
        user_score = calculate_score(user_cards)
        print(f"User cards : {user_cards} and score is {user_score}")

        if user_score > 21:
            pick_card = False
            print("User bust")

    else:
        pick_card = False

if user_score < 22:
    while computer_score < 18:
        computer_cards.append(random.choice(list(cards.keys())))
        computer_score = calculate_score(computer_cards)

    print(f"User cards : {user_cards} and score is {user_score}")
    print(f"Computer cards : {computer_cards} and score is {computer_score}")

    if computer_score > 21:
        print("Computer bust")

    else:
        if user_score > computer_score:
            print("User Win")
        elif computer_score > user_score:
            print("Computer Win")
        else:
            print("Game draw")
