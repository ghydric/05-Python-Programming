# this program demonstrates polymorphism

import animals

def main():
    # create a Mammal object, a Dog object, and a Cat object
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    # display information about each one
    print('Here are some animals and')
    print('the sounds they make.')
    print('-------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

# the show_mammal_info function accepts an object of type Mammal
# as an argument, and calls its show_species and make_sound methods
def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a Mammal!')

# call main function
main()