"""
25/25 points
Good job on this one. 
"""

"""
3. 
(The Triangle class) Design a class named Triangle that extends the
GeometricObject class defined below. The Triangle class contains:
    - Three float data fields named side1, side2, and side3 to denote the three
    sides of the triangle.
    - A constructor that creates a triangle with the specified side1, side2, and
    side3 with default values 1.0.
    - The accessor methods for all three data fields.
    - A method named getArea() that returns the area of this triangle.
    - A method named getPerimeter() that returns the perimeter of this triangle.
    - A method named __str__() that returns a string description for the triangle.


    class GeometricObject:
        def __init__(self, color = "green", filled = True):
            self.color = color
            self.filled = filled

        def getColor(self):
            return self.color

        def setColor(self, color):
            self.color = color

        def isFilled(self):
            return self.filled

        def setFilled(self, filled):
            self.filled = filled
    
        def toString(self):
            return "color: " + self.color + " and filled: " + str(self.filled)


    Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
"""
# import needed libraries
import math

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled

    def toString(self):
        return "color: " + self.color + " and filled: " + str(self.filled)

class Triangle(GeometricObject):
    # constructor for Triangle objects
    def __init__(self, color = "green", filled = True, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        
        # call super class's init method
        super().__init__(color, filled)
        
        # construct sides
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    # setters
    def set_side1(self, side1):
        self.side1 = side1

    def set_side2(self, side2):
        self.side2 = side2

    def set_side3(self, side3):
        self.side3 = side3

    # getters
    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    # getPerimeter function calculates the perimeter of the triangle object and returns the perimeter
    def getPerimeter(self):
        return (self.side1 + self.side2 + self.side3)
    
    # getArea function calculates the area of the triangle object and returns the area
    def getArea(self):
        # get half the perimeter to complete the area formula
        p = (self.getPerimeter() / 2)
        p1 = p - self.side1
        p2 = p - self.side2
        p3 = p - self.side3
        p_tot = p1 * p2 * p3

        # calculate the area
        area = math.sqrt(p * p_tot)

        # return the area
        return f"{area:.02f}"
    
    # print out the triangle object's properties
    def __str__(self):
        return "Color: " + self.color + "\nFilled: " + str(self.filled) + "\nArea: " + f"{str(self.getArea())}" + "\nPerimeter: " + f"{str(self.getPerimeter())}"
        
# main function creates a triangle object based on user inputs and then displays all of its properties once created
def main():
    # gather all user inputs for triangle creation
    s1 = float(input("Please enter side 1 length: "))
    s2 = float(input("Please enter side 2 length: "))
    s3 = float(input("Please enter side 3 length: "))
    num = '5'
    while num != '1' and num != '0':
        num = str(input("Please enter 1 for filled or 0 for not filled: "))
        if num == '0':
            filled_tri = False
        else:
            filled_tri = True
    color_tri = input("Please enter a color for the triangle: ")

    # create the triangle object
    triangle_obj = Triangle(color_tri, filled_tri, s1, s2, s3)

    # print out the triangle object
    print(triangle_obj)

main()