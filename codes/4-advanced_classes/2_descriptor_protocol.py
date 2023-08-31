# Descriptors are Python objects that implement a method of the descriptor protocol, which gives you 
# the ability to create objects that have special behavior when they’re accessed as 
# attributes of other objects
#
# methods of descriptor protocol
# __get__(self, obj, type=None) -> object
# __set__(self, obj, value) -> None
# __delete__(self, obj) -> None
# __set_name__(self, owner, name)

# If your descriptor implements just .__get__(), then it’s said to be a non-data descriptor. 
# If it implements .__set__() or .__delete__(), then it’s said to be a data descriptor. Note 
# that this difference is not just about the name, but it’s also a difference in behavior. 
# That’s because data descriptors have precedence during the lookup process,

# class Verbose_attribute():
#     def __get__(self, obj, type=None) -> object:
#         print("accessing the attribute to get the value")
#         return 42

#     def __set__(self, obj, value) -> None:
#         print("accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")

# class Foo():
#     attribute1 = Verbose_attribute()

# foo_obj = Foo()
# x = foo_obj.attribute1
# print(x)

# As a descriptor, it has binding behavior when it’s accessed using dot notation. 
# In this case, the descriptor logs a message on the console every time it’s accessed to get 
# or set a value
# so everytime when we use 'foo_obj.attribute1 to get' or 'foo_obj.attribute1 = to set' attribute1 of foo_obj the 
# bound __get__() or __set__() method will be executed

# the previous code example can also be written using '@property' decorator  
# class Foo():
#     @property
#     def attribute1(self) -> object:
#         print("accessing the attribute to get the value")
#         return 42

#     @attribute1.setter 
#     def attribute1(self, value):
#         print("accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")

# foo_obj = Foo()
# x = foo_obj.attribute1
# print(x)


# the previous code example can also be written using builtin 'property() function'
# which have method signature like this 
# property(fget=None, fset=None, fdel=None, doc=None) -> object
# property() returns a property object that implements the descriptor protocol. It uses 
# the parameters fget, fset and fdel for the actual implementation of the three 
# methods of the protocol.

# class Foo():
#     def getter(self) -> object:
#         print("accessing the attribute to get the value")
#         return 42
 
#     def setter(self, value):
#         print("accessing the attribute to set the value")
#         raise AttributeError("Cannot change the value")

#     attribute1 = property(getter, setter)

# foo_obj = Foo()
# x = foo_obj.attribute1
# print(x)

# how regular function in a class becomes methods ?
# The magic that transforms your obj.method(*args) call into method(obj, *args) is inside a .__get__() 
# implementation of the function object that is, in fact, a non-data descriptor. In particular, 
# the function object implements .__get__() so that it returns a bound method when you 
# access it with dot notation. 

# import types

# class Function(object):
#     ...
#     def __get__(self, obj, objtype=None):
#         "Simulate func_descr_get() in Objects/funcobject.c"
#         if obj is None:
#             return self
#         return types.MethodType(self, obj)
# types.MethodType(self, obj) returns a method(self)

# In the example above, when the function is accessed with dot notation, .__get__() is called and a 
# bound method is returned.
# This works for regular instance methods just like it does for class methods or static methods. 
# So, if you call a static method with obj.method(*args), then it’s automatically transformed into 
# method(*args). Similarly, if you call a class method with obj.method(type(obj), *args), 
# then it’s automatically transformed into method(type(obj), *args).

# how attributes are accessed with the lookup chain 
# In Python, every object has a built-in __dict__ attribute. This is a dictionary that contains all 
# the attributes defined in the object itself.
# A class is actually an object as well, so it will also have a __dict__ attribute that contains 
# all the attributes and methods of the class.
