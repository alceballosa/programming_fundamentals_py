def saludar(nombre, titulo = ""):
    """
    Esta función recibe un nombre y un título
    e imprime un saludo personalizado.
    
    --- nombre: primer nombre de la persona.
    --- titulo: título de la persona (opcional).
    
    """
    if titulo:
        saludo = f"Hola {titulo} {nombre}"
    else:
        saludo = f"Hola {nombre}"
    print(saludo + ", es un gusto verle por aquí.")


def saludar_con_apellido(nombre, apellido, titulo = ""):
    """
    Esta función recibe un nombre, un apellido y un título
    e imprime un saludo personalizado.
    
    --- nombre: primer nombre de la persona.
    --- apellido: primer apellido de la persona.
    --- titulo: título de la persona (opcional).
    
    """
    if titulo:
        saludo = f"Hola {titulo} {nombre} {apellido}"
    else:
        saludo = f"Hola {nombre} {apellido}"
    print(saludo + ", es un gusto verle por aquí.")
