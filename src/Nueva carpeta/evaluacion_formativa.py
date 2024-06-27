import csv

trabajadores=[]

def registrar_trabajador():
    try:
        datos=["Nombre","Cargo","Sueldo Bruto","Descuento Salud", "Descuento AFP","Sueldo Liquido"]
        nombre=input("Ingresa el nombre completo del trabajador a registrar: ")
        cargo=input("Ingresa el cargo del trabajador a registrar: ")
        sueldo_bruto=int(input("Ingresa el sueldo bruto del trabajador: "))
    except:
        print("Ingresa los datos solicitados!!!!")
    descuento_salud= sueldo_bruto * 0.07
    descuento_afp=sueldo_bruto * 0.12
    descuentos_totales=descuento_salud + descuento_afp
    sueldo_liquido=sueldo_bruto - descuentos_totales
    
    trabajador={
        "Nombre":nombre,
        "Cargo":cargo,
        "Sueldo Bruto":sueldo_bruto,
        "Descuento Salud":descuento_salud,
        "Descuento AFP":descuento_afp,
        "Sueldo Liquido":sueldo_liquido
    }
    trabajadores.append(trabajador)
    
    with open("C:/Users/Nicol/OneDrive/Escritorio/CARPETA IMPORTANTE/PYTHON/PYTHON/src/Nueva carpeta/empresa.csv",mode="a", newline="") as file:
        escritor=csv.DictWriter(file,fieldnames=datos)
        if file.tell()==0:
            escritor.writeheader()
        escritor.writerow(trabajador)
    print("Trabajador añadido al sistema")


def lista_trabajadores():
    with open("C:/Users/Nicol/OneDrive/Escritorio/CARPETA IMPORTANTE/PYTHON/PYTHON/src/Nueva carpeta/empresa.csv",mode="r") as file:
        lector=csv.reader(file)
        for trabajador in lector:
            print(trabajador)


#falta terminar
def imprimir_planilla():
    print("1.- Imprimir Todos los sueldos")
    print("2.- Imprimir algún cargo especifico")
    opc=int(input("ingresa tu opcion: "))
    if opc == 1:
        with open("C:/Users/Nicol/OneDrive/Escritorio/CARPETA IMPORTANTE/PYTHON/PYTHON/src/Nueva carpeta/empresa.csv",mode="r")as file:
            lector=csv.reader(file)
            for trabajador in lector:
                print(trabajador)
    elif opc == 2:
        contador=1
        with open("C:/Users/Nicol/OneDrive/Escritorio/CARPETA IMPORTANTE/PYTHON/PYTHON/src/Nueva carpeta/empresa.csv",mode="r") as file:
            lector=csv.reader(file)
            next(lector)
            print("¿Que cargo deseas ver?")
            for trabajador in lector:
                print(f"{contador}.- {trabajador[1]}")
                contador+=1
            opc=int(input("Ingresa tu opcion: "))
            
            if opc ==1:
                cargo="CEO"
                reporte="Reporte_ceo.txt"
            elif opc == 2:
                cargo="Desarrollador"
                reporte="Reporte_Desarrollador.txt"
            elif opc == 3: 
                cargo="Analista de Datos"
                reporte="Reporte_Analista de Datos.txt"

        with open("C:/Users/Nicol/OneDrive/Escritorio/CARPETA IMPORTANTE/PYTHON/PYTHON/src/Nueva carpeta/empresa.csv", mode="r") as file:
            lector = csv.reader(file)
            next(lector)  # Saltar el encabezado
            for trabajador in lector:
                if trabajador[1] == cargo:
                    with open(f"C:/Users/Nicol/OneDrive/Escritorio/CARPETA IMPORTANTE/PYTHON/PYTHON/src/Nueva carpeta/{reporte}", mode="w") as file_reporte:
                        file_reporte.write(f"Nombre: {trabajador[0]}, Cargo: {trabajador[1]}, Sueldo Bruto: {trabajador[2]}, Descuento Salud: {trabajador[3]}, Descuento AFP: {trabajador[4]}, Sueldo Líquido: {trabajador[5]}\n")