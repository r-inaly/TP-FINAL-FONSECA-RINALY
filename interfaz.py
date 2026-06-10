import os
from mensajes import (
    menu_productos_mensaje,
    menu_clientes_mensaje,
    menu_ordenar_productos_mensaje,
    menu_ordenar_clientes_mensaje
)
from logica import (
    cargar_productos_hardcodeados,
    mostrar_datos_productos,
    do_selection_sort_productos,
    modificar_producto,
    borrar_producto,
    cargar_clientes_hardcodeado,
    mostrar_datos_clientes,
    do_selection_sort_clientes,
    modificar_cliente,
    borrar_cliente,
    filtrar_clientes_por_ciudad
)
from validaciones import (
    texto_letras
)

def menu_productos(lista_productos: list[list]):
    bucle = True
    while(bucle):
        os.system('cls')
        menu_productos_mensaje()
        opcion = input('ingrese una opcion entre 1-5: ')
        match opcion:
            case '1':
                lista_productos[:] = cargar_productos_hardcodeados()
                print("productos cargados correctamente.")
                os.system('pause')
                os.system('cls')
            case '2':
                if len(lista_productos) == 0:
                    print("primero se debe cargar los productos!")
                else:
                    mostrar_datos_productos(lista_productos)
                    id = int(input("ingrese el ID del producto a modificar: "))
                    stock = int(input("ingrese el nuevo Stock: "))
                    precio = float(input("ingrese el nuevo precio: "))
                    if modificar_producto(lista_productos, id, stock, precio):
                        print("producto modificado correctamente.")
                    else:
                        print("no se encontro ningun producto con ese ID.")
                os.system('pause')
                os.system('cls')
            case '4':
                if len(lista_productos) == 0:
                    print("primero se debe cargar los productos!")
                else:
                    mostrar_datos_productos(lista_productos)
                    id_borrar = int(input("ingrese el ID del producto a borrar: "))
                    if borrar_producto(lista_productos, id_borrar):
                        print("producto eliminado correctamente.")
                    else:
                        print("no se encontro ningun producto con ese ID.")
                os.system('pause')
                os.system('cls')
            case '3':
                if len(lista_productos) == 0:
                    print("primero se debe cargar los productos!")
                else:
                    os.system('cls')
                    menu_productos_complemento(lista_productos)
                os.system('pause')
                os.system('cls')
            case '5':
                bucle = False

def menu_productos_complemento(lista_productos: list[list]):
    bucle = True
    while(bucle):
        os.system('cls')
        menu_ordenar_productos_mensaje()
        opcion = input('ingrese una opcion entre 1-4: ')
        match opcion:
            case '1':
                do_selection_sort_productos(lista_productos, 0)
                mostrar_datos_productos(lista_productos)
                os.system('pause')
                os.system('cls')
            case '2':
                do_selection_sort_productos(lista_productos, 2)
                mostrar_datos_productos(lista_productos)
                os.system('pause')
                os.system('cls')
            case '3':
                do_selection_sort_productos(lista_productos, 1)
                mostrar_datos_productos(lista_productos)
                os.system('pause')
                os.system('cls')
            case '4':
                bucle = False

def menu_clientes(lista_clientes: list[dict]):
    bucle = True
    while(bucle):
        os.system('cls')
        menu_clientes_mensaje()
        opcion = input('ingrese una opcion entre 1-5: ')
        match opcion:
            case '1':
                lista_clientes[:] = cargar_clientes_hardcodeado()
                print("clientes cargados correctamente.")

                os.system('pause')
                os.system('cls')
            case '2':
                if len(lista_clientes) == 0:
                    print("primero se debe cargar los clientes!")
                else:
                    mostrar_datos_clientes(lista_clientes)
                    id = int(input("ingrese el ID del cliente a modificar: "))
                    apellido = texto_letras("ingrese el nuevo apellido: ")
                    nombre = texto_letras("ingrese el nuevo nombre: ")
                    ciudad = texto_letras("ingrese la nueva ciudad: ")
                    
                    if modificar_cliente(lista_clientes, id, apellido, nombre, ciudad):
                        print("cliente modificado correctamente.")
                    else:
                        print("no se encontro ningun cliente con ese ID.")
                os.system('pause')
                os.system('cls')
            case '4':
                if len(lista_clientes) == 0:
                    print("primero se debe cargar los clientes")
                else:
                    mostrar_datos_clientes(lista_clientes)
                    id_borrar = int(input("ingrese el ID del cliente a borrar: "))
                    if borrar_cliente(lista_clientes, id_borrar):
                        print("cliente eliminado correctamente.")
                    else:
                        print("no se encontro ningun cliente con ese ID.")
                os.system('pause')
                os.system('cls')
            case '3':
                if len(lista_clientes) == 0:
                    print("primero se debe cargar los clientes!")
                else:
                    os.system('cls')
                    menu_clientes_complemento(lista_clientes)
                os.system('pause')
                os.system('cls')
            case '5':
                bucle = False

def menu_clientes_complemento(lista_clientes: list[dict]):
    bucle = True
    while(bucle):
        os.system('cls')
        menu_ordenar_clientes_mensaje()
        opcion = input('ingrese una opcion entre 1-5: ')
        match opcion:
            case '1':
                do_selection_sort_clientes(lista_clientes, 'id')
                mostrar_datos_clientes(lista_clientes)
                os.system('pause')
                os.system('cls')
            case '2':
                do_selection_sort_clientes(lista_clientes, 'apellido')
                mostrar_datos_clientes(lista_clientes)
                os.system('pause')
                os.system('cls')
            case '3':
                do_selection_sort_clientes(lista_clientes, 'ciudad')
                mostrar_datos_clientes(lista_clientes)
                os.system('pause')
                os.system('cls')
            case '4':
                mostrar_datos_clientes(lista_clientes)
                ciudad_a_filtrar = texto_letras("ingrese la ciudad a filtrar: ")
                lista_filtrada = filtrar_clientes_por_ciudad(lista_clientes, ciudad_a_filtrar)
                if len(lista_filtrada) == 0:
                    print("no se encontraron clientes en la ciudad:", ciudad_a_filtrar)
                else:
                    do_selection_sort_clientes(lista_filtrada, 'apellido')
                    mostrar_datos_clientes(lista_filtrada)
                os.system('pause')
                os.system('cls')
            case '5':
                bucle = False