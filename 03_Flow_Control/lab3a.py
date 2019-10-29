"""## Lab 3A

![](../.gitbook/assets/madlibs.png)

## General

Create your own mad libs game asking the user for 
input to fill in the blanks. Print out using .format\(\).

## Requirments

* Adhere to PEP8 \(Comments, formatting, style, etc\)
* Create a handfull of pharses that require different numbers 
of inputs
* Prompt the user for input\(s\):
  * Inputs can be done a number of ways... 
    * \(SIMPLE\) Ask user for input directly, tell them if the 
    word\(s\) need to be a verb, noun, etc. 
    * \(Moderate\) Give the user a handful of choices per input 
    to choose from.You will need to create a bank of verbs, 
    nouns, etc for this. 
    * \(Harder\) Give the user cards based off the actual game. 
    Allowing them to draw, etc following the rules. Allow them 
    to only input those cards. 
  * \(opitional\) Implement basic user input checking:
    * Check to ensure words are words, numbers are numbers 
    \(there are many ways to do this\)
    * Ensure symobls aren't used if they are not needed
    * Check length
    * etc
    * Implement re-input if input is incorrect
* Output the user inputs into the given pharse
* Use formatting to not only output the user inputs, 
but to create a UI within the terminal. Space out certain 
UI elements such as title of program, choices, menu deceration, 
etc.
"""
def clear_screen():
    print(chr(27) + "[H" + chr(27) + "[J")

def display_game():
    title = "It's MAD LIBS!"

    print(title)
    
clear_screen
display_game   
