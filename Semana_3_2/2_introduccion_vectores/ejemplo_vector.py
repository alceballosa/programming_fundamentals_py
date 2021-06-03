"""
Ahora asumamos que queremos hacer un censo para Antioquia y sus 10 municipios (dato no verificado). En este caso, volvemos a tener las siguientes planillas:

- Identificador del municipio al que pertenece la casa
    - Número de personas

Los códigos son:

1. Medellín
2. Envigado
3. ...

125. Zaragoza

No podemos usar condicionales al ser tantos municipios, así que veamos una nueva estructura de datos, el vector.


"""

import vector as vec


def censoConVector(n_municipios):

    v_municipios = vec.construyeVector(tamano=n_municipios, val_inicial=0)

    while True:
        codigo = int(input("Ingrese el código del munic. de la vivienda: "))
        if codigo == 0:
            break

        if 1 <= codigo <= n_municipios:
            num_personas = int(input("Ingrese el número de personas en la vivienda : "))
            v_municipios[codigo] += num_personas
        else:
            print("Ha ingresado un código erroneo, intente otra vez")

    return v_municipios


n_municipios = 20
v_municipios = censoConVector(n_municipios)

for i in range(1, n_municipios + 1):
    print(f"El total de personas en el municipio {i} es {v_municipios[i]}.")