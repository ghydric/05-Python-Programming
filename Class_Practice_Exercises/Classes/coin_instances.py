# this program imports the simulation module and
# creates three instances of the Coin class

import coin

def main():
    # create three coin objects from the Coin class
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # display the side of each coin that is facing up
    print('I have three coins with these sides up:')
    print('Coin1: ',coin1.get_sideup())
    print('Coin2: ',coin2.get_sideup())
    print('Coin3: ',coin3.get_sideup())

    # toss the coins
    print('I am tossing all three coins...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # display the side of each coin that is now facing up
    print('Now, the three coins have these sides up:')
    print('Coin1: ',coin1.get_sideup())
    print('Coin2: ',coin2.get_sideup())
    print('Coin3: ',coin3.get_sideup())

# call the main function
main()