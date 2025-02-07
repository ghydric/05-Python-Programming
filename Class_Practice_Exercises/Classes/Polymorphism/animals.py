# the Mammal class rerpresents a generic mammal
class Mammal:
    # __init__ method accepts an argument for
    # the mammal's species
    def __init__(self, species):
        self.__species = species

    # the show_species method displays a message
    # indicating the mammal's species
    def show_species(self):
        print('I am a ', self.__species)
    
    # the make_sound method is the mammal's way
    # of making a generic sound
    def make_sound(self):
        print('Grrrr')

# the Dog class is a subclass of the Mammal class
class Dog(Mammal):
    # __init__ method calls the superclass's
    # __init__ method passing Dog as the species
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # the make_sound method overrides the superclass's
    # make_sound method
    def make_sound(self):
        print('Woof! Woof!')
    
# the Cat class is a subclass of the Mammal class
class Cat(Mammal):
    # __init__ method calls the superclass's
    # __init__ method passing Cat as the species
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # the make_sound method overrides the superclass's
    # make_sound method
    def make_sound(self):
        print('Meow! Meow!')

# define main function
def main():
    mammal = Mammal('Bigfoot')
    mammal.show_species()
    mammal.make_sound()

    cat = Cat()
    cat.show_species()
    cat.make_sound()

    dog = Dog()
    dog.show_species()
    dog.make_sound()

# call the main function
main()