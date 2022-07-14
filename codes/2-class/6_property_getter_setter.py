class Employee: 

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@email.com'

    # getter
    @property
    def fullname(self)->str:
        return f'{self.first} {self.last}'

    # setter
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')
        
    # deleter 
    @fullname.deleter 
    def fullname(self):
        print('Deleting fullname attribute!')
        self.first = None 
        self.last = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'


emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Protick Roy'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)
# property decorator allows us to define a method and access it like a attribute
