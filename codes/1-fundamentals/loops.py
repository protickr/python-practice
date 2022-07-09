nums = [1 , 2, 3, 4, 5]

# for loops with iterables
#
# for num in nums: 
#     print(num)
# 1
# 2
# 3
# 4
# 5

# for with range(start, stop)
# range(stop) == range(0, stop)
# returns an iterable which starts from start value (inclusive) 
# and stops at end value (not inclusive)
# if single value is passed as an argument then start value becomes 0
#
# for i in range(1, 6):
#     print(i)

# 1
# 2
# 3
# 4
# 5

# while loop 
# x = 0
# while x < 10: 
#     print(x)
#     x += 1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# infinite loop
# x = 0
# while True: 
#     x += 1
#     if x == 4: 
#         continue

#     if x == 5:
#         break

#     print(x)

# 1
# 2
# 3
 
# else clause on loops 
# The else clause is executed if you exit a block normally, by hitting the loop 
# condition or falling off the bottom of a try block. 
# It is not executed if you break or return out of a block, or raise an exception. 
# It works for not only while and for loops, but also try blocks.

# You typically find it in places where normally you would exit a loop early, and running 
# off the end of the loop is an unexpected/unusual occasion. For example, if you're looping 
# through a list looking for a value:

values = [ 1, 2, 3, 4, 5, 6]
for value in values:
    if value == 5:
        print("Found it!")
        break
else:
    print("Nowhere to be found. :-(")