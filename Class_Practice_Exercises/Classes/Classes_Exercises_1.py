"""
1. Pet Class
    Write a class named Pet, which should have the following data attributes:
        • __name (for the name of a pet)
        • __animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’,
        and ‘Bird’)
        • __age (for the pet’s age)
        The Pet class should have an __init__ method that creates these attributes. It should also
        have the following methods:
        • set_name
        This method assigns a value to the __name field.
        • set_animal_type
        This method assigns a value to the __animal_type field.
        • set_age
        This method assigns a value to the __age field.
        • get_name
        This method returns the value of the name field.
        • get_type
        This method returns the value of the type field.
        • get_age
        This method returns the value of the age field.
    Once you have written the class, write a program that creates an object of the class and
    prompts the user to enter the name, type, and age of his or her pet. This data should be
    stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name,
    type, and age and display this data on the screen.
"""

# pet class
class Pet:
    # __init__ method creates a Pet object with a name, animal type, and age
    def __init__(self, name, animalType, age):
        self.__name = name
        self.__animal_type = animalType
        self.__age = age
    
    # set_name method assigns the name of the Pet object
    def set_name(self, name):
        self.__name = name

    # set_animal_type assigns the animal type to the Pet object
    def set_animal_type(self, animalType):
        self.__animal_type = animalType

    # set_age assigns an age to the Pet object
    def set_age(self, age):
        self.__age = age

    # get_name returns the value in the __name attribute
    def get_name(self):
        return self.__name

    # get_type returns the value in the __animal_type attribute
    def get_type(self):
        return self.__animal_type

    # get_age returns the value in the __age attribute
    def get_age(self):
        return self.__age

# main function creates a Pet object based on user input
def main():
    # create Pet object using user input
    my_pet = Pet(
        input('Enter the name of your pet: '),
        input('Enter the type of animal: '),
        input('Enter the age of your pet: ')
    )
    # display my pet's attributes using the accessor methods
    print(f'My pet\'s name is: {my_pet.get_name()}.')
    print(f'{my_pet.get_name()} is a: {my_pet.get_type()}.')
    print(f'{my_pet.get_name()} is {my_pet.get_age()} years old.')

# call main function
main()