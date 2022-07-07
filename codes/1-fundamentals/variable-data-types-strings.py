# print message to the console
# message = 'hello world'
# print(message)


# multi line string 
# retians white space and formatting as created
#
# message = '''hello 
# world!'''
# print(message)
#
# hello 
# world!




# string methods 
# message = "Hello world!"

# lower case
# print(message.lower()) 
# hello world!

# upper case 
# print(message.upper())
# HELLO WORLD!

# count number of occurance of a substring in a string 
# print(message.count("world"))
# 1
#
# print(message.count("o"))
# 2
#
# print(message.count("t"))
# 0

# find starting index of a substring in a string 
# only returns the first match 
# print(message.find("world"))
# 6
#
# print(message.find('universe'))
# -1 , no match found

# replace parts of a string with another string 
# print(message.replace("world", "universe"))
# Hello universe!
# does not mutate the original string; returns a new string 



# string concatanation 
# greetings = "Hey"
# name = "John"

# with (+) operator
# message = "Hello " + "world!"
# print(message)
# Hello world!

# with str.format() method / formatted string
# message = '{}, {}. Welcome! '.format(greetings, name)
# print(message)
# Hey, John. Welcome! 

# with f-string (template literals in JS)
# message = f'{greetings}, {name}. Welcome!'
# print(message)
# Hey, John. Welcome!



# helper functions 

# dir()
# print(dir(greetings))
# returns all methods and attributes that we have access to when using a variable

# help()
# print(help(str))
# returns doc string of a class 

