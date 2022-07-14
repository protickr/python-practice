# class variables 
# class variables are variables that are shared among all instance of a class 
# instance variables are unique to each instance 


class Employee: 
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"
        Employee.num_of_emps += 1
        # accessing num_of_emps with class reference because in no circumstance 
        # we want to the num_of_emps become specific to any instance

    def fullname(self)->str:
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.raise_amount so that we can access the general raise amount 
        # but if need be then we can reassign the raise amount using instance reference 
        # and access the raise_amount specific to that instance without chaning the code

emp_1 = Employee('Protick', 'Roy', 10000)
emp_2 = Employee('Test', 'User', 15000)

# we can access class variable through the class name itself or through any instance of the class 
# why ?
# because of scope chain 
# first it looks if the instance has a instance variable named raise_amount if not then it looks for 
# the variable in the class from which it was created

# Employee.raise_amount = 1.05

# emp_1.raise_amount = 1.05
# when we reassign a class variable with an instance reference then it overrides the class variable 
# and creates a new instnace variable with the same name as the class varaible 
# think of it as how global variable can be accessed in a local scope but re-assignment would lead to 
# creating a new variable in that local scope with the same name as the global variable 
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


# print(Employee.num_of_emps)

# any object's attributes 
# print(emp_1.__dict__)

# any class's namespace 
# print(Employee.__dict__)
