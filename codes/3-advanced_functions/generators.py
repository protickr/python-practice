# generators 
# def square_nums(nums):
#     result = []
#     for i in nums:
#         result.append(i * i) 
#     return result

# nums = [1, 2, 3, 4]
# snums = square_nums(nums)

# print(snums)

# to transform the previous example to generator 
def square_nums(nums):
    for i in nums:
        yield(i * i) 

nums = [1, 2, 3, 4]
snums = square_nums(nums)

# print(snums)

# generators do not hold the entire result in memory it yields one result at a time 
# it waits for us to ask for the next result 
# to ask for the next result we have to use 
# print(next(snums))
# print(next(snums))
# print(next(snums))
# print(next(snums))
# print(next(snums)) # StopIteration exception thrown as we reach the end of a generator; generator is exhausted
# yield returns a generator object

# for i in snums: 
#     print(i)
# for loop knows when to stop iteration or when generator is exhausted 

# while True: 
#     try:
#         print(next(snums))
#     except StopIteration as e: 
#         break


# list comprehension vs generator expression 
# sqr_nums = [ n*n for n in nums]
# print(sqr_nums)

gen_sqr_nums = (n*n for n in nums)
print(gen_sqr_nums)

# gen_sqr_nums holds a generator object on which we need to call next() to iterate through it. 
# or we can convert the generator object to a list 
li = list(gen_sqr_nums)
print(li)

# generator expression returns a generator object





