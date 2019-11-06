"""
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts,
it should retrieve the dictionary from the file and unpickle it.
"""


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

    # loop through the choices and print out the number of the
    # choice with the choice next to it
    for key in menu_to_show['choices']:
        print(f"    ({key}) {menu_to_show['choices'][key]}")
    
    # print a new line and line break
    print(f"\n{line_break}")
    
    # initialize user response to menu
    user_response = 0

    # input validation loop for user response
    while user_response < 1 or user_response > len(menu_to_show['choices']):
        try:
            user_response = int(input(prompt))
        except:
            print('Invalid entry')
            continue
    return user_response

# main function
def main():
    
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
            'choices' : {
                '1' : 'Main Menu'
            }
        },
        'add' : {
            'current' : ['Main','Add'],
            'choices' : {
                '1' : 'Main Menu'
            }
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
    
    # loop showing the main menu unless 5 is entered to exit the program
    while user_selection != 5:
        user_selection = print_menu(menus['main'], "What would you like to do? ")
        if user_selection == 4:
            user_selection = print_menu(menus['delete'], "Enter a name: ")
main()