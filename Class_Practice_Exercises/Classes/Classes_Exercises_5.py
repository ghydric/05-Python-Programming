"""
5. RetailItem Class
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:
​
            Description     Units in Inventory  Price
Item #1     Jacket          12                  59.95
Item #2     Designer Jeans  40                  34.95
Item #3     Shirt           20                  24.95
"""

# RetailItem class
class RetailItem:
    # __init__ method creates a RetailItem object with
    # description, units_in_inventory, and price attributes
    def __init__(self, desc, units, price):
        self.__description = desc
        self.__units_in_inventory = int(units)
        self.__price = float(price)
    
    # __str__ method displays all the attributes as strings
    def __str__(self):
        return f'Description: {self.__description}\n' \
        f'Units in Inventory: {self.__units_in_inventory}\n' \
        f'Price: ${self.__price:.2f}'

# main function creates 3 RetailItem objects using a dictionary of item_data,
# then appends them to items_list
def main():
    # create empty items_list
    items_list = []

    item_data = {
        1 : {
            'desc' : 'Jacket',
            'units' : 12,
            'price' : 59.95
        },
        2 : {
            'desc' : 'Designer Jeans',
            'units' : 40,
            'price' : 34.95
        },
        3 : {
            'desc' : 'Shirt',
            'units' : 20,
            'price' : 24.95
        }
    }

    # loop through each item in item_data to create
    # RetailItem objects
    for i in range(1,4):
        new_item = RetailItem(
            item_data[i]['desc'],
            item_data[i]['units'],
            item_data[i]['price']
        )

        # add the new_item to items_list
        items_list.append(new_item)
    
    # initialize counter
    count = 1
    
    # add a blank line for readability
    print()

    # loop through each item in items_list and display value for each attribute
    for item in items_list:
        print(f'Item ' + str(count) + ':')
        print(item, '\n')
        count += 1
        
# call main function
main()