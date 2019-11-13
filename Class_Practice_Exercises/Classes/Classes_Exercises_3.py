"""
3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods. Also, write a program that creates
    three instances of the class. One instance should hold your information, and the other two
    should hold your friends’ or family members’ information.
"""

# Personal_Info class
class Personal_Info:
    # __init__ method creates a Personal_Info object with
    # name, address, age, and phone number attributes
    def __init__(self, name, address, age, number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = number
    
    # set_name sets the __name attribute
    def set_name(self, name):
        self.__name = name

    # set_address sets the __address attribute
    def set_address(self, address):
        self.__address = address

    # set_age sets the __age attribute
    def set_age(self, age):
        self.__age = age
    
    # set_phone_number sets the __phone_number attribute
    def set_phone_number(self, number):
        self.__phone_number = number

    # get_name gets the value in the __name attribute
    def get_name(self):
        return self.__name

    # get_address gets the value in the __address attribute
    def get_address(self):
        return self.__address

    # get_age gets the value in the __age attribute
    def get_age(self, age):
        return self.__age
    
    # get_phone_number gets the value in the __phone_number attribute
    def get_phone_number(self):
        return self.__phone_number

    # __str__ displays all the values in each of the attributes 
    # from the Personal_Info object
    def __str__(self):
        return f'Name: {self.__name}\n' \
        f'Address: {self.__address}\n' \
        f'Age: {self.__age}\n' \
        f'Phone Number: {self.__phone_number}'

# main function creates 3 Personal_Info objects using user input
# and then displays each instance
def main():
    # create a blank list to hold each Personal_Info object
    pers_info_objs = []

    # loop 3 times to create 3 Personal_Info objects
    # and append each to the pers_info_objs list
    for i in range(1,4):
        # create the Personal_Info object using user input
        info = Personal_Info(
            input('Info ' + str(i) + ', Enter your name: '),
            input('Info ' + str(i) + ', Enter your address: '),
            input('Info ' + str(i) + ', Enter your age: '),
            input('Info ' + str(i) + ', Enter your phone number: ')
        )
        # append the Personal_Info object to the list
        pers_info_objs.append(info)
    
    # add a blank line for ease of reading
    print()
    
    # loop through the pers_info_objs list and display each object's attributes
    for item in pers_info_objs:
        print(item)
        print()

# call main function
main()