"""
4. A customer in a store is purchasing five items. Write a program that asks for the price of
each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 6 percent.
"""
salesTax = 0.06
subTotal = 0.00
exitFlag = False
for i in range(1,6):
    if exitFlag == False:
        sale = "item {}".format(i)
        item = input("Please enter the amount of {} or 'exit' to exit: ".format(sale))
        if item == "exit":
            print("Exiting.")
            exitFlag = True
            break
        elif item.isalpha() == True:
            print("You must enter a number amount.")
            continue            
        else:
            try:               
                subTotal += float(item)
            except:
                print("Something went wrong")
                exitFlag = True
                break
if exitFlag == False:
    totalSalesTax = salesTax*subTotal
    totalPrice = totalSalesTax + subTotal
    print(f"The subtotal is:    ${subTotal:10.2f}")
    print(f"The total tax is:   ${totalSalesTax:10.2f}")
    print(f"The grand total is: ${totalPrice:10.2f}")            