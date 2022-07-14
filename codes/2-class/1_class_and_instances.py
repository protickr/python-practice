class Employee: 
    def __init__(self, first, last, pay):
        # constructor function 
        # self.instance_variables
        # self.attributes 
        # self.properties
        # self is the instance / object
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"

    # each method inside a class will take the instance as first argument automatically
    def fullname(self)->str:
        return f'{self.first} {self.last}'

emp_1 = Employee('Protick', 'Roy', 10000)
# when we create instance of a class that instance is passed to the constructor __init__ method automatically 
# as the first argument so we do not need to pass it explicitly
# the __init__() method will run automatically upon creating the instance

emp_2 = Employee('Test', 'User', 15000)

# instance variables contain data that is unque to each instance 
# emp_1.first = 'Protick'
# emp_1.last = 'Roy'
# emp_1.email = emp_1.first + emp_1.last + "@gmail.com"

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = emp_2.first + emp_2.last + "@gmail.com"

print(emp_1.email, emp_2.email)     # ProtickRoy@gmail.com TestUser@gmail.com

# print full name 
print(emp_1.fullname()) # passes the instance as first argument to the fullname() method automatically 
print(Employee.fullname(emp_1)) # we have pass the instance as first argument specifically when calling a 
                                # instance method by Class name 

