import json
from clases.Material import Material
from clases.User import User
from clases.MyList import MyList
from clases.File import File
from datetime import date
from clases.MySqlConnection import DatabaseMySql
from clases.PyMongoConnection import MongoConect
import copy
from os import system, name as sysname

userList: MyList = MyList()
matList: MyList = MyList()
connection = DatabaseMySql()
connectionMDB = MongoConect()
DB = connectionMDB.CLIENT['pymongo']

f1 = File(usersDoc="User.obj")
f2 = File(usersDoc="Material.obj")
try:
    userList = f1.readData()
except Exception as e:
    print("error " + str(e))
try:
    matList = f2.readData()
except Exception as e:
    print("error " + str(e))


class Interface:

    def __init__(self):
        self.selectorDB = "2"

    @staticmethod
    def clear():
        # for windows
        if str(sysname) == "nt":
            _ = system("cls")
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system("clear")

    @staticmethod
    def newUser():
        Interface.clear()
        name = input("Ingrese el nombre del usuario: ")
        lastName = input("Ingrese el apellido del usuario: ")
        age = int(input("Ingrese la edad del usuario: "))
        return name, lastName, age

    def saveUser(self):
        try:
            name, lastName, age = Interface.newUser()
            obj = User(name=name, lastName=lastName, age=int(age))
            if self.selectorDB == "1":
                Interface.localSaveU()
            elif self.selectorDB == "2":
                connection.sendData(obj, table='Users')
            elif self.selectorDB == "3":
                MongoConect.createMongo(connectionMDB, DB['Users'], Interface.my_dict(obj))
        except Exception as err:
            print(err)

    @staticmethod
    def localSaveU(obj):
        userList.addObject(obj)
        file = File(usersDoc="User.obj")
        file.saveData(userList)

    @staticmethod
    def newMaterial():
        Interface.clear()
        name = input("Ingrese el nombre del material: ")
        quantity = input("Ingrese la cantidad de material: ")
        return name, quantity

    def saveMaterial(self):
        try:
            name, quantity = Interface.newMaterial()
            obj = Material(name=name, quantity=int(quantity))
            if self.selectorDB == "1":
                Interface.localSaveM()
            elif self.selectorDB == "2":
                connection.sendData(obj, table="Materials")
            elif self.selectorDB == "3":
                MongoConect.createMongo(connectionMDB, DB['Materials'], Interface.my_dict(obj))
        except Exception as err:
            print(err)

    @staticmethod
    def localSaveM(obj):
        matList.myList.append(obj)
        file = File(materialDoc="Material.obj")
        file.saveData(matList)

    def lendMaterial(self):
        try:
            Interface.clear()
            n = input("\nIngrese el usuario: ")
            nm = input("\nIngrese el material: ")
            q = int(input("\nIngrese la cantidad: "))
            if self.selectorDB == "1":
                Interface.localLend(n, nm, q)
            elif self.selectorDB == "2":
                Interface.mySqlLend(n, nm, q)
            elif self.selectorDB == "3":
                Interface.mongoLend(n, nm, q)
        except Exception as err:
            print(err)

    @staticmethod
    def localLend(n, nm, q):
        u: User = userList.getObject(name=n)
        ui = userList.getIndex(n)
        if u is not None:
            m: Material = matList.getObject(name=nm)
            mi = matList.getIndex(nm)
            if m is not None:
                mu: Material = copy.copy(m)
                mu.setData(quantity=q, date_out=str(date.today()))
                u.mList.addObject(mu)
                userList.updateObject(ui, u)
                m.setData(quantity=(int(m.quantity) - q))
                matList.updateObject(mi, m)
                file = File(usersDoc="User.obj")
                file.saveData(userList)
                file2 = File(materialDoc="Material.obj")
                file2.saveData(matList)
            else:
                print('\nMaterial no encontrado')
        else:
            print('\nUsuario no encontrado')

    @staticmethod
    def mySqlLend(n, nm, q):
        mat = connection.getOneData("Name", "Materials", nm)
        usr = connection.getOneData("Name", "Users", n)
        obj = {"uid": usr[0], "mid": mat[0], "quantity": q}
        print(obj)
        connection.sendData(obj, table="UserMaterials")
        connection.updateData("Materials", "id", "Quantity", (mat[2] - q), mat[0])

    @staticmethod
    def mongoLend(n, nm, q):
        kwargs = {"arg1": {"name": n}, "arg2": {"_id": 0}}
        usr = MongoConect.readMongo(connectionMDB, DB['Users'], **kwargs)
        data = json.loads(usr.replace("'", '"'))
        kwargs2 = {"arg1": {"name": nm}, "arg2": {"_id": 0, "date_out": 0, "date_in": 0}}
        mater = MongoConect.readMongo(connectionMDB, DB['Materials'], **kwargs2)
        print(mater)
        data2 = json.loads(mater.replace("'", '"'))
        newQuantity = (data2['quantity'] - q)
        data2.update({'quantity': q})
        print(data2)
        data['mList']['myList'].append(data2)
        newData = data['mList']['myList']
        print(newData)
        kwargs3 = {"arg1": {"name": n}, "arg2": {"$set": {"mlist.myList": newData}}}
        MongoConect.updateMongo(connectionMDB, DB['Users'], **kwargs3)
        kwargs4 = {"arg1": {"name": nm}, "arg2": {"$set": {"quantity": newQuantity}}}
        MongoConect.updateMongo(connectionMDB, DB['Materials'], **kwargs4)

    def returnMaterial(self):
        try:
            Interface.clear()
            n = input("\nIngrese el usuario: ")
            nm = input("\nIngrese el material: ")
            q = int(input("\nIngrese la cantidad: "))
            if self.selectorDB == "1":
                Interface.localReturn(nm, q, n)
            elif self.selectorDB == "2":
                Interface.returnMySql(n, q)
            elif self.selectorDB == "3":
                Interface.mongoReturn(n, nm, q)
        except Exception as err:
            print(err)

    @staticmethod
    def localReturn(nm, q, n):
        u: User = userList.getObject(name=n)
        ui = userList.getIndex(n)
        if u is not None:
            m: Material = matList.getObject(name=nm)
            mi = matList.getIndex(nm)
            if m is not None:
                mu: Material = u.mList.getObject(name=nm)
                mui = u.mList.getIndex(nm)
                mu.setData(quantity=(int(mu.quantity) - q))
                if int(mu.quantity) <= 0:
                    u.mList.removeObject(name=nm)
                    m.setData(date_in=str(date.today()))
                    matList.updateObject(mi, m)
                else:
                    u.mList.updateObject(mui, mu)
                userList.updateObject(ui, u)
                m.setData(quantity=(int(m.quantity) + q))
                matList.updateObject(mi, m)
                file = File(usersDoc="User.obj")
                file.saveData(userList)
                file2 = File(materialDoc="Material.obj")
                file2.saveData(matList)
            else:
                print('\nMaterial no encontrado')
        else:
            print('\nUsuario no encontrado')

    @staticmethod
    def returnMySql(nm, n, q):
        mat = connection.getOneData("Name", "Materials", nm)
        connection.updateData("Materials", "id", "Quantity", (mat[2] + q), mat[0])
        usr = connection.getOneData("Name", "Users", n)
        usrMat = connection.getUMList(mat[0], usr[0])
        connection.updateData("UserMaterials", "id", "Quantity", (usrMat[3] - q), usrMat[0])
        usrMat = connection.getUMList(mat[0], usr[0])
        if usrMat[3] == 0:
            connection.deleteData("UserMaterials", "id", usrMat[0])

    @staticmethod
    def mongoReturn(n, nm, q):
        kwargs = {"arg1": {"name": nm}, "arg2": {"_id": 0, "date_out": 0, "date_in": 0}}
        mater = MongoConect.readMongo(connectionMDB, DB['Materials'], **kwargs)
        data = json.loads(mater.replace("'", '"'))
        kwargs2 = {"arg1": {"name": n, "mlist.mylist.name": nm}, "arg2": {"_id": 0, "date_out": 0, "date_in": 0}}
        user = MongoConect.readMongo(connectionMDB, DB['Users'], **kwargs2)
        print(user)
        data2 = json.loads(user.replace("'", '"'))
        for x in data2['mList']['myList']:
            if x['name'] == nm:
                quantity = x['quantity']
                newQuiantity = quantity - q
                kwargs3 = {"arg1": {"name": n, "mlist.mylist.name": nm}, "arg2": {"$set": {"quantity": newQuiantity}}}
                MongoConect.updateMongo(connectionMDB, DB['Users'], **kwargs3)
                print(data2)
                newData = data['mList']['myList']
                print(newData)
                kwargs4 = {"arg1": {"name": n}, "arg2": {"$set": {"mlist.myList": newData}}}
                MongoConect.updateMongo(connectionMDB, DB['Users'], **kwargs4)
                updQuantity = (mater['quantity'] + q)
                kwargs4 = {"arg1": {"name": nm}, "arg2": {"$set": {"quantity": updQuantity}}}
                MongoConect.updateMongo(connectionMDB, DB['Materials'], **kwargs4)
            else:
                print("Material no encontrado")

    def showMaterial(self):
        try:
            Interface.clear()
            a = input("\nIngrese el material: ")
            if self.selectorDB == "2":
                data = connection.getOneData("Name", "Materials", a)
                print("\nNombre: " + data[1] + ", Cantidad: " + str(data[2]))
            elif self.selectorDB == "1":
                b: Material = matList.getObject(None, a)
                if b is not None:
                    print("\nNombre: " + str(b.name) + ", Cantidad: " + str(b.quantity))
                else:
                    print('No encontrado')
            elif self.selectorDB == "3":
                kwargs = {"arg1": {"name": a}, "arg2": {"_id": 0}}
                mater = MongoConect.readMongo(connectionMDB, DB['Materials'], **kwargs)
                print(mater)
        except Exception as err:
            print(err)

    def showUser(self):
        Interface.clear()
        a = input("\nIngrese el usuario: ")
        if self.selectorDB == "2":
            Interface.showUsrMySql(a)
        elif self.selectorDB == "1":
            b: User = userList.getObject(None, a)
            if b is not None:
                Interface.showUsrLocal(a)
            else:
                print('No encontrado')
        elif self.selectorDB == "3":
            kwargs = {"arg1": {"name": a}, "arg2": {"_id": 0}}
            usr = MongoConect.readMongo(connectionMDB, DB['Users'], **kwargs)
            data = json.loads(usr.replace("'", '"'))
            data['mList']['myList'].append(1)

    @staticmethod
    def showUsrLocal(a):
        b: User = userList.getObject(None, a)
        if b is not None:
            print("\nNombre: " + str(b.name) + ", Edad: " + str(b.age))
            for obj in b.mList.getmyList():
                print("Lista de materiales pedidos\nNombre: " + str(obj.name) + ", cantidad: " + str(
                    obj.quantity))

    @staticmethod
    def showUsrMySql(a):
        data = connection.getOneData("Name", "Users", a)
        print("\nDatos del usuario:"
              "\nNombre: " + data[1] +
              "\nApellido: " + str(data[2]) +
              "\nEdad: " + str(data[3]))
        mlist = connection.getManyData("UserID", "UserMaterials", data[0])
        for x in mlist:
            nom = connection.getOneData("id", "Materials", x[1])
            print("\nLista de materiales pedidos:"
                  "\nNombre: " + nom[1] + ", Cantidad: " + str(x[3]))

    def showUsrList(self):
        Interface.clear()
        if self.selectorDB == "1":
            for obj in userList.getmyList():
                print("\nNombre: " + str(obj.name) + " " + str(obj.lastName) + ", Edad: " + str(obj.age))
        elif self.selectorDB == "2":
            data = connection.getAllData("Users")
            for x in data:
                print(x)
        elif self.selectorDB == "3":
            usr = MongoConect.readMongo(connectionMDB, DB['Users'], )
            print(usr)

    def showMaterials(self):
        Interface.clear()
        if self.selectorDB == "1":
            for obj in matList.getmyList():
                print("\nNombre: " + str(obj.name) + ", Cantidad: " + str(obj.quantity) + ", Fecha de prestamo: "
                      + str(obj.date_out) + ", Fecha de regingreso: " + str(obj.date_in))
        elif self.selectorDB == "2":
            data = connection.getAllData("Materials")
            for x in data:
                print(x)
        elif self.selectorDB == "3":
            mater = MongoConect.readMongo(connectionMDB, DB['Materials'], )
            print(mater)

    @staticmethod
    def my_dict(obj):
        if not hasattr(obj, "__dict__"):
            return obj
        result = {}
        for key, val in obj.__dict__.items():
            if key.startswith("_"):
                continue
            element = []
            if isinstance(val, list):
                for item in val:
                    element.append(Interface.my_dict(item))
            else:
                element = Interface.my_dict(val)
            result[key] = element
        return result

    def mongoDBLend(self, ui, mi):
        obj = {"uid": ui, "mid": mi}
        print("this is mongo")

    def selectStorage(self):
        o = input("\n1) Local \n2) MySql \n3) MongoDB \nSelecciona una de las opciones anteriores: ")
        if int(o) < 4:
            if int(o) > 0:
                self.selectorDB = o
                print("\nCambio realizado!!\n")
            else:
                print("Opcion no valida, se continuara con la opcion actual")
        else:
            print("Opcion no valida, se continuara con la opcion actual")
