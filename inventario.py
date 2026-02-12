# Clase Inventario: Maneja la lógica de la lista de productos (Requisito 2)
class Inventario:
    def __init__(self):
        self.productos = [] # Estructura de datos personalizada

    def añadir_producto(self, producto):
        # Asegura que el ID sea único antes de agregar
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido.")

    def eliminar_producto(self, id_p):
        self.productos = [p for p in self.productos if p.get_id() != id_p]
        print("Eliminación procesada.")

    def actualizar_producto(self, id_p, cant=None, prec=None):
        for p in self.productos:
            if p.get_id() == id_p:
                if cant is not None: p.set_cantidad(cant)
                if prec is not None: p.set_precio(prec)
                print("Actualizado correctamente.")
                return
        print("No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        # Busca productos con nombres similares
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_inventario(self):
        if not self.productos: print("Vacío.")
        for p in self.productos: print(p)