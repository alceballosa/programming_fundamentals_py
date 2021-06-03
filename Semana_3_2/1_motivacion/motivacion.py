"""
Consolidemos un censo en Medellín, simulando que leemos
las planillas que ya llenó el personal.

- Vivienda
    - Número de personas

Cada vivienda está identificada por un número (no tiene que ser único en esta implementación)
y por cada vivienda se cuentan las personas en esta y se añaden a un total.

"""


def censoMedellin():

    total_pers = 0

    while True:
        n_vivienda = int(input("Ingrese el número de la vivienda: "))
        if n_vivienda == 0:
            break
        n_personas = int(
            input(f"Ingrese el número de personas en la vivienda {n_vivienda}: ")
        )
        total_pers += n_personas

    return total_pers


conteo_pers = censoMedellin()
print("El total de personas en Medellín es {}".format(conteo_pers))
