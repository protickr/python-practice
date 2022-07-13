# name = 'Protick'
# age = 28 

# txt = 'I am {} my age is {}'.format(name, age)
# print(txt)      # I am Protick my age is 28


# element = '<{0}> {1} </{0}>'.format('p', 'paragraph text')
# print(element)


# person = { 'name': 'Protick', 'age': 28 }
# # txt = 'I am {0[name]} my age is {1[age]}'.format(person, person)

# txt = 'I am {0[name]} my age is {0[age]}'.format(person)
# print(txt)      # 


# info = ['Protick', 28]
# txt = 'I am {0[0]} my age is {0[1]}'.format(info)
# print(txt)      # I am Protick my age is 28


# with object attributes 
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

# p1 = Person('Protick', 28)
# txt = 'I am {0.name} my age is {0.age}'.format(p1)
# print(txt)      # I am Protick my age is 28


# with keyword argument and dictionary unpacking 
# txt = 'I am {name} my age is {age}'.format(name='Protick', age=28)
# print(txt)      # I am Protick my age is 28

# dictionary unpacking to generate keyword arguments 
# person = {'name': 'Protick', 'age': 28}
# txt = 'I am {name} my age is {age}'.format(**person)
# print(txt)      # I am Protick my age is 28

# number formatting 
# txt = '{0:02} '.format(8)
# print(txt)      # '08'

# txt = '{0:.4f}'.format(3.141592)
# print(txt)      # 3.1416

# txt = '{0:,.2f}'.format(10000000)
# print(txt)      # 10,000,000.00

# date formatting 
from datetime import datetime
a = datetime(2022, 1, 11)
birthday = '{0:%B %d, %Y}'.format(a)
print(birthday)     # January 11, 2022
