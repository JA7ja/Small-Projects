import random

#############################################################################################
#   Chooses a random word from the sowpods dictionary and creates the display(blank) word   #
#############################################################################################
def choose_word(gamelog):
    word_file = open("C:\\Users\\Jack\\Documents\\atom-workspace\\Games\\sowpods.txt", "r")
    words = []
    for line in word_file:
        words.append(line)
    word_file.close()
    rand_word = random.choice(words)
    rand_word = rand_word[:len(rand_word)-1]
    disp_word = []
    for letter in rand_word:
        disp_word.append("_")
    gamelog.append(disp_word)
    return rand_word, gamelog

##############################################################################################
#   Universal way of displaying words or lists with spaces between indexes for readability   #
##############################################################################################
def print_display(display):
    for letter in display:
        print(letter + " ", end="")
    print("")

###################################################################################################################
#   Used to print the game log after every guess to keep the player from having to scroll back through the game   #
###################################################################################################################
def print_log(gamelog):
    print()
    for word in gamelog:
        if(word != "------------------------------"):
            print_display(word)
        else:
            print(word)
    print()

#################################################################################
#   Tests the guess against the lingo word and adds the result to the gamelog   #
#################################################################################
def guess_test(word, guess, gamelog):
    guess_result = []
    for i in range(len(guess)):
        if(word[i] == guess[i]):
            guess_result.append(guess[i])
            gamelog[0][i] = word[i]
        elif(guess[i] in word):
            guess_result.append(guess[i].lower())
        else:
            guess_result.append('/')
    gamelog.append(guess_result)
    gamelog.append("------------------------------")
    return gamelog

##################################################################################################
#   Gets a valid guess from the user, checking both for word length and validity of characters   #
##################################################################################################
def get_guess(word, gamelog):
    print("Guess a word of equal length: ", end="")
    guess = input().upper()
    all_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    bad_guess = True
    while(bad_guess):
        good_chars = True
        for letter in guess:
            if letter not in all_letters:
                good_chars = False
        if(len(word) != len(guess)):
            print("That guess doesn't have the same amount of letters as the Lingo word! Guess again: ", end="")
            guess = input().upper()
        elif(not good_chars):
            print("That guess contains non-letter characters! Guess again: ", end="")
            guess = input().upper()
        else:
            bad_guess = False
    gamelog.append(guess)
    return guess, gamelog

######################################################################################################################
#   Congradulates the user at the end of the game and lets them know how many guesses it took them to get the word   #
######################################################################################################################
def end_of_game(gamelog):
    guesses = (int)(((len(gamelog)-2))/3)
    print()
    if guesses == 1:
        print("Congrats! You got the Lingo word! It took you " + str(guesses) + " guess to get the word! Impressive!")
    else:
        print("Congrats! You got the Lingo word! It took you " + str(guesses) + " guesses to get the word!")



##############################
######  MAIN FUNCTION  #######
##############################

def main():
    gamelog = []
    word, gamelog = choose_word(gamelog)
    gamelog.append("------------------------------")
    print(word)
    print(len(word))
    print("Welcome to Lingo!")
    print_log(gamelog)
    while("_" in gamelog[0]):
        guess, gamelog = get_guess(word, gamelog)
        gamelog = guess_test(word, guess, gamelog)
        print_log(gamelog)
    end_of_game(gamelog)

main()
