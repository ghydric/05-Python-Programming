## Append to list

# This function demonstrates how the append method
# can be usesd to add items to a list
def main():
    # initialize empty list
    name_list = []

    # create a variable to control our loop
    again = 'y'

    # add some names to the list
    while again == 'y':
        # get a name from the user
        name = input('Enter a name: ')

        # append the name to the list
        name_list.append(name)

        # add another one?
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()

    # display the names in the name list
    print(name_list)

# run the main function
main()