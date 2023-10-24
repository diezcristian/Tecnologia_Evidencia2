class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def registrar(self, margen_de_venta):
        # Calculamos el precio de venta
        self.precio_de_venta = self.costo / (1 - margen_de_venta)

        # Guardamos el producto en el diccionario
        productos[self.id] = self

    def imprimir(self):
        print("ID:", self.id)
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Costo:", self.costo)
        print("Cantidad:", self.cantidad)
        print("Precio de venta:", self.precio_de_venta)


productos = {}

# Registramos un producto
producto = Producto(1, "Portatil", "Asus", 500, 22)
producto.registrar(0.2)

# Registramos otro producto
producto2 = Producto(2, "Celulares", "iphone 15", 900, 15)
producto2.registrar(0.3)

# Imprimimos el listado de productos
for producto in productos.values():
    producto.imprimir()