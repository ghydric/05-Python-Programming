"""
4. A customer in a store is purchasing five items. Write a program that asks for the price of
each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 6 percent.
"""
salesTax = 0.06 # sales tax percentage
subTotal = 0.00 # subtotal will hold all 5 item values
exitFlag = False # initialize exitFlag as false to not exit the program
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