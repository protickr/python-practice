from datetime import datetime


class Employee: 
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"
        Employee.num_of_emps += 1


    def fullname(self)->str:
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod 
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # class method as alternative constructor 
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod 
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
            return False 
        return True

emp_1 = Employee('Protick', 'Roy', 10000)
emp_2 = Employee('Test', 'User', 15000)



# Employee.set_raise_amount(1.05)
# you can also call class methods with instance reference but that does not make sense and 
# it is rarely used 
# emp_1.set_raise_amount(1.01)
# this will change the class variable raise_amount same as invoking class method with the class name did

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


# class method as alternative constructor 
# emp_str_1 = 'John-Doe-20000'
# emp_3 = Employee.from_string(emp_str_1)
# print(emp_3.email)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

# 3 types of methods 
# regular methods, class methods, static methods

# regular method takes the instance reference as the first argument 

# class method takes the class reference as the first argument 
# class method can be created by adding a decorator '@classmethod' to the 
# top of a method definition inside a class 

# static method takes neither object nor class reference as first argument by default 
# they are just regular functions which have some logical conneciton to the class itself 
# static method does not depend on any class variable or instance variable 
# so if you need a method inside a class which does not need instance or class reference 
# then declare that method as static method
# static method can be declared with '@staticmethod' decorator
