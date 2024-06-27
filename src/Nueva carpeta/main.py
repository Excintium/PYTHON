import csv
from evaluacion_formativa import lista_trabajadores,registrar_trabajador,imprimir_planilla

while True:
    print("**Registro de trabajadores**")
    print("1.- Registrar Trabajador")
    print("2.- Listar todos los trabajadores")
    print("3.- Imprimir planilla de sueldos")
    print("4.- Salir del programa")
    opc=int(input("Ingresa una opción: "))
    if opc == 1:
        registrar_trabajador()
    elif opc == 2:
        lista_trabajadores()
    elif opc == 3:
        imprimir_planilla()
    elif opc == 4:
        break