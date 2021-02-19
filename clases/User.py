from clases.MyList import MyList


class User:

    def __init__(self, name='', lastName='', age=''):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.mList = MyList()

    def setData(self, name=None, lastName=None, age=None):
        if name is not None:
            self.name = name
        if lastName is not None:
            self.lastName = lastName
        if age is not None:
            self.age = age

    def getData(self):
        return self.name, self.age

    def getMaterial(self):
        return self.mList
