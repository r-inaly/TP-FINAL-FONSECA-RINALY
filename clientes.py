from logica import (
    do_selection_sort_asc
)

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


def do_selection_sort_asc_clientes(lista_cli: list[dict], clave_a_ordenar: str):
    do_selection_sort_asc(lista_cli, clave_a_ordenar)


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

def validar_existe_cliente(lista_clientes: list[dict], id: int):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            return True
    return False

def entregar_cliente_solicitado(lista_clientes: list[dict], id: int):
    for cliente in lista_clientes:
        if cliente["id"] == id:
            return cliente
    return False
