

def es_primo(numero):

    """
    Esta función recibe un número entero y retorna un valor booleano
    indicando si es o no es primo.
    
    Entradas:
    --- numero: valor entero.
    
    Salida:
    --- valor booleano.
    """
    if numero == 2:
        return True
    elif numero%2 == 0:
        return False
    else:
        i = 3
        while i < int(numero**(1/2))+1:
            if numero%i == 0:
                return False
            i+=2
        return True
        