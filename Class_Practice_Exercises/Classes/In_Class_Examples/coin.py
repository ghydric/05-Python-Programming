# import libraries
import random

# The Coin class simulates a coin that can be flipped
class Coin:

    # the __init__ method initializes the sideup data attribute with 'Heads'.
    def __init__(self):
        self.__sideup = 'Heads' # double underscore in front of attribute makes it private

    # the toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'
    # Otherwise, sideup is set to 'Tails'
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # the get_sideup method returns the value
    # referenced by sideup
    def get_sideup(self):
        return self.__sideup
    
# The main function
def main():
    # create an object from the Coin class
    my_coin = Coin()

    # sideup attribute is not private
    my_coin.__sideup = 'Tails'

    # display the side of the coin that is up
    print('This side is up:', my_coin.get_sideup())

    # toss the coin
    print('I am tossing the coin...')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

    # display the side of the coin that is up now
    print('Now, this side is up:', my_coin.get_sideup())

# call the main function
main()