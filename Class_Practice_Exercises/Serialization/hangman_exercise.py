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

# function that reads a file (input as argument) and returns the word list
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

# function that returns an encoded version of a word.
# word is passed in as an argument.
# can also take another argument of a single letter.
def encode_word(input_word, guess = ''):
    # initialize encoded word
    word_encoded = ''
    # loop through each letter in input word
    for letter in input_word:
        # if the letter is a dash or a space,
        # output the letter as it is with a space added
        if letter == '-' or letter == ' ':
            word_encoded += (f'{letter} ')
        # if the letter matches user guess,
        # output the letter as it is with a space added
        elif letter == guess:
            word_encoded += (f'{letter} ')
        # output the letter as an underscore
        else:
            word_encoded += (f'_ ')
    # strip the last space off the end of the encoded word
    word_encoded = word_encoded.rstrip(' ')
    # return the encoded word
    return word_encoded


# function that displays the game
def display_game():



# main function
def main():
    # check if the name/email file exists already
    # if not, create the dictionary, then save it to the filepath
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
    rand_chosen_word = random.choice(word_bank)

    # create empty list of incorrect guesses
    list_inc_guesses = []
    
    print(rand_chosen_word)

main()