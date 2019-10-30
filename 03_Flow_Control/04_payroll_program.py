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
employees = {} # dictionary to hold all employees

# Create Employee Class
class Employee:
    def _init_(self, employeeNum, firstName, lastName, payRate):
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

    print_menu(menus_selected, ["Enter a new employee","Calculate employee weekly gross pay","Exit"],"What would you like to do? ")

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