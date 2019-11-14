"""
6. Employee Management System
    This exercise assumes that you have created the Employee class for Programming Exercise 4.
    Create a program that stores Employee objects in a dictionary. Use the employee ID number
    as the key. The program should present a menu that lets the user perform the following actions:
        • Look up an employee in the dictionary
        • Add a new employee to the dictionary
        • Change an existing employee’s name, department, and job title in the dictionary
        • Delete an employee from the dictionary
        • Quit the program
    When the program ends, it should pickle the dictionary and save it to a file. Each time the
    program starts, it should try to load the pickled dictionary from the file. If the file does not
    exist, the program should start with an empty dictionary.
"""

# import libraries
from Classes_Exercises_4 import Employee
import pickle
from os import path

# initialize constants
DICT_FILE_PATH = r"C:\Users\student\Documents\myGitStuff\05-Python-Programming" + \
r"\Class_Practice_Exercises\Classes\Employees.dat"

# function that creates the initial employee dictionary and returns the dictionary
def create_initial_dict():
    employees = {
        '47899' : Employee('Susan Meyers', '47899', 'Accounting', 'Vice President'),
        '39119' : Employee('Mark Jones', '39119', 'IT', 'Programmer'),
        '81774' : Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
    }

    return employees

# function that takes a dictionary and filepath as arguments and pickles
# the dictionary to the filepath
def save_file(emp_dict, filepath):
    output_file = open(filepath, 'wb') # create and open the filepath for writing binary
    pickle.dump(emp_dict, output_file)
    output_file.close()

# function that clears the terminal screen
def clear_screen():
    print(chr(27) + "[H" + chr(27) + "[J")

# validate user input
def validate_input(user_input, input_type, min='', max='', option='', emp_dict=''):
    
    if input_type == 'id' and option == 'find_existing_id':
        if not user_input.isdigit() or \
        len(user_input) != max or \
        user_input == min or \
        user_input not in emp_dict:
            return False
        else:
            return True

 
    elif input_type == 'number':
        num_list = []
        for i in range(min, max):
            num_list.append(f'{i}')
        if user_input not in num_list:
            return False
        else:
            return True

# function that prints out a menu of options to choose from
def print_menu(menu_to_show, prompt, message = ''):
    # begin with clearing the screen
    clear_screen()
    
    #initialize local variables
    program_name = " ## Employee Management System ##"
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
    if message:
        print(message)
    elif 'message' in menu_to_show:
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
                continue
    # if no choices are given, get the user input
    else:
        user_response = input(prompt)
    return user_response

# find user by name
def find_id(emp_id, emp_dict):
    if emp_id in emp_dict:
        return True
    else:
        return False

# delete email function
def delete_user(emp_dict):
    find_name(input('Enter the person\'s name: '), email_dict)

# main function
def main():
    # check if the Employees.dat file exists already
    # if not, create the dictionary, then save it to the filepath
    if not path.exists(DICT_FILE_PATH):
        emp_dict = create_initial_dict()
        output_file = open(DICT_FILE_PATH, 'wb') # create and open the filepath for writing binary
        save_file(emp_dict, output_file)
        output_file.close()
    
    # indicate the end of the file
    end_of_file = False

    # open a file for binary reading
    input_file = open(DICT_FILE_PATH, 'rb')

    # read to the end of the file
    while not end_of_file:
        try:
            # unpickle/deserialize the next object
            emp_dict = pickle.load(input_file)
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
                '1' : 'Lookup Employee by ID',
                '2' : 'Add a New Employee',
                '3' : 'Modify an Employee',
                '4' : 'Delete an Employee',
                '5' : 'Quit'
            }
        }, 
        'lookup' : {
            'current' : ['Main','Lookup'],
            'message' : 'Enter an Employee ID to lookup.'
        },
        'invalid_id' : {
            'current' : ['Main','Lookup','Invalid'],
            'message' : 'Could not find that ID...\nChoose an option below:\n',
            'choices' : {
                '1' : 'Try to lookup another ID',
                '2' : 'Main Menu'
            }
        },
        'show_employee' : {
            'current' : ['Main','Lookup','View_Employee']
        },
        'add_emp_id' : {
            'current' : ['Main','Add_New_Emp_ID']
        },
        'add_emp_name' : {
            'current' : ['Main','Add_New_Emp_Name']
        },
        'add_emp_dept' : {
            'current' : ['Main','Add_New_Emp_Dept']
        },
        'add_emp_title' : {
            'current' : ['Main','Add_New_Emp_Title']
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
        
        # if user selects lookup employee by ID
        if user_selection == 1:
            # while main_menu option not chosen
            while not main_menu:
                # show the lookup menu
                emp_id = print_menu(menus['lookup'], 'ID: ')
                # validate id input
                valid_id = validate_input(emp_id, 'id', '00000', 5, 'find_existing_id', emp_dict)
                # if not a valid id
                if valid_id == False:
                    user_input = ''
                    # only options are 1 and 2, so keep displaying invalid menu until correct option is entered
                    while str(user_input) != '1' and str(user_input) != '2':
                        user_input = print_menu(menus['invalid_id'], 'Enter "1" or "2": ')
                    # if user wants to try entering another id, go back to beginning of loop
                    if user_input == '1':
                        continue
                    # if user wants to go back to main menu, set the option and break out of loop
                    else:
                        main_menu = True
                        break
                # if it was a valid id
                else:
                    # print out the employee data requested
                    print_menu(
                        menus['show_employee'], 
                        'Press <enter> to go back to main menu.', 
                        message = f'Employee Name: {emp_dict[emp_id].get_name()}\n' \
                        f'Employee ID: {emp_dict[emp_id].get_id_number()}\n' \
                        f'Employee Department: {emp_dict[emp_id].get_department()}\n' \
                        f'Employee Job Title: {emp_dict[emp_id].get_job_title()}'
                    )
                    # break out of loop
                    main_menu = True
                    break
            # if main_menu is chosen, go back to main menu loop
            if main_menu:
                continue

        # if user selects add a new employee
        if user_selection == 2:
            # set correct to false
            correct = False
            # loop while the information entered for new employee is not correct
            while not correct:
                # get all new employee information with input validation
                new_id = print_menu(menus['add_emp_id'], 'ID: ', 'Please enter the new\nemployee\'s 5 digit ID.')
                while not new_id.isdigit():
                    new_id = print_menu(menus['add_emp_id'], 'ID: ', 'ID must be an integer\n5 digits long.')
                while int(new_id) < 1 or len(new_id) != 5:
                    new_id = print_menu(menus['add_emp_id'], 'ID: ', 'ID must be an integer\n5 digits long.')
                while new_id in emp_dict:
                    new_id = print_menu(menus['add_emp_id'], 'ID: ', 'ID is already in use,\nenter another ID.')
                new_name = print_menu(menus['add_emp_name'], 'Name: ', 'Please enter the new\nemployee\'s name.')
                while len(new_name) < 2 or len(new_name) > 40:
                    new_name = print_menu(menus['add_emp_name'], 'Name: ', 'Name cannot be less than\n2 characters or greater\nthan 40 characters long.')
                while not new_name.isalpha:
                    new_name = print_menu(menus['add_emp_name'], 'Name: ', 'Name must be alphabet characters.')
                new_dept = print_menu(menus['add_emp_dept'], 'Department: ', 'Please enter the new\nemployee\'s job department.')
                new_title = print_menu(menus['add_emp_title'], 'Job Title: ', 'Please enter the new\nemployee\'s job title.')
                # initialize user input out of loop
                user_input = '0' 
                # loop until user inputs a "1" to append to dictionary or 
                # "2" to re-enter new employee information
                while user_input != '1' and user_input != '2':
                    # show all the employee information to verify before saving
                    user_input = print_menu(
                        menus['show_employee'],
                        'If correct enter "1", else "2": ',
                        message = f'Employee Name: {new_name}\n' \
                        f'Employee ID: {new_id}\n' \
                        f'Employee Department: {new_dept}\n' \
                        f'Employee Job Title: {new_title}'
                    )
                # if information is not correct, restart entries
                if user_input == '2':
                    continue
                # break out of while information is not correct loop
                else:
                    correct = True
            # add employee to employee dictionary
            emp_dict.update({new_id : Employee(new_name, new_id, new_dept, new_title)})
            # save the dictionary before displaying main menu again
            save_file(emp_dict, DICT_FILE_PATH)
        if user_selection == 4:
            user_input = '0'
            while user_input not in emp_dict:
                user_input = print_menu(menus['lookup'])
        #    user_selection = print_menu(menus['delete'], "Enter a name: ")
    print('\nSaving database.')
    save_file(emp_dict, DICT_FILE_PATH)
    print('\nExiting now.')
main()
