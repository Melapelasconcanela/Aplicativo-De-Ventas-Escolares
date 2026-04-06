from carrito import Carrito

def menu():
    carrito = Carrito()

    while True:
        print("=== Tienda Escolar ===")
        print("1. Registrar producto")
        print("2. Ver productos y total")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            carrito.agregar_producto()
        elif opcion == "2":
            carrito.mostrar_productos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")


menu()