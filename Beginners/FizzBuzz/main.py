# FizzBuzz Code challenge
# Rules:
# Print numbers from 1 to 100.
# If number is divisible by 3 is replaced with "Fizz".
# If number divisible by 5 is replaced with "Buzz".
# If number divisible by both 3 and 5 is replaced with "FizzBuzz".

for i in range(1,101):
    if i%3 == 0:
        if i%5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)