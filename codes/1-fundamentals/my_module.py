print('Imported my module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find a index of a value in a sequnce'''
    for i, value in enumerate(to_search):
        if value == target: 
            return i
            
    return -1
