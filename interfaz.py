import os
from mensajes import (
    menu_principal, menu_productos_mensaje, menu_clientes_mensaje, menu_productos_complemento_mensaje
)
from logica import (
    cargar_producto
)

def interfaz_principal(matriz: list[list]):
    bucle = True
    while(bucle):
        os.system('cls')
        menu_principal()
        opcion = input(f'Ingrese una opcion entre: [1-3]: ')
        match opcion:
            case '1':
                menu_productos(matriz)
                os.system('pause')
                os.system('cls')
            case '2':
                menu_clientes_mensaje()
                os.system('pause')
                os.system('cls')
            case '3':
                bucle = False

    os.system('pause')
    os.system('cls')


def menu_productos(matriz: list[list]):
    bucle = True
    while(bucle):
        os.system('cls')
        mensaje = menu_productos_mensaje()
        opcion = input(mensaje)
        match opcion:
            case '1':
                matriz = cargar_producto()
                os.system('pause')
                os.system('cls')
            case '2':
                print("opcion 2")
                os.system('pause')
                os.system('cls')
            case '3':
                os.system('cls')
                menu_productos_complemento()
                os.system('pause')
                os.system('cls')
            case  '4':
                print("opcion 4")
                os.system('pause')
                os.system('cls')
            case '5':
                bucle = False

def menu_productos_complemento():
    bucle = True
    while(bucle):
        os.system('cls')
        menu_productos_complemento_mensaje()
        opcion = input(f'ingrese un numero 1-4:')
        match opcion:
            case '1':
                print("opcion 1")
                os.system('pause')
                os.system('cls')
            case '2':
                print("opcion 2")
                os.system('pause')
                os.system('cls')
            case '3':
                print("opcion 3")
                os.system('pause')
                os.system('cls')
            case '4':
                bucle = False