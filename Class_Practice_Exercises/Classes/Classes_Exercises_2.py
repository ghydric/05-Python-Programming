"""
2. Car Class
    Write a class named Car that has the following data attributes:
        • __year_model (for the car’s year model)
        • __make (for the make of the car)
        • __speed (for the car’s current speed)
        The Car class should have an __init__ method that accept the car’s year model and make
        as arguments. These values should be assigned to the object’s __year_model and __make
        data attributes. It should also assign 0 to the __speed data attribute.
        The class should also have the following methods:
        • accelerate
        The accelerate method should add 5 to the speed data attribute each time it is
        called.
        • brake
        The brake method should subtract 5 from the speed data attribute each time it is called.
        • get_speed
        The get_speed method should return the current speed.
    Next, design a program that creates a Car object, and then calls the accelerate method
    five times. After each call to the accelerate method, get the current speed of the car and
    display it. Then call the brake method five times. After each call to the brake method, get
    the current speed of the car and display it.
"""

# Car class
class Car:
    # __init__ method creates a Car object with a year_model, make, and speed attributes
    def __init__(self, year, make, speed = 0):
        self.__year_model = year
        self.__make = make
        self.__speed = int(speed)

    # accelerate method adds 5 to the __speed attribute each time it is called
    def accelerate(self):
        self.__speed += 5
    
    # brake method subtracts 5 from the __speed attribute each time it is called
    def brake(self):
        self.__speed -= 5
    
    # get_speed method returns value in the __speed attribute
    def get_speed(self):
        return self.__speed

# main function creates a Car object, accelerates five times, then brakes five times
# displaying the current speed after each accelerate and brake
def main():
    # create the Car object using user input
    my_car = Car(
        input('Enter the year of your car: '),
        input('Enter the make of your car: ')
    )

    # print the starting speed
    print(f'My car\'s starting speed is: {my_car.get_speed()}')

    # accelerate 5 times and display the speed after each accelerate
    for i in range(1,6):
        print('Accelerating now.')
        my_car.accelerate()
        print(f'My car is now going {my_car.get_speed()}mph.')
    
    # brake 5 times and display the speed after each brake
    for i in range(1,6):
        print('Braking now.')
        my_car.brake()
        print(f'My car is now going {my_car.get_speed()}mph.')

# call main function
main()