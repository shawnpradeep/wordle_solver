import pandas as pd

# Possible wordle word solutions, data frame
DF_VALID_SOLUTIONS = pd.read_csv("data/valid_solutions.csv")
DF_VALID_GUESSES = pd.read_csv("data/valid_guesses.csv")

# '$' = green tile
# 'Y' = yellow tile
# 'G' = grey tile

incomplete_word = "ab__k"

guess_word = "poopy"
guess_tile_color= "$$GGY" 

list_of_grey = list()

df = DF_VALID_SOLUTIONS

# Method will filter out all the words with GRAY letters (i.e. letter not in the word at all)
def grey_filter(letters):
    for letter in letters:
        df = df[~(df['word'].str.contains(letter))]

# Method will filter out all the words without the GREEN letters (i.e. right letter, right position)
def green_filter(incomplete_word):
    for index in range(len(incomplete_word)):
        if(incomplete_word[index] == '_'):
            pass
        else:
            # Aquire words that have the letters in them (in the correct position)
            df = df[df['word'].str.contains('^a...y$', regex = True)]


# Generates the regular expression to be used in @green_filter method.
def reg_expression_generator(incomplete_word):
    reg_expression = "^"

    for ch in incomplete_word:
        if ch == '_':
            reg_expression += '.'
        else:
            reg_expression += ch
    
    reg_expression += '$'

    return reg_expression

# Updates the list of grey letters, incomplete_word variable*****
def update_memory(guess_word, list_of_grey, guess_tile_color):
    incomplete_word = ""
    for i, ch in enumerate(guess_word):
        if (guess_tile_color[i] == '$'):
            incomplete_word[i] = ch
        elif (guess_tile_color[i] == 'G'):
            list_of_grey.append(ch)
            incomplete_word[i] = '_'
        else:
            print("yellow logic not yet implemented")
            incomplete_word[i] = '_'

# Checks inputs to see if the user formatted them correctly
def is_valid_input(guess_word, guess_tile_color):
    if (len(guess_word) != 5 or len(guess_tile_color) != 5):
        return False

    for ch in guess_word:
        if (ch not in "abcdefghijklmnopqrstuvwxyz"):
            return False
    
    for ch in guess_tile_color:
        if (ch not in "$GY"):
            return False
    
    return True

