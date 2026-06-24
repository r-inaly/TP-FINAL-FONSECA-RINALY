# id_venta, id_cliente apellido nombre monto_venta
from logica import (
    do_selection_sort_asc,
    do_selection_sort_des
)

from clientes import (
    validar_existe_cliente,
    entregar_cliente_solicitado
)

from productos import (
    validar_existe_productos,
    validar_stock
)

def validar_comienzo_de_venta():
    if validar_existe_cliente() and validar_existe_productos():
        return True
    else:
        False

def generar_venta(id_venta: int, id_cliente: int, lista_clientes: list[dict], monto_venta_total: str):
    apellido = "N/A"
    nombre = "N/A"

    if validar_existe_cliente(lista_clientes, id):
        cliente = entregar_cliente_solicitado()
        nombre = cliente["nombre"]
        apellido = cliente["apellido"]

    return {
        "id_venta": id_venta,
        "id_cliente": id_cliente,
        "nombre": nombre,
        "apellido": apellido,
        "monto_venta": monto_venta_total
    }

def do_selection_sort_asc_ventas(lista_ventas: list[list], columna_a_ordenar: int):
    do_selection_sort_asc(lista_ventas, columna_a_ordenar)

def do_selection_sort_des_ventas(lista_ventas: list[list], columna_a_ordenar: int):
    do_selection_sort_des(lista_ventas, columna_a_ordenar)

def mostrar_venta(venta: dict):
    print(venta["id_venta"], ",", venta["id_venta"], ",", venta["apellido"], ",", venta["nombre"], venta["monto_venta"])

def mostrar_ventas(lista_ventas: list[dict]):
    for venta in lista_ventas:
        mostrar_venta(venta)

def validar_existe_venta(lista_ventas: list[dict], id: int):
    for venta in lista_ventas:
        if venta["id_venta"] == id:
            return True
    return False

