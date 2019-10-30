"""
1. Roman Numerals

Write a program that prompts the user to enter a number within 
the range of 1 through 10. The program should display the Roman numeral version of 
that number. If the number isoutside the range of 1 through 10, the program 
should display an error message.
"""
while True:
    userNum = input("Please enter a number 1 through 10:  ")
    
    if userNum == "1":
        print("I")
        break
    elif userNum == "2":
        print("II")
        break
    elif userNum == "3":
        print("III")
        break
    elif userNum == "4":
        print("IV")
        break
    elif userNum == "5":
        print("V")
        break
    elif userNum == "6":
        print("VI")
        break
    elif userNum == "7":
        print("VII")
        break
    elif userNum == "8":
        print("VIII")
        break
    elif userNum == "9":
        print("IX")
        break
    elif userNum == "10":
        print("X")
        break
    else:
        print("Invalid Entry!")
        continue