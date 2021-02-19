from pymongo import MongoClient


class MongoConect:

    def __init__(self):
        self.CLIENT = MongoClient('localhost', 27017)
        print("Established Connection with MongoDB")
    # "mongodb+srv://Admin:123asterisco@practica1.hjadu.mongodb.net/pymongo?retryWrites=true&w=majority")

    def createMongo(self, collection, x):
        collection.insert_one(x)

    def readMongo(self, collection, arg1, arg2):
        self.results = collection.find(arg1, arg2)
        self.all = '\n'.join([str(r) for r in self.results])
        return self.all

    def updateMongo(self, collection, arg1, arg2):
        collection.update_one(arg1, arg2)
        # print(str(arg1), "\n" + str(arg2))

    def deleteMongo(self, collection, **kwargs):
        collection.delete_one(kwargs)
