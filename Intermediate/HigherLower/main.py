import random
from gameData import data


game = True
num2 = random.randint(0, len(data)-1)

while game:

    num1 = num2
    while num1 == num2:
        num2 = random.randint(0, len(data)-1)

    option_a = data[num1]
    option_b = data[num2]

    print(f"Option A : {option_a['name']}, {option_a['description']} from {option_a['country']}")
    print("Vs")
    print(f"Option B : {option_b['name']}, {option_b['description']} from {option_b['country']}")

    user_answer = input("Choose your answer 'A' or 'B': ")

    if user_answer.lower() == 'a' and check_answer(option_a, option_b, option_a):
        option_a = option_a

    elif user_answer.lower() == 'b' and check_answer(option_a, option_b, option_b):
        option_a = option_b

    else:
        game = False

