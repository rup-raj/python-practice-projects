import random
import hangman_art
import hangman_words

print(hangman_art.logo)
random_word = random.choice(hangman_words.word_list)
guessed_word = ["_"] * len(random_word)
guessed_letters = set()
lives = 6
game_over = False
print(random_word)

while not game_over:
    guess = input("Guess a letter: ")

    if len(guess)!=1 or not guess.isalpha():
        print("Invalid guess!")
    else:
        if guess in guessed_letters:
            print(f"You have already guessed {guess}, try another one.")
        else:
            guessed_letters.add(guess)
            if guess in random_word:
                print(f"{guess} is present in the word.")
                for i,letter in enumerate(random_word):
                    if letter == guess:
                        guessed_word[i] = guess

                print(f"Your guessed word so far: {"".join(guessed_word)}")
                if "_" not in guessed_word:
                    print(f"============= You guessed {random_word} correctly. You win =============")
                    print(f"============= Your lives balance is {lives}. =============")
                    game_over = True
            else:
                lives -= 1
                print(f"{guess} is not present in the word. You loose one life. lives remains: {lives}")
                print(f"Your guessed word so far: {"".join(guessed_word)}")
                if lives == 0:
                    print("============= Lives are over. You loose =============")
                    game_over = True
            print(hangman_art.stages[lives])
