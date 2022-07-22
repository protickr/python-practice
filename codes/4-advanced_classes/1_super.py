class Adam(object):
    def print_me(self):
        print('class Adam')

class Eve(object):
    def print_me(self):
        print('class Eve')

class Father(Adam, Eve):
    def print_me(self):
        print('class Father')

class Mother(Adam, Eve):
    def print_me(self):
        print('class Mother')

class Child(Father, Mother):
    pass

#  |  Method resolution order:
#  |      Child
#  |      Father
#  |      Mother
#  |      Adam
#  |      Eve
#  |      builtins.object