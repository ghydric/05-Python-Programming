"""
2.  A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, and then displays
the profit that will be made from that amount.
"""

profitRate = 0.23

while True:
    sales = input("Please enter the projected amount of sales for the year or 0 to exit: ")
    if sales.isdigit() == False:
        print("You must enter a number amount.")
        continue
    elif int(sales) == 0:
        print("Exiting.")
        break
    else:
        profit = float(sales)*profitRate
        print("The total profit for the year is {}!".format(profit))