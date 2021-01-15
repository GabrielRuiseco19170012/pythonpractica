class Usuario:

    def __init__(self):
        self.nom = ''
        self.edad = ''
        self.lista = []

    def __str__(self):
        if len(self.lista) > 0:
            return str(len(self.lista)) + ' Registros'
        return self.nom + ' ' + str(self.edad)

    def setData(self, nombre, edad):
        self.nom = nombre
        self.edad = edad

    def getData(self):
        return self.nom, self.edad

    def getIndex(self, name):
        for obj in self.lista:
            if obj.nom == name:
                return self.lista.index(obj)

    def addObject(self, usuario):
        self.lista.append(usuario)
        return len(self.lista)

    def removeObject(self, index):
        self.lista.pop(index)
        return len(self.lista)

    def updateObject(self, index, usuario):
        self.lista[index] = usuario
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