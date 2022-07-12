nl = [0,   1,   2,  3,  4,  5,  6,  7,  8,  9]
    # 0,   1,   2,  3,  4,  5,  6,  7,  8,  9 -> positive index
    # -10, -9, -8, -7, -6, -5, -4, -3, -2, -1 -> negative index

# print(nl[0], nl[-10])
# retrieving same element of the list using positive and negative index 
# 0 0

# print(nl[1:-1:2])
# nl[start:end:step]
# start from index 1 end at index -1 (not inclusive) with step size of 2 meaning 
# take every second element of the list extracted by start:end == 1:-1
# [1, 3, 5, 7]

# print(nl[3::])
# start from index 3 and take all elements including the last 
# [3, 4, 5, 6, 7, 8, 9]

# print(nl[:9])
# start index is not given so start from 0 and upto index 9 (not inclusive)
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

# we can also use negative step size. In that case list element extraction will start from the opposite of the 
# default direction (which is left to right)
# print(nl[-1:1:-1])
# [9, 8, 7, 6, 5, 4, 3, 2]

# print(nl[1:9:-1])
# []
# you can not just go to index 9 from index 1 at reverse order 

# reversing a list 
# print(nl[::-1])
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# slicing also applies to strings same as lists
