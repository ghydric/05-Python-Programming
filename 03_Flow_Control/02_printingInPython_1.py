"""Write a program that displays the following information:
	• Your name
	• Your address, with city, state, and ZIP
	• Your telephone number
	• Your MOS
"""
# Gather input data
name = input("Please enter your name: ")
bldgNum = int(input("Please enter your building number: "))
street = input("Please enter your street name: ")
city = input("Please enter your city: ")
state = input("Please enter your state: ")
zipCode = int(input("Please enter your zip code: "))
phone = int(input("Please enter your phone number: "))
mos = input("Please enter your MOS: ")

# Output formatted answers
print("Your name is %s." % name)
print("Your address is:\n%d %s,\n%s, %s %d" % (bldgNum, street, city, state, zipCode))
print("Your phone number is: %d" % phone)
print("Your mos is: %s" % mos)