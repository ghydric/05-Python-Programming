# this program demonstrates the Car class

import vehicles

def main():
    # create a Car object
    # The car is a 2007 Audi with 12,500 miles,
    # priced at $21,500.00, and has 4 doors
    user_car = vehicles.Car('Audi','A3',12500, 21500.00, 4)

    # display the car's data
    print('Make:', user_car.get_make())
    print('Model:', user_car.get_model())
    print('Mileage:', user_car.get_mileage())
    print('Price', user_car.get_price())
    print('Number of doors:', user_car.get_doors())

# call the main function
main()