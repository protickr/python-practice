# iterable
# an iterable means it is something that can be looped over 
# for example a book with multiple pages can be considered as an iterable as we can turn the pages to traverse 
# through all the pages

# iterators 
# an iterator is an object with a state so that it remembers where it is during iteration and iterator also 
# know how to get their next value. They get their next value with a __next__() method 



# A list is iterable but not an iterator 
nums = [1, 2, 3, 4]
# for num in nums: 
#     print(num)

# you can also iterate through sets, tuples, dictionaries, generators, files etc,
#  
# how to determine if something is iterable ?
# to something to be an iterable it needs to have a method implemented in it called __iter__()
# print(dir(nums)) # __iter__ is lited in the result so it is an iterable
# __iter__() returns an iterator which for loop uses to iterate through the list 
# but list does not have a __next__() method so it is not an iterator 

# print(next(nums))
# TypeEroor: 'list' object is not an iterator

# when we run next() on an object it executes the __next__() defined on that object 
# when we run iter() on an object it executes the __iter__() defined on that object
# iterator is also an iterable but iterable is not always an iterator object 
# a generator is also an iterator but an iterator does not have to be a generator

# i_nums = nums.__iter__()
i_nums = iter(nums)
# print(i_nums, dir(i_nums))
# print(next(i_nums))     # 1

# iterator throws a StopIteration exception when the iterator is exhausted. 
# you can only go forward in an iterator, there is not resetting it, going back to previous entry or
# copying an iterator

# mimic the range() iterator 


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if(self.value >= self.end):
            raise StopIteration

        current = self.value
        self.value += 1
        return current

def my_range(start, end):
    while start < end:
        yield start 
        start += 1
    # generator raises StopIteration exception automatically 


nums = MyRange(0, 10)
g_nums = my_range(0, 10)

for num in g_nums: 
    print(num)
