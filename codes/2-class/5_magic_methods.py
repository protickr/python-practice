class Employee: 
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

    def fullname(self)->str:
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Protick', 'Roy', 10000)
emp_2 = Employee('Test', 'User', 15000)

print(emp_1 + emp_2)
print(len(emp_1))


# special / magic / dunder methods 
# this methods emulates builtins behaviours in python 

# __repr__() is called when we do repr(obj)
# output of this method is meant to be used by developers to logging debugging 
# from this method return a string that can be used to recreate that object on which it was called
# you must implement this method even if you do not implement __str__()

# __str__() is called when we do str(obj)
# output of this method is meant to be used by the end user, readable representation of an object 

# we can also implement operator overloading with special methods 
# such as to overload the '+' operator's behavior for objects of a class we can 
# define __add__() method in that class  