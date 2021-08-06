import random
import string

def hangman():
  fruits = ['apple', 'banana', 'guava', 'grape', 'orange', 'papaya', 'mango', 'lychee']
  word = random.choice(fruits)
  validLetters = string.ascii_letters
  turns = 10
  guessmade = ''

  while len(word) > 0:
    main = ''

    for letter in word:
      if letter in guessmade:
        main = main + letter
      else:
        main = main + "_" + " "
    
    if main == word:
      print(main)
      print("You won!")
      break

    print("Guess the word: ", main)
    guess = input()

    if guess in validLetters:
      guessmade = guessmade + guess
    else:
      print("Enter a valid character")
      guess = input()
    
    if guess not in word:
      turns = turns - 1
      if turns == 1:
        print(f"{turns} turn left. Last chance")
      elif turns==0:
        print("You lost the game.\nBye!")
        break
      else:
        print(f"{turns} turn left")


name = input("Enter your name: ")
print(f"Hello {name}! \nWelcome in Hangman game.")
print()
print("=====================****=========================")
print("Try to guess the words in less than 10 attempts.")
print("Hint: Guess the words from fruits name")
print("=====================****=========================")
print()
hangman()
