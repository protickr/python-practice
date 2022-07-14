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

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None: 
            self.employees = []
        else: 
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees: 
            print('-> {}'.format(emp.fullname()))


dev_1 = Developer('Protick', 'Roy', 10000, 'Python')
dev_2 = Developer('Test', 'User', 15000, 'JavaScript')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# python class inheritance 
# inheritance allows us to inherit attributes and methods from a parent class 
# we can create subclasses and get all the functionality of our parent class 
# and then we can overwrite or add completely new functionality witout affecting 
# the parent class in any way  

# when python does not find a specific method in a subclass then it walks up the 
# chain of inheritance until it finds what it is looking for 
# this chain is called Method Resolution Order (MRO)
# subclass also inherits parent's constructor method __init__()

# every class in python inherits from the base builtins.object 

# changing a class variable in subclass has no effect on the parent class 

# to help understand the MRO of a subclass we can use help() function 
# help(Subclass)

# isinstance(obj, Class)
# issubclass(ChildClass, ParentClass)

