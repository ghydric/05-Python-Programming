"""
4. Employee Class
    Write a class named Employee that holds the following data about an employee in attributes: 
    name, ID number, department, and job title.
    Once you have written the class, write a program that creates three Employee objects to
    hold the following data:
​
Name            ID Number       Department      Job Title
Susan Meyers    47899           Accounting      Vice President
Mark Jones      39119           IT              Programmer
Joy Rogers      81774           Manufacturing   Engineer
​
The program should store this data in the three objects and then display the data for each
employee on the screen.
"""

# Employee class
class Employee:
    # __init__ creates an Employee object with Name,
    # ID_number, department, and job title attributes
    def __init__(self, name, id_num, dept, title):
        self.__name = name
        self.__id_number = id_num
        self.__department = dept
        self.__job_title = title
    
    # __str__ method displays the values in each attribute
    # for the Employee object
    def __str__(self):
        return f'Employee Name: {self.__name}\n' \
        f'Employee ID Number: {self.__id_number}\n' \
        f'Employee Department: {self.__department}\n' \
        f'Employee Job Title: {self.__job_title}'

    def set_name(self, name):
        self.__name = name
    
    def set_id_number(self, id_num):
        self.__id_number = id_num
        
    def set_department(self, dept):
        self.__department = dept
    
    def set_job_title(self, title):
        self.__job_title = title
    
    def get_name(self):
        return self.__name
    
    def get_id_number(self):
        return self.__id_number
    
    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

# main function creates 3 Employee objects from a dictionary,
# then displays their data
def main():
    # list holding each employee
    employee_list = []
    
    # dictionary holding all employee data
    employee_data = {
        1 : {
            'name' : 'Susan Meyers',
            'id_num' : 47899,
            'dept' : 'Accounting',
            'title' : 'Vice President'
        },
        2 : {
            'name' : 'Mark Jones',
            'id_num' : 39119,
            'dept' : 'IT',
            'title' : 'Programmer'
        },
        3 : {
            'name' : 'Joy Rogers',
            'id_num' : 81774,
            'dept' : 'Manufacturing',
            'title' : 'Engineer'
        }
    }

    # loop through each dictionary of employee data
    # and create Employee objects
    for i in range(1,4):
        employee = Employee(
            employee_data[i]['name'],
            employee_data[i]['id_num'],
            employee_data[i]['dept'],
            employee_data[i]['title']
        )

        # add employee to employee_list
        employee_list.append(employee)
    
    # loop through each employee in employee_list
    # and display all of their data
    for emp in employee_list:
        print(emp)
        print() # print extra blank line for readability

# call main function
#main()