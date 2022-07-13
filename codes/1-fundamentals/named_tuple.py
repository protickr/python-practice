from collections import namedtuple

# tuples
# color = (55, 155, 255)
# print(color[0])

# named tuple 
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
print(color)        # Color(red=55, green=155, blue=255)
# The first parameter to the namedtuple() constructor sets the name of the generated class:
# here the name Color at the left of the assignment is just a reference to the returned class from 
# the namedtuple() constructor 

# accessing element of a namedtuple 
# by index 
print(color[0])     # 55

# by attribute
print(color.red)    # 55
