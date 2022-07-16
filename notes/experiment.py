# Class() -> __call__() -> __new__() -> __init__()

class Foo: 
    def __init__(self, x, y = 0):
        self.x = x
        self.y = y

Foo(10, 20)
print(type(Foo))