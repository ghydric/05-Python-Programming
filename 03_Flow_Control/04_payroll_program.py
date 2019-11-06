"""
Chris owns an auto repair business and has several employees. If any 
employee works over 40 hours in a wewek, he pays them 1.5 times their regular
hourly pay rate for all hours over 40. He has asked you to design a simple
payroll program that calculates an employee's gross pay, including any overtime wages.
"""
# Global Constants
BASE_HOURS = 40
OT_MULTIPLIER = 1.5

# Global Variables
exitFlag = False # initialize exitFlag as false to not exit the program
current_employees = [] # list to hold all current employees

# Create Employee Class
class Employee:
    def __init__(self, employeeNum, firstName, lastName, payRate):
        self.employeeNum = employeeNum
        self.firstName = firstName
        self.lastName = lastName
        self.payRate = payRate

    def calc_gross_pay(self, hoursWorked = 40):
        self.hoursWorked = hoursWorked
        grossOTPay = 0.00

        if self.hoursWorked > BASE_HOURS:
            hoursOT = self.hoursWorked - BASE_HOURS
            grossOTPay = self.payRate*OT_MULTIPLIER*hoursOT
        
        grossPay = self.hoursWorked*self.payRate + grossOTPay
        return grossPay

def clear_screen():
    print(chr(27) + "[H" + chr(27) + "[J")

# function that creates current employees from the Employee class
# and adds them to a current_employees list
def create_current_employees():
    emp1 = Employee(1, "Nancy", "Howard", 10.00)
    emp2 = Employee(2, "Travis", "Kline", 12.00)
    emp3 = Employee(3, "Brandon", "Hane", 15.00)
    current_employees.insert(0,emp1)
    current_employees.insert(1,emp2)
    current_employees.insert(2,emp3)

# function that prints out a menu of options to choose from
def print_menu(current_menu, choices, prompt):
    # begin with clearing the screen
    clear_screen()
    
    #initialize local variables
    header = "-"*20 + "Chris Autos" + "-"*20
    slogan = "        Where you break it and we fix it!"
    line_break = "-"*51
    
    #start printing the menu
    print(header)
    print(slogan)
    print(line_break)
    
    # loop through the menu tree and display tree
    for x in current_menu:
        print(" => {}".format(x))
    
    print("\n")

    #get number of choices
    choice_count = len(choices)

    # loop through the choices and print out the number of the
    # choice with the choice next to it
    for i in range(choice_count):
        print("    ({0}) {1}".format(i+1, choices[i]))
    
    # print a new line and line break
    print("\n{0}".format(line_break))
    
    # initialize user response to menu
    user_response = 0

    # input validation loop for user response
    while user_response < 1 or user_response > choice_count:
        try:
            user_response = int(input("Type in a number (1-{0}): ".format(choice_count)))
        except:
            continue
    return user_response


def main():
    
    menus_selected = ["main"]
    create_current_employees()
    user_main_selection = 0
    user_calc_selection = 0
    # while loop to keep running the main menu until exit is selected
    while user_main_selection != 3:
        user_main_selection = print_menu(menus_selected, ["Enter a new employee","Calculate employee weekly gross pay","Exit"],"What would you like to do? ")
        
        if user_main_selection == 1:
            print("You selected 1")
        elif user_main_selection == 2:
            while user_calc_selection <= 0 or user_calc_selection > len(current_employees):
                user_calc_selection = int(input("Please enter your employee number: "))

main()
"""
for i in range(1,6):
    if exitFlag == False: # exit program if exitFlag is set to True
        
        # add the item number in the question each loop iteration
        item = input("Please enter the amount of item {} or 'exit' to exit: ".format(i))
        
        if item == "exit": # check whether user typed exit
            print("Exiting.")
            exitFlag = True # set the exitFlag to True to exit program
            break
        elif item.isalpha() == True: # check if there is only characters and no numbers
            print("You must enter a number amount.")
            continue # ask the same loop question again
        else:
            try:               
                subTotal += float(item)
            except:
                print("Something went wrong")
                exitFlag = True
                break
if exitFlag == False: # only do below if not exiting the program
    totalSalesTax = salesTax*subTotal
    totalPrice = totalSalesTax + subTotal
    print(f"The subtotal is:    {subTotal:10.2f}")
    print(f"The total tax is:   {totalSalesTax:10.2f}")
    print(f"The grand total is: {totalPrice:10.2f}")
"""