# list 
li = [3, 2, 1, 4]
# 1.
# li.sort()
# print(li)     # [1, 2, 3, 4]

# nli = sorted(li)
# print(nli)    # [1, 2, 3, 4]

# 2.
# li.sort(reverse=True)
# print(li)     # [4, 3, 2, 1]

# nli = sorted(li, reverse=True)
# print(nli)      # [4, 3, 2, 1]

# my_dict = {'name': 'Protick', 'age': 28, 'profession': 'Bekar'}
# sd = sorted(my_dict)
# print(sd)       # ['age', 'name', 'profession']
# returns a list of keys sorted alphabetically ascending order

# li = [-6, -5, -4, 1, 2, 3]
# nli = sorted(li, key=abs)
# print(nli)      # [1, 2, 3, -4, -5, -6]

from operator import attrgetter
class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

def sorter_func(emp):
    return emp.age


e1 = Employee('Corey', 26)
e2 = Employee('Jonas', 24)
emps = [e1, e2]

# sorted_emps = sorted(emps, key=sorter_func)
# print(sorted_emps[0].age, sorted_emps[1].age)   # 24 26

sorted_emps = sorted(emps, key=attrgetter('age'))
print(sorted_emps[0].age, sorted_emps[1].age)   # 24 26