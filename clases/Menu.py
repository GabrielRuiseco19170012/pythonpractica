from clases.Interface import Interface
import sys


class Menu:

    def __init__(self):
        self.showMenu()

    def endProg(self):
        print("\n")
        print("Fin del programa")
        sys.exit()

    def showMenu(self):
        print(
            "\n\nMENU DEL CENTRO\n\n1) Pedir material\n2) Regresar material\n3) Nuevo usuario\n4) Nuevo material \n5) Mostrar usuario \n6) Mostrar material \n7) Mostrar lista usuarios \n8) Mostrar lista materiales \n9) Salir")
        opc = input("\nSeleccione una opcion: ")
        if int(opc) < 10:
            while opc != "9":
                if opc == "1":
                    Interface.pedirMaterial()

                    self.showMenu()
                elif opc == "2":
                    Interface.regresarMaterial()

                    self.showMenu()
                elif opc == "3":
                    Interface.nuevoUsuario()

                    self.showMenu()
                elif opc == "4":
                    Interface.nuevoMaterial()

                    self.showMenu()
                elif opc == "5":
                    Interface.mostrarUsuario()

                    self.showMenu()
                elif opc == "6":
                    Interface.mostrarMaterial()

                    self.showMenu()
                elif opc == "7":
                    Interface.mostrarListaUsr()

                    self.showMenu()
                elif opc == "8":
                    Interface.mostrarListaMat()

                    self.showMenu()
            else:
                Interface.guardarCambios()
                self.endProg()
        else:
            print("\nOpcion no valida")
            self.showMenu()
