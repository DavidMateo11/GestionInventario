# Clase Producto: Define los atributos básicos de cada artículo
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados para asegurar el encapsulamiento (Requisito 1)
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters y Setters para cada atributo
    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def get_cantidad(self): return self.__cantidad
    def get_precio(self): return self.__precio

    def set_nombre(self, n): self.__nombre = n
    def set_cantidad(self, c): self.__cantidad = c
    def set_precio(self, p): self.__precio = p

    def __str__(self):
        return f"ID: {self.__id} | {self.__nombre} | Stock: {self.__cantidad} | Precio: ${self.__precio}"