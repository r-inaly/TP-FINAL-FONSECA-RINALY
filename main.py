import os
from mensajes import (
    menu_principal_mensaje
)
from interfaz import (
    menu_productos,
    menu_clientes
)

def main():
    productos_sistema = []  
    clientes_sistema = []   
    
    bucle = True
    while bucle:
        os.system('cls')
        menu_principal_mensaje()
        opcion = input('ingrese una opcion entre 1-3:')
        
        match opcion:
            case '1':
                menu_productos(productos_sistema)
            case '2':
                menu_clientes(clientes_sistema)
            case '3':
                print("saliendo del sistema...")
                bucle = False
            case _:
                print("opcion invalida.")
                os.system('pause')

if __name__ == "__main__":
    main()