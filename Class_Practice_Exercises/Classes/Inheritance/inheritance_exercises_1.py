"""
1. Employee and ProductionWorker Classes
    Write an Employee class that keeps data attributes for the following pieces of information:
        • Employee name
        • Employee number
    Next, write a class named ProductionWorker that is a subclass of the Employee class. The
    ProductionWorker class should keep data attributes for the following information:
        • Shift number (an integer, such as 1, 2, or 3)
        • Hourly pay rate
    The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the
    night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
    Once you have written the classes, write a program that creates an object of the
    ProductionWorker class and prompts the user to enter data for each of the object’s data
    attributes. Store the data in the object and then use the object’s accessor methods to retrieve
    it and display it on the screen.
"""

# Employee class
class Employee:
    # __init__ method creates an Employee object and takes
    # in an Employee name and Employee number as arguments
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    
    # setters
    def set_name(self, name):
        self.__name = name
    
    def set_number(self, number):
        self.__number = number

    # getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

# Production Worker class
class ProductionWorker(Employee):
    # __init__ method creates a ProductionWorker object and takes in
    # name, number, shift_number, and hourly_pay_rate as arguments
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        # call superclass's __init__ method
        super().__init__(name, number)

        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate
    
    # setters
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # getters
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    # function to print out all attributes neatly
    def __str__(self):
        if self.get_shift_number() == '1':
            shift = 'Day Shift'
        else:
            shift = 'Night Shift'
        return (
            f'Employee Name: {self.get_name()}\n' \
            f'Employee Number: {self.get_number()}\n' \
            f'Shift: {shift}\n' \
            f'Hourly Pay Rate: {self.get_hourly_pay_rate():.2f}\n'
        )

# main function creates a ProductionWorker object and prompts
# user to input all of the data attributes and then displays
# all of them
def main():
    # set valid_name to False to start user input loop
    valid_name = False
    # loop for user input until a valid name is entered
    while not valid_name:
        # get user input for Employee name
        name = input('Enter the ProductionWorker\'s name: ')
        # check the length for a valid name and start loop over if invalid length
        if len(name) < 2 or len(name) > 40:
            continue
        invalid_char = False
        # check each letter in name for invalid characters and start loop over
        # if any invalid characters are given, set invalid_char to True
        for letter in name:
            if not letter.isalpha() and letter != ' ':
                invalid_char = True
                break
        # if invalid character found in name, start loop over
        if invalid_char:
            continue
        # otherwise user entered a valid name and break out of loop
        else:
            valid_name = True
    # get user input for employee number
    number = input('Enter the ProductionWorker\'s number: ')
    # validate user input number is a digit, and length is 2 or 3 digits
    # otherwise loop and prompt for employee number again
    while not number.isdigit() or len(number) < 2 or len(number) > 3:
        number = input('Number must be either 2 or 3 digits: ')
    # get user input for shift number
    shift_number = input('Enter the shift number (1 or 2): ')
    # validate user input shift_number is a digit, and that it is a 1 or 2
    # otherwise loop and prompt for shift_number again
    while not shift_number.isdigit() or shift_number != '1' and shift_number != '2':
        shift_number = input('Shift number must be 1 or 2: ')
    # set variable to track whether input can be type-casted to float without errors
    is_float = False
    # user input loop to get the hourly pay rate
    while not is_float:
        try:
            # if this type-cast to float works without error
            # then set is_float to True to break out of loop
            hourly_pay_rate = float(input('Enter the hourly pay rate: '))
            is_float = True
        except:
            # if type-cast to float errors, print to screen and start
            # user input loop over
            print('Hourly pay rate must be a number!')
    # create the ProductionWorker object with user inputs
    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)
    # add blank line for readability
    print()
    # display ProductionWorker attributes
    print(worker)
    # add blank line for readability
    print()

# call main()
main()