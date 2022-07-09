# lists
# list is a collection of elements 
# list is not actually array because list can have heterogenous data as list element. 
# takes a lot more space than arrays 
# array.array and numpy.ndarray are arrays. 

# lists can have different types of data as element. 
# lists can have lists as elements
# list can have dict as elements 
# list can have all of the above at the same list at the same time. 
# list retains order 
# lists are mutable

# declaraing a list 
# 1
# students = []

# # 2
# students = list()

# print(type(students))
# <class 'list'>

# list methods 
courses = ['Bangla', 'English', 'Math']

# length of a list 
# print(len(courses))
# 3

# access list element by index
# print(courses[1])
# English

# access list item by negative index 
# negative index starts from -1 from the end of a list
# print(courses[-1])
# Math

# update list element by index 
# courses[-1] = 'Mathematics'
# print(courses)
# ['Bangla', 'English', 'Mathematics']

# list slicing / new list from a list by start index (inclusive) and end index ( not inclusive ) 
# new_list = courses[ 1 : 2 ]
# print(new_list)
# ['English']
#
# omitting start index will default to 0 
# print(courses[:2])
# ['Bangla', 'English']
#
# omitting end index will return all elements including the last element of a list
# print(courses[0:])
# ['Bangla', 'English', 'Math']
#

# list.append( value )
# append new element at the end of a list 
# courses.append('History')
# print(courses)
# ['Bangla', 'English', 'Math', 'History']

# list.insert(index, value)
# append element at the specified index and shifts the current element and the consecutive elements to the right 
# courses.insert(1, 'History')
# print(courses)
# ['Bangla', 'History', 'English', 'Math']
# the 'value' can also be a list and in that case it will be placed in the list as an element

# list.extend([new, list])
# unpacks the list argument's elements and append them to the list 
# new_courses = ['History', 'Physics']
# courses.extend(new_courses)
# print(courses)
# ['Bangla', 'English', 'Math', 'History', 'Physics']

# list.pop(index)
# pop a value from a list
# popped_value = courses.pop()
# print(popped_value)
# Math
# pop value from a list by index
# print(courses.pop(-2))
# English
# print(courses)
# ['Bangla', 'Math']

