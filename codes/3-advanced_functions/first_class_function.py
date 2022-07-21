# first class function 
# A programming language said to have first class function if treats functions as first-class citizens 

# first-class citizen 
# A first class citizen (sometimes called first-class objects) in a programming language is an entity which 
# supports all the operations generally available to other entities. These operations typically include being 
# passed as an argument, returned from a function and assigned to a variable. 

# if functions are treated as values


# higher order function 
# if a function takes another function as argument or return a function then it is called a higher order function
# map() is a higher order function becaues it takes a callback function as an argument.


# Example 1: first class function
# def square(x):
#     return x * x 

# f = square

# print(square)
# print(f(5))

# Example 2.1: higher order function
# def square(num):
#     return num * num

# def cube(num):
#     return num * num * num

# # map_to() is a higher order function as it takes mapper function's as an argument
# def map_to(mapper, nums):
#     res = []
#     for num in nums:
#         res.append(mapper(num))

#     return res


# nums = [1, 2, 3, 4]
# res = map_to(cube, nums)
# print(res)


# Example 2.2: Higher order function 
def log_message(msg):

    def print_log():
        print("Log: ", msg)

    # log_message() is a higher order function because it returns print_log() function
    return print_log

log = log_message("This message need to be logged !")
log()

