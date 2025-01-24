# Rock Paper Scissors game
# Rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

sign = {"rock" : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
"paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
"scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

winning_combination_dict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
winning_combination_tuple = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

def display(user, computer):
    if user in list(sign.keys()):
        print(f"Your choice: {user}\n{sign[user]}")
        print(f"Computer choice: {computer}\n{sign[computer]}")
        return 1
    else:
        return 0


def result_using_dictionary(u, c):
    # Pros: For rock paper scissors game dictionary based approach is good because there one-to-one relationship in winning combination.
    # Cons: It is not scalable because if we want to extend this game (ex. rock paper scissors lizard spock)
    if u == c:
        print("Game Draw!")
    elif winning_combination_dict[u] == c:
        print("You Win!")
    else:
        print("Computer Wins!")


def result_using_tuple(u1,c1):
    # Pros: It is simple and easy to extend approach. We can easily add new rules in the list of tuples
    if u1==c1:
        print("Game Draw!")
    elif (u1, c1) in winning_combination_tuple:
        print("You Win!")
    else:
        print("Computer Wins!")


if __name__ == "__main__":
    user_choice = input("What do you choose? Rock, Paper and Scissors: ").lower()
    computer_choice = random.choice(list(winning_combination_dict.keys()))
    if display(user_choice, computer_choice):
        #result_using_dictionary(user_choice, computer_choice)
        result_using_tuple(user_choice, computer_choice)
    else:
        print("Invalid Choice!")
