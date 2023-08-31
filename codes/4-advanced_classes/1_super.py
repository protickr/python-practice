# class Adam(object):
#     def print_me(self):
#         print('class Adam')

# class Eve(object):
#     def print_me(self):
#         print('class Eve')

# class Father(Adam, Eve):
#     def print_me(self):
#         print('class Father')

# class Mother(Adam, Eve):
#     def print_me(self):
#         print('class Mother')

# class Child(Father, Mother):
#     pass

# #  |  Method resolution order:
# #  |      Child
# #  |      Father
# #  |      Mother
# #  |      Adam
# #  |      Eve
# #  |      builtins.object


# dependency injection example by Raymond Hettinger
# class Robot(object):
#     def left(self):
#         print("walking left")
#     def right(self):
#         print("walking right")

# class MyRobot(Robot):
#     def clean(self):
#         super().left()
#         super().right()

# # dependency 
# class MockRobot(Robot):
#     def left(self):
#         print("mock left")
#     def right(self):
#         print("mock right")

# # injection 
# class MyRobotTestable(MyRobot, MockRobot):
#     pass

# super() call's  your children's ancestor
