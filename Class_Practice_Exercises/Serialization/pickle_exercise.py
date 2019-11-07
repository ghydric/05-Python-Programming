"""
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts,
it should retrieve the dictionary from the file and unpickle it.
"""
# import necessary libraries
from os import path
import pickle

DICT_FILE_PATH = r"C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\Serialization\names_emails.dat"

# function that creates the initial name/email dictionary and returns the dictionary
def create_initial_dict():
    name_email_dict = {
        'Bob' : 'bobsyouruncle@yahoo.com',
        'Nancy' : 'nantheman@msn.com',
        'Hope' : 'hopealways@gmail.com',
        'Catherine' : 'catsaysmeowmix@msn.com'
    }
    return name_email_dict

# function that takes a dictionary and filepath as arguments and pickles
# the dictionary to the filepath
def save_file(email_dict, file):
    pickle.dump(email_dict, file)

# function that clears the terminal screen
def clear_screen():
    print(chr(27) + "[H" + chr(27) + "[J")

# function that prints out a menu of options to choose from
def print_menu(menu_to_show, prompt):
    # begin with clearing the screen
    clear_screen()
    
    #initialize local variables
    program_name = "      ## Email Helper 1.0 ##"
    line_break = "-"*34
    
    #start printing the menu
    print(line_break)
    print(program_name)
    print(line_break)
    
    # loop through the menu tree and display tree
    for menu in menu_to_show['current']:
        print(f" => {menu}", end='')
    
    print("\n") # print blank line

    # if there is a message to show, print it
    if 'message' in menu_to_show:
        print(str(menu_to_show['message']))

    # if there are choices to display, print them
    if 'choices' in menu_to_show:
        # loop through the choices and print out the number of the
        # choice with the choice next to it
        for key in menu_to_show['choices']:
            print(f"    ({key}) {menu_to_show['choices'][key]}")
    
    # print a new line and line break
    print(f"\n{line_break}")

    # input validation loop for user response if choices are given
    if 'choices' in menu_to_show:
        # initialize user response to menu
        user_response = 0
        # if user response is less than 1 or greater than number of choices given
        while user_response < 1 or user_response > len(menu_to_show['choices']):
            try:
                user_response = int(input(prompt))
            except:
                print('Invalid entry')
                continue
    # inf no choices are given, get the user input
    else:
        user_response = input(prompt)
    return user_response

# find user by name
def find_name(name, email_dict):
    if name in email_dict:
        return name, email_dict[name]
    else:
        return False, False

# delete email function
def delete_user(email_dict):
    find_name(input('Enter the person\'s name: '), email_dict)

# main function
def main():
    # check if the name/email file exists already
    # if not, create the dictionary, then save it to the filepath
    if not path.exists(DICT_FILE_PATH):
        name_email_dict = create_initial_dict()
        output_file = open(DICT_FILE_PATH, 'wb') #create and open the filepath for writing binary
        save_file(name_email_dict, output_file)
        output_file.close()
    
    # indicate the end of the file
    end_of_file = False

    # open a file for binary reading
    input_file = open(DICT_FILE_PATH, 'rb')

    # read to the end of the file
    while not end_of_file:
        try:
            # unpickle/deserialize the next object
            name_email_dict = pickle.load(input_file)
        except EOFError:
            # set the flag to indicate the end
            # of the file has been reached
            end_of_file = True
    
    # close our file
    input_file.close()

    # dictionary containing all the menus and options
    menus = {
        'main' : {
            'current' : ['Main'],
            'choices' : {
                '1' : 'Lookup email by name',
                '2' : 'Add a new email',
                '3' : 'Change an email',
                '4' : 'Delete an email',
                '5' : 'Exit'
            }
        },
        'lookup' : {
            'current' : ['Main','Lookup'],
            'message' : 'Enter a name to lookup.'
        },
        'invalid_name' : {
            'current' : ['Main','Lookup','Invalid'],
            'message' : 'Could not find that name...\nChoose an option below:\n',
            'choices' : {
                '1' : 'Try to lookup another name',
                '2' : 'Main Menu'
            }
        },
        'show_email' : {
            'current' : ['Main','Lookup','View_Email'],
            'message' : 'Below is the email address:'
        },
        'add_name' : {
            'current' : ['Main','Add_Name'],
            'message' : 'Enter a new name to add.'
        },
        'add_email' : {
            'current' : ['Main','Add_Name','Add_Email'],
            'message' : 'Enter a new email to add.'
        },
        'change' : {
            'current' : ['Main','Change'],
            'choices' : {
                '1' : 'Main Menu'
            }
        },
        'delete' : {
            'current' : ['Main','Delete'],
            'choices' : {
                '1' : 'Main Menu'
            }
        }
    }
    # initialize user selection
    user_selection = 0
    
    ### MAIN MENU SELECTION LOGIC ###
    # loop showing the main menu unless 5 is entered to exit the program
    while user_selection != 5:
        # variable telling whether main menu was initiated
        main_menu = False
        
        # show main menu
        user_selection = print_menu(menus['main'], 'What would you like to do? ')
        
        # if user selects lookup email by name
        if user_selection == 1:
            # show the lookup menu
            name = print_menu(menus['lookup'], 'Name: ')
            # attempt to locate the name entered in the email dictionary
            person, email = find_name(name, name_email_dict)
            # loop while name entered was not in dictionary
            while not person:
                # show the invalid name menu
                user_input = print_menu(menus['invalid_name'], 'Enter "1" or "2": ')
                while user_input != 1 and user_input != 2:
                    user_input = print_menu(menus['invalid_name'], 'Invalid entry, enter "1" or "2": ')
                if user_input == 1:
                    # show the lookup menu
                    name = print_menu(menus['lookup'], 'Name: ')
                    # attempt to locate the name entered in the email dictionary
                    person, email = find_name(name, name_email_dict)
                else:
                    # user entered 2 to go back to main menu
                    main_menu = True
                    break # break out of while loop
            
            # only go to main_menu if main_menu set to True
            if main_menu:
                # show main menu
                continue
            # print out the email requested
            print(f'\nThe email for {person} is:\n    {email}\n')
            input('Press <enter> to go back to main menu.')

        # if user selects add a new email
        if user_selection == 2:
            new_name = print_menu(menus['add_name'], 'Name: ')
            new_email = print_menu(menus['add_email'], 'Email: ')
        #if user_selection == 4:
        #    delete_user
        #    user_selection = print_menu(menus['delete'], "Enter a name: ")
    print('\nExiting now.')
main()