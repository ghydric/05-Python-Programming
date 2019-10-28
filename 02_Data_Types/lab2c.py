tax = 0.07

while True:
    amt = float(input("Please enter '0' to exit or enter the item amount: "))
    if amt == 0 or amt == "":
        break
    elif amt < 0:
        continue
    else:
        total = amt*tax + amt
        print("Your total is: ",total)