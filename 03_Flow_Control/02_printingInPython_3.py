"""
3.  One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
enter the total square feet in a tract of land and calculates the number of acres in the tract.
"""

sqFtInAcre = 43560

while True:
    sqFtLand = input("Please enter the amount of square feet of land or 0 to exit: ")
    if sqFtLand.isdigit() == False:
        print("You must enter a number amount.")
        continue
    elif int(sqFtLand) == 0:
        print("Exiting.")
        break
    else:
        acres = float(sqFtLand) / sqFtInAcre
        print(f"The total acres of land is {acres:.2f}!")