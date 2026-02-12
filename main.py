from producto import Producto
from inventario import Inventario

# Interfaz de Usuario: Menú interactivo (Requisito 3)
def menu():
    mi_inv = Inventario()
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Mostrar | 6. Salir")
        op = input("Seleccione: ")

        if op == '1':
            mi_inv.añadir_producto(Producto(input("ID: "), input("Nombre: "), int(input("Cant: ")), float(input("Precio: "))))
        elif op == '2':
            mi_inv.eliminar_producto(input("ID a eliminar: "))
        elif op == '3':
            id_a = input("ID: ")
            c = input("Nueva Cantidad (vacío para saltar): ")
            p = input("Nuevo Precio (vacío para saltar): ")
            mi_inv.actualizar_producto(id_a, int(c) if c else None, float(p) if p else None)
        elif op == '4':
            for r in mi_inv.buscar_por_nombre(input("Nombre: ")): print(r)
        elif op == '5':
            mi_inv.mostrar_inventario()
        elif op == '6':
            break

if __name__ == "__main__":
    menu()