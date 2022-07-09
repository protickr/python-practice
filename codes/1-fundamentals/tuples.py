# tuples 

# declaraing a tuple 
# 1
# months = ()
# 
# 2
# months = tuple()
# 
# print(type(months))
# <class 'tuple'>

# A tuple consists of a number of values separated by commas
# Though tuples may seem similar to lists, they are often used in different situations 
# and for different purposes. Tuples are immutable, and usually contain a heterogeneous 
# sequence of elements that are accessed via unpacking or indexing or even by attribute in 
# the case of namedtuples. 
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

# single element tuple 
# new_tuple = (123,)
# print(new_tuple)
# (123,)

# empty tuple 
# months = ()
# print(months, type(months))
# () <class 'tuple'>

# packing 
# t = 12345, 54321, 'hello!'
# print(t, type(t))
# (12345, 54321, 'hello!') <class 'tuple'>

# unpacking 
# t = 12345, 54321, 'hello!'
# a, b, c = t
# print(a, b, c)
# 12345 54321 hello!

new_tuple = (12345, 54321, 'hello!')

# retrieving tuple elements by index
# print(new_tuple[-1])
# hello!

# assignment operation on tuple throws error 

# tuple methods 

# tuple.count(value)
# returns number of times an element is present in the tuple
# print(new_tuple.count("hello!"))
# 1

# tuple.index()
# returns index of an element in a tuple or exception
# print(new_tuple.index('hello!'))
# 2
# print(new_tuple.index('welcome'))
# ValueError: tuple.index(x): x not in tuple

# two tuples can be concatenated by + operation 
# extended_tuple = new_tuple + (1, 2, 3)
# print(extended_tuple)
# (12345, 54321, 'hello!', 1, 2, 3)

# tuple initialization 
# nt = ('hi', ) * 5
# print(nt)
# ('hi', 'hi', 'hi', 'hi', 'hi')
# interesting but I do not know where to use this technique
