from logica import (
    do_selection_sort_asc
)

def cargar_productos_hardcodeados():
    matriz_productos = [
        {"id":3, "nombre": "Cafe con leche", "cantidad": 18, "precio": 800.0},
        {"id":1, "nombre": "Cafe chico", "cantidad": 20, "precio": 500.0},
        {"id":5, "nombre": "Capuchino", "cantidad": 12, "precio": 900.0},
        {"id":2, "nombre": "Cafe grande", "cantidad": 15, "precio": 700.0},
        {"id":4, "nombre": "Cortado", "cantidad": 22, "precio": 600.0}
    ]
    return matriz_productos


def mostrar_datos_productos(lista_prod: list[list]):
    print("id | nombre | cantidad | precio")
    for producto in lista_prod:
        print(producto[id], ",", producto["nombre"], ",", producto["cantidad"], ",", producto["precio"])


def do_selection_sort_asc_productos(lista_prod: list[list], columna_a_ordenar: int):
    do_selection_sort_asc(lista_prod, columna_a_ordenar)


def modificar_producto(lista_prod: list[list], id_buscar: int, nuevo_stock: int, nuevo_precio: float):
    modificar = False
    for producto in lista_prod:
        if producto[0] == id_buscar:
            producto[2] = nuevo_stock
            producto[3] = nuevo_precio
            modificar = True
    return modificar


def borrar_producto(lista_prod: list[list], id_buscar: int):
    borrar = False
    for i in range(len(lista_prod)):
        if lista_prod[i][0] == id_buscar:
            lista_prod.pop(i)
            borrar = True
            break
    return borrar

def validar_existe_productos(lista_productos: list[dict], id: int):
    for producto in lista_productos:
        if producto["id"] == id:
            return True
    return False

def validar_stock(lista_productos: list[dict], id: int):
    
    for producto in lista_productos:
        if producto["id"] == id:
            if producto["cantidad"] > 0:
                return True
    
    return False
