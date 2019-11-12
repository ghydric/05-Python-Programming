# this program creates five CellPhone objects and stores them in a list

import cellPhone as c

def main():
    # get a list of CellPhones
    phones = make_list()

    # display the data in the list
    print('Here is the data you entered: ')
    display_list(phones)

# the make_list function gets data from the user
# for five phones. the function returns a list
# of CellPhone objects containing the data
def make_list():
    # create an empty list
    phone_list = []

    # add five CellPhone objects to the list
    for count in range(1,6):
        # get the phone data
        print('Phone number ' + str(count) + ':')
        man = input('Enter the manufacturer: ')
        mod = input ('Enter the model number: ')
        retail = float(input('Enter the retail price: '))
        print()
    
        # create a new CellPhone object in memory and 
        # assign it to the new phone variable
        phone = c.CellPhone(man, mod, retail)

        # add the object to the list
        phone_list.append(phone)

    return phone_list

# the display_list function accepts a list containing
# CellPhone objects as an argument and displays the 
# data stored in each object
def display_list(phone_list):
    index = 1
    for phone in phone_list:
        print('Phone number ' + str(index) + ':')
        print(phone.get_manufact())
        print(phone.get_model())
        print(phone.get_retail_price())
        print()
        index = index + 1

main()