# Dictionary is an unordered collection of key value pairs where value can be anything and 
# dictionaries are indexed by keys, which can be any immutable type; 
# strings and numbers can always be keys. 
# Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple 
# contains any mutable object either directly or indirectly, it cannot be used as a key. 
# You can’t use lists as keys, since lists can be modified in place using index assignments, 
# slice assignments, or methods like append() and extend().
# It is best to think of a dictionary as a set of key: value pairs, 
# with the requirement that the keys are unique (within one dictionary).

# declaring a dictionary 
# 1
# student = {}

# 2
# student = dict()

# 3 
# The dict() constructor builds dictionaries directly from sequences of key-value pairs

# print(type(student))
# <class 'dict'>

john = { 'name': 'John', 'age': 28, 'country': 'Bangladesh' }

# access dictionary entries
# dict_obj[key]
# returns value against a key or throws a KeyError if key does not exist
# print(john['name'])
# John

# inserting or updating a new entry 
# john['age'] = 27
# print(john)
# {'name': 'John', 'age': 27, 'country': 'Bangladesh'}
#
# insert value against a key
# john['language'] = 'Bangla'
# print(john)
# {'name': 'John', 'age': 28, 'country': 'Bangladesh', 'language': 'Bangla'}




# dictionary methods

# dict.get(key, default_value)
# print(john.get('name'))
# John

# returns None or default value if key does not exist
# print(john.get('language'))
# None
#
# print(john.get('language', 'Bangla'))
# Bangla

# dict.update({})
# insert and update entries of a dictionary 
# inserts new key: value pair if key does not exist in dictionary or update if key exists 
# john.update({'language': 'Bangla', 'country': 'Heaven'})
# print(john)
# {'name': 'John', 'age': 28, 'country': 'Heaven', 'language': 'Bangla'}

# dict.pop(key)
# pops and returns value from a dictionary against the provided key or throws KeyError if key does not exist
# x = john.pop('age')
# print(x)
# 28
#
# x = john.pop('language')
# KeyError: 'language'

# dict.keys()
# returns a list of keys 
# keys = john.keys()
# print(keys)
# dict_keys(['name', 'age', 'country'])

# dict.values()
# returns a list of values 
# values = john.values()
# print(values)
# dict_values(['John', 28, 'Bangladesh'])

# dict.items()
# returns a list of tuples (key, value) 
# items = john.items()
# print(items)
# dict_items([('name', 'John'), ('age', 28), ('country', 'Bangladesh')])

# dict.popitem()
# pops and returns last key value as a tuple: (key, value) 
# last = john.popitem()
# print(last)
# ('country', 'Bangladesh')

# dict.clear()
# clears dictionary
# d = john.clear()
# print(d, john)
# None {}

# len(dict_obj)
# returns length of a dictionary object 
# print(len(john))
# 3

# del dict_obj[key]
# deletes key: value from a dictionary 
# del john['age']
# print(john)
# {'name': 'John', 'country': 'Bangladesh'}
