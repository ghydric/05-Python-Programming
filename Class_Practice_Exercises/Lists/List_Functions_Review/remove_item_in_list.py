# This program demonstrates how to remove an item from a list

def main():
    # create a list with some items
    food = ['pizza', 'burgers', 'chips']

    #display the list
    print('Here are the items in the food list: ')
    print(food)

    # get the item to remove
    item = input('Which item should I remove? ')

    try:
        # remove the item
        food.remove(item)

        # display the list
        print('Here is the revised list: ')
        print(food)

    except ValueError:
        print('That item was not found in the list')

# call the main function
main()