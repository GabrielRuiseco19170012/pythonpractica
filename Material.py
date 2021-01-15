class Material:

    def __init__(self):
        self.nom = ''
        self.cantidad = 0
        self.lista = []

    def __str__(self):
        if len(self.lista) > 0:
            return str(len(self.lista)) + ' Registros'
        return self.nom + ' ' + str(self.cantidad)

    def setData(self, nombre, cantidad):
        self.nom = nombre
        self.cantidad = cantidad

    def getData(self):
        return self.nom, self.cantidad

    def getIndex(self, name):
        for obj in self.lista:
            if obj.nom == name:
                return self.lista.index(obj)

    def addObject(self, materoal):
        self.lista.append(materoal)
        return len(self.lista)

    def removeObject(self, index):
        self.lista.pop(index)
        return len(self.lista)

    def updateObject(self, index, materoal):
        self.lista[index] = materoal
        return True

    def getObject(self, index=None, name=None):
        if index != None:
            return self.lista[index]
        elif name != None:
            for obj in self.lista:
                if obj.nom == name:
                    return obj
        else:
            return None