"""
Task:
    Your task is to implement the Hangman game in Python.
​
Program Specifications:
    1) Output a brief description of the game of hangman and how to play
    2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
        for you if you want to be surprised)
    3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
        how many letters are in each word and how many words there are)
    4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
        letter is in the word, otherwise report that the user has made an incorrect guess.
    5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
        as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
    6) Your program should allow the user to make a total of k=6 guesses.
​
Assignment Notes:
If the letter has already been guessed, output a message to the player and ask for input again.
If the guess entered is not an alphabetic letter, output a message and ask for input again.
​
If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 
If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the 
player they have won and quit the game.
​
If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the 
guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), 
the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.
​
Bonus:
    You can do one or both of the following:
​
    1) Using a file:
    Instead of asking for user input for the word, make a word bank in a file named hangman_words.txt. 
    Read in the contents of the file and choose a word at random.
​
    2) Forever alone option:
    You enter the word (or it is randomly chosen from the word bank) and have the computer try to guess the letters.
​
    3) Add some more functionality: 
        - Persist user profiles with scores
        - Prompt for which user is playing
        - Ask if the user wants to play a set of games
        - Build a leader board
        
    Have fun, get creative, and demonstrate what you've come up with.
"""
### Import Libraries
import random
from os import path

### Define Global CONSTANTS
# file path to word bank
WORD_BANK_PATH = r"C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\Serialization\hangman_words.txt"
# list of available choices
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

### Define Global Variables

### Start of Functions
#-----------------------#
# function that creates the hangman_words.txt file with a list of words
def create_word_bank(filepath):
    # Open a file named hangman_words.txt
    f = open(filepath, 'w')
    # list of words to become the word bank
    words = ['DISTRIBUTOR ROTOR','PRESSURE PLATE','THROW-OUT BEARING','LIMITED-SLIP DIFFERENTIAL','INNER TIE-ROD END']
    # write each of the words in list to the file
    for word in words:
        f.write(f"{word}\n")
    # close the file
    f.close()

# function that reads a text file (input as argument) and returns the word list
def get_word_bank(filepath):
    # open file at filepath
    f = open(filepath, 'r')
    # create empty words list
    words = [] 
    # loop through the file reading each line,
    # then append that line to the words list
    for line in f.readlines():
        words.append(line.rstrip('\n'))
    # close the file
    f.close()
    #return the list
    return words

# function that returns an underscore version of a word.
# word and underscore version are passed in as arguments.
# this word created as underscores is what is to be shown to user to guess.
def make_spooky_word(chosen, spooky):
    
    # loop through each letter in input word
    for letter in chosen:
        # if the letter is a dash or a space,
        # output the letter as it is with a space added
        if letter == '-' or letter == ' ':
            spooky += (f'{letter} ')

        # output the letter as an underscore
        else:
            spooky += (f'_ ')
    # strip the last space off the end of the encoded word
    spooky = spooky.rstrip(' ')
    # return the encoded word
    return spooky

# function that returns a spaced version of the chosen word.
# chosen word is passed in as an argument.
# update_spooky_word uses this version for index reference to update the spooky word.
def make_spaced_chosen_word(chosen):
    # initialize spaced version of chosen word to null string
    spaced_chosen = ''
    # loop through each letter of chosen word and add letter
    # with a space to spaced version
    for letter in chosen:
        spaced_chosen += f'{letter} '
    # remove the final space off of spaced version
    spaced_chosen = spaced_chosen.rstrip(' ')
    # return the spaced version of chosen word
    return spaced_chosen

# function that updates the spooky word shown to player to guess
def update_spooky_word(guess, spooky, chosen):
    # make spooky a list to modify based on index
    spooky_list = list(spooky)
    # loop through each letter in chosen word
    for index, value in enumerate(chosen):
        # skip letters that are spaces
        if chosen[index] == ' ':
            continue
        # if guess matches letter,
        # then replace the same index of spooky word with guess
        elif guess == chosen[index]:
            spooky_list[index] = guess
        # otherwise skip the letter
        else:
            continue
    # change spooky list back into string
    spooky = "".join(spooky_list)
    print(spooky)
    # return spooky word
    return spooky

# function that displays the game
def display_game(menu, spooky = '', incorrect = ''):
    
    if menu == 'launch':
        print('                   HANGMAN')
        print('----------------------------------------------')
        print('Guess a letter of the alphabet to see if it')
        print('is in the below mystery word that was chosen')
        print('randomly. If your guess is not in the mystery')
        print('word, you are that much closer to being hung!')
        print('Guess incorrectly too many times and you lose!')
        print('To win, guess all the letters in the mystery')
        print('word without getting hung!')
        print('')
        print('To play: Enter "1"')
        print('To exit: Enter "2"')
        while True:
            try:
                choice = input('Choice: ')
                if choice != '1' and choice != '2':
                    print('Invalid choice.')
                    continue
                else:
                    break
            except:
                continue
        if choice == '1':
            return True
        else:
            return False

    elif menu == 'game_play':
        print('                   HANGMAN')
        print('----------------------------------------------')
        print('')
        print(f'    {spooky}')
        print('')
        print(f'Incorrect Guesses: {str(incorrect).strip("[]")}')
        print('----------------------------------------------')

    elif menu == 'won':
        print('                   HANGMAN')
        print('----------------------------------------------')
        print('')
        print(f'    {spooky}')
        print('')
        print('YOU WIN!!')
        print('')
    
    elif menu == 'lost':
        print('                   HANGMAN')
        print('----------------------------------------------')
        print('')
        print('  The mystery word was:')
        print(f'    {spooky}')
        print('')
        print('YOU DUN GOT HANGED!!')
        print('')

# function that gets the player's guess and validates it is
# a single alphabetic character, then returns the uppercase version
def get_player_guess():
    # get a guess from the player
    guess = input('Guess a single letter: ')
    # loop while the guess is not a character
    while guess.isalpha() == False:
        print('Guess must be a letter of the alphabet!')
        guess = input('Guess a single letter: ')
    # loop while length of guess is not equal to 1
    while len(guess) != 1:
        guess = input('Too many letters, enter a single letter: ')
    # return the uppercase version of the guess
    return guess.upper()

# function that takes the player's guess as input and checks
# whether the guess is in the mystery word
def check_guess_correct(guess, chosen):
    if guess in chosen:
        return True
    else:
        return False

# main function
def main():
    # play game until player chooses to exit at launch menu
    while True:
        # display the launch menu for the game
        play = display_game(menu = 'launch')
        
        # exit the game if player chose not to play
        if not play:
            exit()
        
        # check if the word bank file exists already
        # if not, create the word bank text file
        if not path.exists(WORD_BANK_PATH):
            try:
                create_word_bank(WORD_BANK_PATH)
            except:
                print('An error occured creating the wordbank, exiting')
                exit()
        
        # try to retrieve the word bank
        try:
            word_bank = get_word_bank(WORD_BANK_PATH)
        except:
            print('An error occured retrieving the wordbank, exiting')
            exit()
        
        # let computer choose a word from the word bank
        chosen_word = random.choice(word_bank)
        
        # create spaced version of chosen_word
        spaced_chosen_word = make_spaced_chosen_word(chosen_word)
        
        # initialize spooky_word
        spooky_word = ''
        
        # create spooky version (letters replaced with underscores) of chosen word
        spooky_word = make_spooky_word(chosen_word, spooky_word)

        # create empty list of incorrect guesses
        list_inc_guesses = []

        print(chosen_word)
        print(spaced_chosen_word)
        print(spooky_word)

        # while the spooky word contains at least 1 underscore or
        # the length of the incorrect guesses becomes greater than 7
        # loop through game play
        while '_' in spooky_word and len(list_inc_guesses) <= 7:
            
            display_game(menu = 'game_play', spooky = spooky_word, incorrect = list_inc_guesses)
            user_input = get_player_guess()
            valid = check_guess_correct(user_input, chosen_word)
            if valid:
                spooky_word = update_spooky_word(user_input, spooky_word, spaced_chosen_word)
            elif user_input in list_inc_guesses:
                print('Already guessed that.')
                continue
            else:
                list_inc_guesses += user_input
        
        if len(list_inc_guesses) == 8:
            display_game(menu = 'lost', spooky = spaced_chosen_word)
            input('Press enter')
            
        else:
            display_game(menu = 'won', spooky = spooky_word)
            input('Press enter')

main()