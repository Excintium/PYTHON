def mostrar_menu():
    print("\nMenu de Sushi:")
    print("1. Pikachu Roll - $4500")
    print("2. Otaku Roll - $5000")
    print("3. Pulpo Venenoso Roll - $5200")
    print("4. Anguila Eléctrica Roll - $4800")
    print("5. Completar pedido")

def obtener_precio(opcion):
    precios = {
        1: 4500,
        2: 5000,
        3: 5200,
        4: 4800
    }
    return precios.get(opcion, 0)

def obtener_nombre_roll(opcion):
    nombres = {
        1: "Pikachu Roll",
        2: "Otaku Roll",
        3: "Pulpo Venenoso Roll",
        4: "Anguila Eléctrica Roll"
    }
    return nombres.get(opcion, "")

def aplicar_descuento(total, codigo):
    if codigo == "soyotaku":
        return total * 0.9
    else:
        print("Código no válido")
        return total

def main():
    pedido = []
    total = 0

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-5): "))
        
        if opcion == 5:
            break
        
        if 1 <= opcion <= 4:
            roll = obtener_nombre_roll(opcion)
            precio = obtener_precio(opcion)
            pedido.append((roll, precio))
            total += precio
            print(f"{roll} agregado al pedido. Total actual: ${total}")
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

    while True:
        tiene_codigo = input("¿Posee un código de descuento? (s/n): ").lower()
        if tiene_codigo == 's':
            codigo = input("Ingrese el código de descuento: ")
            total_con_descuento = aplicar_descuento(total, codigo)
            if total_con_descuento != total:
                total = total_con_descuento
                break
        elif tiene_codigo == 'n':
            break
        else:
            print("Entrada no válida, por favor ingrese 's' o 'n'.")

    print("\nDetalle del pedido:")
    for roll, precio in pedido:
        print(f"{roll}: ${precio}")
    print(f"Total a pagar: ${total}")

if __name__ == "__main__":
    main()
