# This program creates a Car, Truck, and SUV object

import vehicles

def main():
    # create Car object
    car = vehicles.Car('Bugatti', 'Veyron', 0, 3000000, 2)

    # create a Truck object
    truck = vehicles.Truck('Dodge', 'Power Wagon', 0, 57000, '4WD')

    # create a SUV object
    suv = vehicles.SUV('Jeep', 'Wrangler', 200000, 5000, 4)

    print('VEHICLE INVENTORY')
    print('=================')

    # display the car data
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price', car.get_price())
    print('Number of doors:', car.get_doors())
    # display the truck data
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price', truck.get_price())
    print('Drive Type:', truck.get_drive_type())
    # display the SUV data
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price', suv.get_price())
    print('Number of doors:', suv.get_pass_cap())

    # Helpful functions below:
    #print(help(vehicles.SUV))
    #print(suv.__dict__)
    #suv_dict = suv.__dict__
    #print(type(suv_dict))

# call main function
main()