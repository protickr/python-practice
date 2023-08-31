# list 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1
# my_list = [ item for item in nums ]
# print(nums, my_list)      # [1, 2, 3, 4, 5, 6, 7, 8, 9]    [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2
# my_list = [ n * n for n in nums ]
# print(my_list)            # [1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# lambda function equivalent of the last list comprehension
# my_list = list(map(lambda x: x * x, nums))
# print(my_list)            # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 3
# my_list = [ n for n in nums if n % 2 == 0 ]
# print(my_list)            # [2, 4, 6, 8]

# 4 
# nested for loops in list comprehension 
# my_list = [(letter, num) for letter in 'abc' for num in range(2)]
# print(my_list)              # [('a', 0), ('a', 1), ('b', 0), ('b', 1), ('c', 0), ('c', 1)]


# dictionary
# names = [ 'Peter', 'Bruce', 'Clerk', 'Jhony']
# heroes = [ 'Spiderman', 'Batman', 'Superman', 'Jack Sparrow' ]

# my_dict = { name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
# print(my_dict)      # {'Bruce': 'Batman', 'Clerk': 'Superman', 'Jhony': 'Jack Sparrow'}

# set comprehension
# nums = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 8, 9]
# my_set = { n for n in nums }
# print(my_set)       # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# generator expression 
nums = [1, 2, 3, 4]
my_gen = (n * n for n in nums)
# print(type(my_gen))     # &lt;class 'generator'&gt;
# print( list(my_gen))    # [1, 4, 9, 16]

# for n in my_gen: 
#     print(n)    # 1 4 9 16 each element on a new line
     

# tuple comprehension 
# there is no syntax for tuple comprehension but you can do it with tuple() constructor combined with 
# generator expression 
my_tup = tuple(my_gen)
print(my_tup)   # (1, 4, 9, 16)
