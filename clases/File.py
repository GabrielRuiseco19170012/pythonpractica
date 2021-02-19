import pickle
from clases.MyList import MyList
from os import path


class File(object):

    def __init__(self, usersDoc=None, materialDoc=None):
        self.usersDoc = usersDoc
        self.materialDoc = materialDoc

    def saveData(self, data):
        if self.usersDoc is not None:
            outfile = open(self.usersDoc, 'wb')
            pickle.dump(data, outfile)
            outfile.close()
            return True
        elif self.materialDoc is not None:
            outfile = open(self.materialDoc, 'wb')
            pickle.dump(data, outfile)
            outfile.close()
            return True
        else:
            return False

    def readData(self):
        newDict = MyList()
        if self.materialDoc is not None:
            if path.exists(self.materialDoc):
                infile = open(self.materialDoc, 'rb')
                newDict = pickle.load(infile)
                infile.close()
            return newDict
        elif self.usersDoc is not None:
            if path.exists(self.usersDoc):
                infile = open(self.usersDoc, 'rb')
                newDict = pickle.load(infile)
                infile.close()
            return newDict
        else:
            return False
