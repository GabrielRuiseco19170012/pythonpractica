from Material import Material
from Usuario import Usuario
import sys

mlist = Material()
ulist = Usuario()


class Menu:

    def __init__(self):
        self.showMenu()

    def endProg(self):
        print("\n")
        print("Fin del programa")
        sys.exit()

    def showMenu(self):
        print(
            "\n\nMENU DEL CENTRO\n\n1) Pedir material\n2) Regresar material\n3) Nuevo usuario\n4) Nuevo material \n5) Mostrar materiales \n6) Mostrar usuario \n7) Mostrar lista usuarios \n8) Mostrar lista materiales \n9) Salir")
        opc = input("\nSeleccione una opcion: ")
        if opc == "1" or opc == "2" or opc == "3" or opc == "4" or opc == "5" or opc == "6" or opc == "7" or opc == "8" or opc == "9":
            while opc != "9":
                if opc == "1":
                    a = input("\nIngrese el usuario: ")
                    b = input("\nIngrese el material: ")
                    c = input("\nIngrese la cantidad: ")
                    u = ulist.getObject(None, a)
                    i = ulist.getIndex(a)
                    if u != None:
                        m = mlist.getObject(None, b)
                        mi = mlist.getIndex(b)
                        if m != None:
                            m.cantidad -= int(c)
                            mlist.updateObject(mi, m)
                            print(str(m))
                            print(str(mlist.lista[mi]))
                            m.cantidad = int(c)
                            u.lista.append(m)
                            ulist.updateObject(i, u)
                            print(str(m))
                        else:
                            print('\nMaterial no encontrado')
                    else:
                        print('\nUsuario no encontrado')
                    self.showMenu()
                    print(str(mlist.lista[0]))
                elif opc == "2":
                    a = input("\nIngrese el usuario: ")
                    b = input("\nIngrese el material: ")
                    c = input("\nIngrese la cantidad: ")
                    u = ulist.getObject(None, a)
                    i = ulist.getIndex(a)
                    if u != None:
                        m = mlist.getObject(None, b)
                        mi = mlist.getIndex(b)
                        if m != None:
                            m.cantidad += int(c)
                            mlist.updateObject(mi, m)
                            print(str(m))
                            mat = u.getObject(None, b)
                            mat.cantidad -= (int(c) * 2)
                            if mat.cantidad < 1:
                                u.lista.pop(mi)
                            else:
                                u.updateObject(mi, mat)
                        else:
                            print('\nMaterial no encontrado')
                    else:
                        print('\nUsuario no encontrado')
                    self.showMenu()
                elif opc == "3":
                    a = input("\nIngrese el nombre: ")
                    b = input("\nIngrese la edad: ")
                    u = Usuario()
                    u.nom = a
                    u.edad = b
                    ulist.addObject(u)
                    self.showMenu()
                elif opc == "4":
                    a = input("\nIngrese el nombre: ")
                    b = input("\nIngrese la cantidad: ")
                    m = Material()
                    m.nom = a
                    m.cantidad = int(b)
                    mlist.addObject(m)
                    self.showMenu()
                elif opc == "5":
                    a = input("\nIngrese el material: ")
                    b = mlist.getObject(None, a)
                    if b != None:
                        print(str(b))
                        print("\nNombre: " + str(b.nom) + ", Cantidad: " + str(b.cantidad))
                    else:
                        print('No encontrado')
                    self.showMenu()
                elif opc == "6":
                    a = input("\nIngrese el usuario: ")
                    b = ulist.getObject(None, a)
                    if b != None:
                        print("\nNombre: " + str(b.nom) + ", Edad: " + str(b.edad))
                        for obj in b.lista:
                            print("Lista de materiales pedidos\nNombre: " + str(obj.nom) + ", cantidad: " + str(
                                obj.cantidad))
                    else:
                        print('No encontrado')
                    self.showMenu()
                elif opc == "7":
                    for obj in ulist.lista:
                        print("\nNombre: " + str(obj.nom) + ", Edad: " + str(obj.edad))
                    self.showMenu()
                elif opc == "8":
                    for obj in mlist.lista:
                        print("\nNombre: " + str(obj.nom) + ", cantidad: " + str(obj.cantidad))
                    self.showMenu()
                elif opc == "9":
                    self.endProg()
            else:
                print("\nOpcion no valida")
                self.showMenu()
