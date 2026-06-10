def texto_letras(mensaje_input):
    valor = input(mensaje_input)
    
    if valor == "":
        print("el ingreso no puede estar vacio.")
        
    solo_letras = True
    for caracter in valor:
        if not caracter.isalpha() and caracter != " ":
            todo_alfabetico = False

    if solo_letras == False:
        print("el ingreso debe contener solo caracteres alfabeticos o espacios.")
    
    return valor