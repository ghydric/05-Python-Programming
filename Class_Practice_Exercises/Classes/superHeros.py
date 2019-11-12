# create a SuperHero Class
class SuperHero:
    # __init__ method takes in hero name, real name, power list, and color list as arguments
    def __init__(self, h_name, r_name, list_obj_powers, list_obj_colors):
        self.__hero_name = h_name
        self.__real_name = r_name
        self.__powers = list_obj_powers
        self.__colors = list_obj_colors
    
    # set_hero_name takes in a name as an argument and sets it as the __hero_name attribute
    def set_hero_name(self, h_name):
        self.__hero_name = h_name
    
    # set_real_name takes in a name as an argument and sets it as the __real_name attribute
    def set_real_name(self, r_name):
        self.__real_name = r_name
    
    # set_powers takes in a list object and sets it as the __powers attribute
    def set_powers(self, list_obj_powers):
        self.__powers = power_list

    # set_colors takes in a list object and sets it as the __colors attribute
    def set_colors(self, list_obj_colors):
        self.__colors = color_list
    
    # get_hero_name returns the __hero_name attribute
    def get_hero_name(self):
        return self.__hero_name

    # get_real_name returns the __real_name attribute
    def get_real_name(self):
        return self.__real_name

    # get_powers returns the __powers attribute
    def get_powers(self):
        return self.__powers

    # get_colors returns the __colors attribute
    def get_colors(self):
        return self.__colors

