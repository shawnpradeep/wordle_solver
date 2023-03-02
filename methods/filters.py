def filterData(df, userWordInput, userTileInput):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    yellow = list()
    grey = list()
    
    # Create a reg expression for words that have the green spaces correctly placed
    reg_expression = "^"
    for i in range(len(userTileInput)):
        if userTileInput[i] == "Y":
            alphabet = alphabet.replace(userWordInput[i],'')
            reg_expression += '[{}]'.format(alphabet)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            yellow.append(userWordInput[i])
        elif userTileInput[i] == "G":
            #alphabet = alphabet.replace(user_word_input[i],'')
            #reg_expression+='[{}]'.format(alphabet)
            #alphabet = "abcdefghijklmnopqrstuvwxyz"
            reg_expression += '.'
            grey.append(userWordInput[i])
        elif userTileInput[i] == "$":
            reg_expression += userWordInput[i]

    reg_expression += '$'
    
    # Keeps all words, that match the regular expression...
    # For example if 'W' at i = 0 is yellow, it will eliminate all words with 'W' at i = 0 but keep words with 'W' at other indexes
    df = df[df['word'].str.contains(reg_expression, regex = True)]

    # Goes through the list of grey characters, and eliminates words in the df that contain them
    for i in grey:
        df = df[~(df['word'].str.contains(i))]

    # For that index, the yellow character in userTileInput is not supposed to be in the solution word (i.e. it can be any other character)
    # Handles duplicate letters such as POPPY so that the count of yellow characters matches the count of the letters in the current word
    for i in yellow:
        df = df[df['word'].str.count(i) == yellow.count(i)]

    return df