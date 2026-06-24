def do_selection_sort_asc(lista: list[dict], clave_a_ordenar: str):
    for indice_fila in range(len(lista) - 1):
        indice_elem_menor = indice_fila
        for indice_sig_fila in range(indice_fila + 1, len(lista)):
            if lista[indice_elem_menor][clave_a_ordenar] > lista[indice_sig_fila][clave_a_ordenar]:
                indice_elem_menor = indice_sig_fila
            
        if indice_elem_menor != indice_fila:
            aux = lista[indice_elem_menor]
            lista[indice_elem_menor] = lista[indice_fila]
            lista[indice_fila] = aux

def do_selection_sort_des(lista: list[dict], clave_a_ordenar: str):
    for indice_fila in range(len(lista) - 1):
        indice_elem_mayor = indice_fila

        for indice_sig_fila in range(indice_fila + 1, len(lista)):
            if lista[indice_elem_mayor][clave_a_ordenar] < lista[indice_sig_fila][clave_a_ordenar]:
                indice_elem_mayor = indice_sig_fila

        if indice_elem_mayor != indice_fila:
            aux = lista[indice_elem_mayor]
            lista[indice_elem_mayor] = lista[indice_fila]
            lista[indice_fila] = aux


