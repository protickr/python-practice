# closure 
# In simple terms, a closure is an inner function that remember and has 
# access to variabless in the local scope in which it was created, 
# even after the outer function has finished executing

# Exmaple 1: 
# def outer_func():
#     message = 'hi'

#     def inner_func():
#         print(message)

#     return inner_func

# func = outer_func()
# func()

# Example 2: 
# def tag(t):
#     def content(c):
#         return f'<{t}>{c}</{t}>'

#     return content

# h1 = tag('h1')
# h1_element = h1('This is heading level 1')
# print(h1_element) # <h1>This is heading level 1</h1>


# Example 3: 
# logging basic functions
# takes a function and inject logging functionality in it 
import logging 
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f'Running: {func.__name__} with arguments: {args}')
        print(func(*args))
        
    return log_func
    

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

log_add = logger(add)
log_mul = logger(multiply)

log_add(10, 20)
log_mul(10, 20)
