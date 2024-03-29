# Checks to see if the user input is valid by first checking length, then to see if it is a letter of the alphabet, then if the color combination is comprised of accepted colors.
def is_valid_input(guess_word, guess_tile_color):
  guess_word = guess_word.strip()
  guess_tile_color = guess_tile_color.strip()

  # Length check:
  if (len(guess_word) != 5 or len(guess_tile_color) != 5):
    return False

  # Part of Alphabet Check:
  for ch in guess_word:
      if (ch not in "abcdefghijklmnopqrstuvwxyz"):
        return False

  # Color Code Validity Check:
  for e in guess_tile_color:
     if (e not in "$GY"):
        return False

  return True


# Prints ASCII welcome msg:
def introduction():
  print("\033[92m\033[1m                                                    ")
  print(" _ _ _           _ _        _____     _             ")
  print("| | | |___ ___ _| | |___   |   __|___| |_ _ ___ ___ ")
  print("| | | | . |  _| . | | -_|  |__   | . | | | | -_|  _|")
  print("|_____|___|_| |___|_|___|  |_____|___|_|\_/|___|_|  ")
  print("                                                    \033[0m")


# Outputs instructions to program user:
def instructions():
  print("\n\033[1m1)\033[0m Start a game of wordle in a browser.")
  print("\033[1m2)\033[0m Enter in a guess.")
  print("\033[1m3)\033[0m Enter in the word you guessed and the color sequence into the program.")
  print("\033[1m3a)\033[0m Color sequences must be entered in the following format:")
  print("    \033[92m$ = green tiles\033[0m, \033[93mY = yellow tiles\033[0m, \033[97mG = grey tiles\033[0m")
  print("\033[1m4)\033[0m Repeat with each iteration until you have your answer!\n")