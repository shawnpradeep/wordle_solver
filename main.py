import pandas as pd
import methods.filters as filters
import methods.wordle_functions as wf


# Possible wordle word solutions, data frame
DF_VALID_SOLUTIONS = pd.read_csv("data/valid_solutions.csv")
DF_VALID_GUESSES = pd.read_csv("data/valid_guesses.csv")

# '$' = green tile
# 'Y' = yellow tile
# 'G' = grey tile

# incomplete_word = ""
guess_word = ""
guess_tile_color= "" 
game_end = False


df = DF_VALID_SOLUTIONS

wf.introduction()
wf.instructions()
# wf.suggested_first_guess()

while(not game_end):
  if (len(df.index) == 1):
    print("\n\033[93mThe answer for today's wordle is: " + df.loc[0].at['word'] + "\033[0m")
    game_end = True
    break
  
  guess_word = input("\033[1mWhat was you're guess?\033[0m ")  
  guess_word = guess_word.lower()
  if guess_word  == "stop":
    game_end = True
    print("\n\033[91mTERMINATING PROGRAM...\033[0m")
    break 
    
  guess_tile_color = input("\033[1mWhat were the tile colors? ($ = green, G = grey, Y = yellow)\033[0m ")
  if guess_tile_color == "stop":
    game_end = True
    print("\n\033[91mTERMINATING PROGRAM...\033[0m")
    break

  if wf.is_valid_input(guess_word, guess_tile_color):
    df = filters.filterData(df, guess_word, guess_tile_color)
    df.index = range(len(df))
    print("")
    print(df)