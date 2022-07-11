# The keyword def introduces a function definition. It must be followed by the function 
# name and the parenthesized list of formal parameters.
# The first statement of the function body can optionally be a string literal; 
# this string literal is the function’s documentation string, or docstring

# The execution of a function introduces a new symbol table used for the local variables of the function. 
# More precisely, all variable assignments in a function store the value in the local symbol table; 
# whereas variable references first look in the local symbol table, then in the local symbol tables 
# of enclosing functions, then in the global symbol table, and finally in the table of built-in names. 
# Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a 
# function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, 
# named in a nonlocal statement), although they may be referenced.


# The actual parameters (arguments) to a function call are introduced in the local symbol table of the 
# called function when it is called; thus, arguments are passed using call by value (where the value is 
# always an object reference, not the value of the object). 1 When a function calls another function, 
# or calls itself recursively, a new local symbol table is created for that call.

# A function definition associates the function name with the function object in the current symbol table. 
# The interpreter recognizes the object pointed to by that name as a user-defined function. 
# Other names can also point to that same function object and can also be used to access the function

# In fact, even functions without a return statement do return a value, albeit a rather boring one. 
# This value is called None 

# The return statement returns with a value from a function. return without an expression argument returns None. 
# Falling off the end of a function also returns None.


# simple function definition that has skipped body implementation by using pass keyword
# def func():
#     pass 

# functions with positional arguments
# def hello_func(name, greetings):
#     print(f'{greetings } { name }!')

# hello_func('Protick', 'Hi')
# Hi Protick!

# default argument values 
# The default values are evaluated at the point of function definition in the defining scope, so that
# def f(arg=i) says "make me a function f where the default value for arg is whatever i is right now". 
# At the time of defining the function, i=5.

def func(pos_arg, kwarg_1='No value', kwarg_2=True):
    print(pos_arg, kwarg_1, kwarg_2)


# func('Required Positional Argument',
#      kwarg_1='keyword argument for optional parameter kwarg_1')

# func(pos_arg = 'Required Positional Argument')
# func('This is for required positional parameter', pos_arg = 'Required Positional Argument')
func(kwarg_1 = 'keword arg', pos_arg = 'pos arg')

