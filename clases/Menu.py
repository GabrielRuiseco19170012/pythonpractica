from clases.Interface import Interface
import sys

inter = Interface()


class Menu:

    def __init__(self):
        self.showMenu()

    @staticmethod
    def endProg():
        print("\n")
        print("Fin del programa")
        sys.exit()

    def showMenu(self):
        print(
            "\n\nMENU DEL CENTRO\n"
            "\n1) Pedir material"
            "\n2) Regresar material"
            "\n3) Nuevo usuario"
            "\n4) Nuevo material "
            "\n5) Mostrar usuario "
            "\n6) Mostrar material "
            "\n7) Mostrar lista usuarios "
            "\n8) Mostrar lista materiales "
            "\n9) Cambiar almacenamiento"
            "\n10) Salir")
        opc = input("\nSeleccione una opcion: ")
        if int(opc) < 11 and int(opc) > 0:
            while opc != "10":
                if opc == "1":
                    inter.lendMaterial()

                    self.showMenu()
                elif opc == "2":
                    inter.returnMaterial()

                    self.showMenu()
                elif opc == "3":
                    inter.saveUser()

                    self.showMenu()
                elif opc == "4":
                    inter.saveMaterial()

                    self.showMenu()
                elif opc == "5":
                    inter.showUser()

                    self.showMenu()
                elif opc == "6":
                    inter.showMaterial()

                    self.showMenu()
                elif opc == "7":
                    inter.showUsrList()

                    self.showMenu()
                elif opc == "8":
                    inter.showMaterials()

                    self.showMenu()
                elif opc == "9":
                    inter.selectStorage()

                    self.showMenu()
            else:
                self.endProg()
        else:
            print("\nOpcion no valida")
            self.showMenu()
