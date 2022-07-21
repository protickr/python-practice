import random
import time 
import memory_profiler as mem_profile # install it with pip install memory_profiler

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.process_time()
people = people_list(1000000)
t2 = time.process_time()

# t1 = time.process_time()
# people = people_generator(1000000)
# t2 = time.process_time()

# print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

# print 'Took {} Seconds'.format(t2-t1)
print ('Took ' + str(t2-t1) + ' Seconds')

# generator
# Memory (Before): [19.08203125]MB
# Memory (After) : [19.09375]MB
# Took 0.0 Seconds

# list
# Memory (Before): [19.05859375]MB
# Memory (After) : [289.921875]MB
# Took 1.96875 Seconds
