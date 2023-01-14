import random
from hangman_words import *
from hangman_art import *
import os

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#print(f"TEST: word is {chosen_word}")
display = ["_" for i in range(word_length)]
lives = 6
end = False

#The game:
while not end :
    guess = input("\nGuess a letter: ").lower()
    os.system('cls')
    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
              if display[i] == guess:
                print(f"\nYou have alraeady guessed '{guess}' 🤔")
              else:
                display[i] = guess

    else:
        print(f"\n'{guess}' is not in the word .. You lose a life 👎😥")
        lives-=1

    print(f"\n{' '.join(display)}\n")
    print(hangman_stages[6-lives])

    if lives == 0 :
      print(f"\nThe word is '{chosen_word}'")
      print("\n *** YOU LOSE ***")
      end = True

    if "_" not in display:
      print(f"\nThe word is '{chosen_word}'")
      end = True
      print("\n *** Congratulations YOU WIN !! ***")
