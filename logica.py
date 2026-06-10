def cargar_productos_hardcodeados():
    matriz_productos = [
        [3, "Cafe con leche", 18, 800.0],
        [1, "Cafe chico", 20, 500.0],
        [5, "Capuchino", 12, 900.0],
        [2, "Cafe grande", 15, 700.0],
        [4, "Cortado", 22, 600.0]
    ]
    return matriz_productos


def mostrar_datos_productos(lista_prod: list[list]):
    print("id | nombre | stock | precio")
    for producto in lista_prod:
        print(producto[0], ",", producto[1], ",", producto[2], ",", producto[3])


def do_selection_sort_productos(lista_prod: list[list], columna_a_ordenar: int):
    for indice_fila in range(len(lista_prod) - 1):
        indice_elem_menor = indice_fila
        for indice_sig_fila in range(indice_fila + 1, len(lista_prod)):
            if lista_prod[indice_elem_menor][columna_a_ordenar] > lista_prod[indice_sig_fila][columna_a_ordenar]:
                indice_elem_menor = indice_sig_fila
            
        if indice_elem_menor != indice_fila:
            aux = lista_prod[indice_elem_menor]
            lista_prod[indice_elem_menor] = lista_prod[indice_fila]
            lista_prod[indice_fila] = aux


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


def cargar_clientes_hardcodeado():
    lista_clientes = [
        {"id": 3, "apellido": "Gomez", "nombre": "Juan", "ciudad": "Rosario"},
        {"id": 1, "apellido": "Argento", "nombre": "Pepe", "ciudad": "CABA"},
        {"id": 5, "apellido": "Argento", "nombre": "Moni", "ciudad": "CABA"},
        {"id": 2, "apellido": "Santi", "nombre": "Ariel", "ciudad": "Cordoba"},
        {"id": 4, "apellido": "Zampa", "nombre": "Luis", "ciudad": "Rosario"}
    ]
    return lista_clientes


def mostrar_datos_clientes(lista_cli: list[dict]):
    print("id |  apellido |  nombre |  ciudad")
    for cliente in lista_cli:
        print(cliente["id"], ",", cliente["apellido"], ",", cliente["nombre"], ",", cliente["ciudad"])


def do_selection_sort_clientes(lista_cli: list[dict], clave_a_ordenar: str):
    for indice_fila in range(len(lista_cli) - 1):
        indice_elem_menor = indice_fila
        for indice_sig_fila in range(indice_fila + 1, len(lista_cli)):
            if lista_cli[indice_elem_menor][clave_a_ordenar] > lista_cli[indice_sig_fila][clave_a_ordenar]:
                indice_elem_menor = indice_sig_fila
            
        if indice_elem_menor != indice_fila:
            aux = lista_cli[indice_elem_menor]
            lista_cli[indice_elem_menor] = lista_cli[indice_fila]
            lista_cli[indice_fila] = aux


def modificar_cliente(lista_cli: list[dict], id_buscar: int, nuevo_apellido: str, nuevo_nombre: str, nueva_ciudad: str):
    modificar = False
    for cliente in lista_cli:
        if cliente["id"] == id_buscar:
            cliente["apellido"] = nuevo_apellido
            cliente["nombre"] = nuevo_nombre
            cliente["ciudad"] = nueva_ciudad
            modificar = True
    return modificar


def borrar_cliente(lista_cli: list[dict], id_buscar: int):
    borrar = False
    for i in range(len(lista_cli)):
        if lista_cli[i]["id"] == id_buscar:
            lista_cli.pop(i)
            borrar = True
            break
    return borrar


def filtrar_clientes_por_ciudad(lista_cli: list[dict], ciudad_buscar: str):
    lista_filtrada = []
    for cliente in lista_cli:
        if cliente["ciudad"] == ciudad_buscar:
            lista_filtrada.append(cliente)
    return lista_filtrada