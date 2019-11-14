# the Automobile class holds general data
# about an automobile in inventory

class Automobile:
    # __init__ method accepts arguments for the
    # make, model, mileage, and price. It initializes
    # the data attributes with these values
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    # the following methods are mutators (setters)
    # for the class's data attributes
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price
    
    # the following methods are accessors (getters)
    # for the class's data attributes
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price

# the Car class represents a car
# it is a subclass of the Automobile class
class Car(Automobile):
    # __init__ method accepts arguments for the car's
    # make, model, mileage, price, doors
    def __init__(self, make, model, mileage, price, doors):
        # call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument
        super().__init__(make, model, mileage, price)
        
        # initialize the __doors attribute
        self.__doors = doors

    # setter for doors
    def set_doors(self, doors):
        self.__doors = doors
    
    # getter for doors
    def get_doors(self):
        return self.__doors

# the Truck class represents a pickup truck.
# it is a subclass of the Automobile class.

class Truck(Automobile):
    # __init__ method accepts arguments for the
    # Truck's make, model, mileage, price, and drive type
    def __init__(self, make, model, mileage, price, drive_type):
        # call the superclass's __init__ method and pass
        # the required arguments.
        super().__init__(make, model, mileage, price)

        # initialize the drive type attribute
        self.__drive_type = drive_type
    
    # drive_type setter
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    # drive_type getter
    def get_drive_type(self):
        return self.__drive_type

# the SUV class represents a sport utility vehicle.
# It is a subclass for the Automobile class
class SUV(Automobile):
    # __init method accepts arguments for the SUV's
    # make, model, mileage, price, and passenger capacity
    def __init__(self, make, model, mileage, price, pass_cap):
        # call the superclass's __init__ method and pass
        # the required arguments
        super().__init__(make, model, mileage, price)

        # initialize the passenger capacity attribute
        self.__pass_cap = pass_cap
    
    # passenger capacity setter
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap
    
    # passenger capacity getter
    def get_pass_cap(self):
        return self.__pass_cap