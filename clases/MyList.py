class MyList(object):

    def __init__(self, myList=None):
        if myList is None:
            myList = []
        self.myList = myList

    def getmyList(self):
        return self.myList

    def __str__(self):
        if len(self.myList) > 0:
            return str(len(self.myList)) + ' registros'

    def getIndex(self, name):
        for obj in self.myList:
            if obj.name == name:
                return self.myList.index(obj)

    def addObject(self, myobject):
        self.myList.append(myobject)

    def removeObject(self, index=None, name=None):
        if index is not None:
            self.myList.pop(index)
            return True
        elif name is not None:
            c = 0
            for element in self.myList:
                if element.name == name:
                    self.myList.pop(c)
                    return True
                c += 1
        else:
            return False

    def updateObject(self, index, myobject):
        self.myList[index] = myobject

    def getObject(self, index=None, name=None):
        if index is not None:
            return self.myList[index]
        elif name is not None:
            for obj in self.myList:
                if obj.name == name:
                    return obj
        else:
            return None
