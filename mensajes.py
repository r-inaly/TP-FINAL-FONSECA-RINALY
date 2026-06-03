
def menu_principal():
    mensaje = """
1. Área Productos 

2. Área Clientes 

3. Salir del Sistema (Termina la ejecución))
    """
    print(mensaje)

def menu_productos_mensaje():
    return """ 
1 Cargar Producto 
2 Modificar Producto 
3 Ver Productos 
4 Borrar Producto 
5 Salir (Vuelve al Menú Principal) 
    """

def menu_productos_complemento_mensaje():
    mensaje = """
──► 1 Ordenar por ID ASC 
──► 2 Ordenar por Stock ASC 
──► 3 Ordenar por nombre ASC 
──► 4 Salir
    """
    print(mensaje)

def menu_clientes_mensaje():
    mensaje = """
1 Cargar Clientes 
2 Modificar Clientes 
3 Ver Clientes 
4 Borrar Clientes 
5 Salir (Vuelve al Menú Principal) 
    """
    print(mensaje)
    
    
def menu_dos_complemento():
    mensaje = """
──► 1 Ordenar por ID ASC 
──► 2 Ordenar por Apellido ASC 
    """
    print(mensaje)
