# id_detalle, id_venta, id_producto, cantidad_producto

from ventas import (
    validar_existe_venta,
)

from productos import (
    validar_existe_productos,
)

def mostrar_detalle_venta(detalle_venta: dict):
    print(detalle_venta["id_detalle"], ",", detalle_venta["id_venta"], ",", detalle_venta["id_producto"], ",", detalle_venta["cantidad_producto"])

def mostrar_detalles_de_ventas(lista_detalle_de_ventas: list[dict]):
    for venta in lista_detalle_de_ventas:
        mostrar_detalle_venta(venta)

def cargar_detalle_de_venta(lista_detalle_de_ventas: list[dict], lista_productos: list[dict], lista_ventas: list[dict], id_detalle: int, id_venta: int, id_producto: int, cantidad_producto: int,):
    if validar_existe_venta(lista_ventas, id_venta) and validar_existe_productos(lista_productos, id_producto):
        lista_detalle_de_ventas.append({
            "id_detalle": id_detalle,
            "id_venta": id_venta,
            "id_producto": id_producto,
            "cantidad_producto": cantidad_producto
        })