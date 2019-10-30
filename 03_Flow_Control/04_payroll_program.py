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