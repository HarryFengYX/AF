#lib for fake memory
from concepts import *
class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.type = self.__class__.__name__

    def __repr__(self):
        return self.name

class rect:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = position(0,0)
        self.type = self.__class__.__name__

    def __repr__(self):
        return self.name

# class pygame_thing:
#     def __init__(self, obj):
#         self.name = obj.name
#         self.color = obj.color
#         self.position = obj.position
#         self.type = self.__class__.__name__
#
#     def __repr__(self):
#         return self.name

class screen:
    def __init__(self):
        self.position = position(0,0)
        self.name = 'the screen'
        self.width = 1920
        self.height = 1080
        self.type = self.__class__.__name__

    def __repr__(self):
        return self.name
