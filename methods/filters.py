def filterData(df, user_word_input, user_tile_color_input):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    yellow = list()
    grey = list()
    
    # Create a reg expression for words that have the green spaces correctly placed
    reg_expression = "^"
    for i in range(len(user_tile_color_input)):
        if user_tile_color_input[i] == "Y":
            alphabet = alphabet.replace(user_word_input[i],'')
            reg_expression+='[{}]'.format(alphabet)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            yellow.append(user_word_input[i])
        elif user_tile_color_input[i] == "G":
            alphabet = alphabet.replace(user_word_input[i],'')
            reg_expression+='[{}]'.format(alphabet)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            grey.append(user_word_input[i])
            #reg_expression+='.'
        elif user_tile_color_input[i] == "$":
            reg_expression += user_word_input[i]

    reg_expression += '$'

    # print(reg_expression)
    
    df = df[df['word'].str.contains(reg_expression, regex = True)]

    # For that index, the yellow character in user_tile_color_input is not supposed to be in the solution word (i.e. it can be any other character)
    for i in yellow:
        df = df[df['word'].str.contains(i)]

    # Handles duplicate letters such as POPPY so that the count of yellow characters matches the count of the letters in the current word.
    for i in yellow:
        df = df[df['word'].str.count(i) == yellow.count(i)]

    return df