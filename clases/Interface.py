from clases.Material import Material
from clases.Usuario import Usuario
import copy
import pickle

mlist = Material()
ulist = Usuario()

try:
    with open("Material.obj", "rb") as f:
        mlist = pickle.load(f)
except:
    print("Sin datos")

try:
    with open("Usuario.obj", "rb") as f:
        ulist = pickle.load(f)
except:
    print("Sin Datos")


class Interface:

    @staticmethod
    def pedirMaterial():
        a = input("\nIngrese el usuario: ")
        b = input("\nIngrese el material: ")
        c = input("\nIngrese la cantidad: ")
        c = int(c)
        u = ulist.getObject(None, a)
        i = ulist.getIndex(a)
        if u != None:
            m = mlist.getObject(None, b)
            mi = mlist.getIndex(b)
            if m != None:
                m.updateCantidad(m.cantidad - c)
                mlist.updateObject(mi, m)
                print(str(m))
                print(str(mlist.lista[mi]))
                mn = Material()
                mn = copy.copy(m)
                mn.updateCantidad(c)
                u.lista.append(mn)
                ulist.updateObject(i, u)
                print(str(m))
            else:
                print('\nMaterial no encontrado')
        else:
            print('\nUsuario no encontrado')
        print(str(mlist.lista[0]))

    @staticmethod
    def regresarMaterial():
        a = input("\nIngrese el usuario: ")
        b = input("\nIngrese el material: ")
        c = input("\nIngrese la cantidad: ")
        u = ulist.getObject(None, a)
        i = ulist.getIndex(a)
        if u != None:
            m = mlist.getObject(None, b)
            mi = mlist.getIndex(b)
            if m != None:
                m.updateCantidad(m.cantidad + int(c))
                mlist.updateObject(mi, m)
                print(str(m))
                mat = u.getObject(None, b)
                mat.updateCantidad(mat.cantidad - (int(c) * 2))
                if mat.cantidad < 1:
                    u.lista.pop(mi)
                else:
                    u.updateObject(mi, mat)
            else:
                print('\nMaterial no encontrado')
        else:
            print('\nUsuario no encontrado')

    @staticmethod
    def nuevoUsuario():
        a = input("\nIngrese el nombre: ")
        b = input("\nIngrese la edad: ")
        u = Usuario()
        u.nom = a
        u.edad = b
        ulist.addObject(u)

    @staticmethod
    def nuevoMaterial():
        a = input("\nIngrese el nombre: ")
        b = input("\nIngrese la cantidad: ")
        m = Material()
        m.nom = a
        m.cantidad = int(b)
        mlist.addObject(m)

    @staticmethod
    def mostrarMaterial():
        a = input("\nIngrese el material: ")
        b = mlist.getObject(None, a)
        if b != None:
            print(str(b))
            print("\nNombre: " + str(b.nom) + ", Cantidad: " + str(b.cantidad))
        else:
            print('No encontrado')

    @staticmethod
    def mostrarUsuario():
        a = input("\nIngrese el usuario: ")
        b = ulist.getObject(None, a)
        if b != None:
            print("\nNombre: " + str(b.nom) + ", Edad: " + str(b.edad))
            for obj in b.lista:
                print("Lista de materiales pedidos\nNombre: " + str(obj.nom) + ", cantidad: " + str(
                    obj.cantidad))
        else:
            print('No encontrado')

    @staticmethod
    def mostrarListaUsr():
        for obj in ulist.lista:
            print("\nNombre: " + str(obj.nom) + ", Edad: " + str(obj.edad))

    @staticmethod
    def mostrarListaMat():
        for obj in mlist.lista:
            print("\nNombre: " + str(obj.nom) + ", cantidad: " + str(obj.cantidad))

    @staticmethod
    def guardarCambios():
        with open("Material.obj", "wb") as f:
            pickle.dump(mlist, f)
        with open("Usuario.obj", "wb") as f:
            pickle.dump(ulist, f)
