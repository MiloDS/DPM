import os, io

productos = {"producto":["manzana"]}


print("°|| =================== MENU ==================== ||°")
print("    1. Ver productos\n    2. Agregar productos al carrito\n    3. Ver carrito\n    4. Finalizar compra\n    5. Salir")
print("°|| ============================================= ||°")

def agregarProducto():
    producto = input(f"Que producto quieres agregar?:{productos["productos"].append(producto)}")
    return productos
    
opcion = input("Por favor ingrese un valor:")

if opcion < 0 or opcion > 5:
    opcion = input("Por favor ingrese un valor valido:")
elif opcion == 1:
    print("°|| ======= Productos ======= ||°")
elif opcion == 2:
    agregarProducto()

