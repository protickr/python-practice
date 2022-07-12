x = 'global x'
y = 'global y'
def outer():
    global x 
    x = 'outer x'
    y = 'outer y'

    def inner():
        # nonlocal x
        nonlocal y 
        y = 'inner y'
        x = 'inner x'
        print(x, y)
    
    inner()
    print(x, y)

outer()
print(x, y)


# global and nonlocal statement for a single variable name should not be combined for that variable name's 
# scope chain 
