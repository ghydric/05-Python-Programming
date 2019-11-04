# this program demonstrates the insert method

def main():
    # create a list with some names
    names = ['James', 'Kathryn', 'Bill']

    # display the list
    print('This list before insert:')
    print(names)

    # insert a new name at element 0
    names.insert(0, 'Joe')

    # display the list again
    print('The list after insert:')
    print(names)

# call the main function
main()