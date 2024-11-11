# Author : Nhan Trong Pham
# Email : trongnhanpha@umass.edu
# Spire ID : 34759664



import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(string, words):
    result = []
    for letter in string:
        if letter.isalpha():
            if letter in words:
                result.append(letter)
            else:
                result.append('_')
        else:
            result.append(letter)
    answer = ''.join(result)
    print(answer)

def get_letter(guesses):
  while True:
    letter = input("Please enter a letter: ").upper()
    if letter.isalpha() and letter not in guesses:
       if len(letter) == 1:
          return letter
       else:
          print(f'"{letter}" is not a letter!')
    elif letter in guesses:
      print(f'"{letter}" has already been guessed!')
    else:
      print(f'"{letter}" is not a letter!')

def won(phrase, guesses ):
    for i in phrase :
      if i.isalpha():
        if not i in guesses:
            return False
    return True

def play_game():
    phrase = make_phrase()
    guesses = []
    misses = 0 
    print("*** Welcome to Hangman ***")
    print_gallows(misses)
    while not won(phrase,guesses):
      print_revealed_phrase(phrase, guesses)
      print(f"Letters guessed: {sorted(guesses)}")
      letter = get_letter(guesses)
      guesses.append(letter)

      if letter not in phrase:
          misses += 1
          print_gallows(misses)
          if misses == 6:
              print("Game over!")
              print(f"Solution was: {phrase.upper()}")
              return
    print(phrase)
    print("Congratulations!")





play_game()