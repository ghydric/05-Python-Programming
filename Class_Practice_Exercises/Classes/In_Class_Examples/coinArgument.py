# this program passes a Coin object as an argument to a function

import coin

#main function
def main():
    # create a Coin object
    my_coin = coin.Coin()

    # This will display 'Heads'
    print(my_coin.get_sideup())

    # pass the object to the flip function
    flip(my_coin)

    # this maight display 'Heads' or 'Tails'
    print(my_coin.get_sideup())

# the flip function flips a coin
def flip(coin_obj):
    coin_obj.toss()

# call main function
main()