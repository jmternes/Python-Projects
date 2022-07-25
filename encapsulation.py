class Dog:
    def __init__(self):
        self._legs = 0
obj = Dog()
obj._legs = 4
print(obj._legs)
# above is protected variable, with output of 4


class Cat:
    def __init__(self):
        self.__thumbs = 0

    def getThumbs(self):
        print(self.__thumbs)
obj2 = Cat()
obj2.getThumbs()
# same process as protected, but private has 2 underscores and tells us we can only access the var within the class

