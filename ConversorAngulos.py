import math
class ConversorAngulos:
    def __init__(self, angle):
        self.angle = angle

    def convertir_a_radianes(self):
        return self.angle * (math.pi / 180)

    def convertir_a_grados(self):
        return self.angle * (180 / math.pi)

    def menu(self):
        print("Seleccione la conversión que desea realizar:")
        print("1. Convertir grados a radianes")
        print("2. Convertir radianes a grados")
        opcion = input("Ingrese el número de la opción deseada (1 o 2): ")

        if opcion == '1':
            self.angle = float(input("Ingrese el ángulo en grados: "))
            print(f"{self.angle} grados es {self.convertir_a_radianes()} radianes.")
        elif opcion == '2':
            self.angle = float(input("Ingrese el ángulo en radianes: "))
            print(f"{self.angle} radianes es {self.convertir_a_grados()} grados.")
        else:
            print("Opción no válida. Intente de nuevo.")