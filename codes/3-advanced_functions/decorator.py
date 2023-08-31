# decorators 
# a decorator is a function that takes another function as an argument, adds some kind of functionality
# and then returns another function 
# without altering the source code of original function that we passed in to the decorator 

# def decorator_function(original_function):
#     def wrapper_function():
#         print(f'wrapper function ran before executing {original_function.__name__}')
#         return original_function()

#     return wrapper_function

# def display():
#     print('display function ran')

# display = decorator_function(display)
# display()

# in python we can achieve the same as the previous code example by, 
# def decorator_function(original_function):
#     def wrapper_function():
#         print(f'wrapper function ran before executing {original_function.__name__}')
#         return original_function()

#     return wrapper_function

# @decorator_function
# def display():
#     print('display function ran')

# # @decorator_function
# def display_info(name, age):
#     print(f'display info ran with arguments {name, age}')

# # display()
# display_info('John', 25)

# so @decorator keyword replaces original function with wrapper function and takes original function as 
# its first argument automatically 
# so now, to pass argument to the wrapper function we need to define wrapper function with parameters that 
# can receive multiple positional and keyword arguments 
# we can do so by, 

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f'wrapper function ran before executing {original_function.__name__}')
#         return original_function(*args, **kwargs)

#     return wrapper_function

# @decorator_function
# def display():
#     print('display function ran')

# @decorator_function
# def display_info(name, age):
#     print(f'display info ran with arguments {name, age}')

# display()
# display_info('John', 25)


# python classes as decorators 
# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args, **kwds):
#         print(f'call method executed before executing {self.original_function.__name__}')
#         return self.original_function(*args, **kwds)


# @decorator_class
# def display():
#     print('display function ran')

# @decorator_class
# def display_info(name, age):
#     print(f'display info ran with arguments {name, age}')

# display()
# display_info('John', 25)



# # practical examples of decorators 
# from functools import wraps
# def logger(orig_func):
#     import logging
#     logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info('ran with arguments {} and keword arguments {}'.format(args, kwargs))
#         return orig_func(*args, **kwargs)
#     return wrapper


# def timer(orig_func):
#     import time

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         execution_time = time.time() - t1
#         print(f'{orig_func.__name__} ran in {execution_time} seconds')
#         return result
#     return wrapper


# @timer
# @logger
# def display():
#     print('display function ran')

# @timer
# @logger
# def display_info(name, age):
#     print(f'display info ran with arguments {name, age}')

# display()
# display_info('John', 25)


# decorators that take arguments 
from functools import wraps

def prefix_decorator(prefix):
    def decorator_function(original_function):

        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            print(f'{prefix}: {original_function.__name__}')
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING: ')
def display_info(name, age):
    print(f'display info ran with arguments {name, age}')

display_info('John', 25)