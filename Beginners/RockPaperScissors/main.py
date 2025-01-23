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

winning_combo = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def display(user, computer):
    if user in list(sign.keys()):
        print(f"Your choice: {user}\n{sign[user]}")
        print(f"Computer choice: {computer}\n{sign[computer]}")
        return 1
    else:
        return 0


def result(u, c):
    if u == c:
        print("Game Draw!")
    elif winning_combo[u] == c:
        print("You Win!")
    else:
        print("Computer Wins!")


if __name__ == "__main__":
    user_choice = input("What do you choose? Rock, Paper and Scissors: ").lower()
    computer_choice = random.choice(list(winning_combo.keys()))
    if display(user_choice, computer_choice):
        result(user_choice, computer_choice)
    else:
        print("Invalid Choice!")
