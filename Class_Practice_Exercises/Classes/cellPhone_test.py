# this program tests the CellPhone class

import cellPhone as c

def main():
    # get the phone data
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    # create an instance
    phone = c.CellPhone(man, mod, retail)

    # display the data that was entered
    print('Here is the data you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number: ', phone.get_model())
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')

# call the main function
main()