"""
Consolidemos un censo en Medellín, Montería y Cali,
simulando que leemos las planillas que ya llenó el
personal.

- Identificador del municipio al que pertenece la casa
    - Número de personas


En este ejercicio ya no se identifican las casas
(si se dan cuenta, esta información no se usaba
en el anterior ejercicio). Solo se pide por teclado
el código del municipio al que pertenece la vivienda
y por cada vivienda se cuentan las personas en esta
y se añaden a un total.

Los códigos son:

1. Cali
2. Medellín
3. Montería

"""


def censoIntermunicipal():

    tp_cali = 0
    tp_mede = 0
    tp_mont = 0

    while True:
        codigo = int(input("Ingrese el código del munic. de la vivienda: "))
        if codigo == 0:
            break
        num_personas = int(input("Ingrese el número de personas en la vivienda : "))

        if codigo == 1:
            tp_cali += num_personas
        elif codigo == 2:
            tp_mede += num_personas
        elif codigo == 3:
            tp_mont += num_personas
        else:
            print("Ha ingresado un código erroneo, intente otra vez")

    return tp_cali, tp_mede, tp_mont


tp_cali, tp_mede, tp_mont = censoIntermunicipal()

print(f"El total de personas en Cali es {tp_cali}.")
print(f"El total de personas en Medellín es {tp_mede}.")
print(f"El total de personas en Montería es {tp_mont}.")