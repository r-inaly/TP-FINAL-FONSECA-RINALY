
def cargar_producto():
    lista_producto_ids = [1, 2, 3, 4, 5]
    lista_producto_nombres = ['Cafe chico', 'Cafe grande', 'Cafe con leche', 'Cortado', 'Capuchino']
    lista_producto_inventarios = [20, 15, 18, 22, 12]
    lista_producto_precios = [500.0, 700.0, 800.0, 600.0, 900.0]


    return [
        lista_producto_ids[0:5],
        lista_producto_nombres[0:5],
        lista_producto_inventarios[0:5],
        lista_producto_precios[0:5]
    ]
