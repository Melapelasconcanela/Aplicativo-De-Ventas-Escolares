from producto import Producto

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        print(f"✓ '{nombre}' agregado.\n")

    def calcular_total(self):
        return sum(p.subtotal() for p in self.productos)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.\n")
            return

        print("\n--- Productos registrados ---")
        for p in self.productos:
            print(p)
        print(f"TOTAL: ${self.calcular_total():.2f}\n")
