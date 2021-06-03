import random

"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O         o   O
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o        O   o
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo       o   o
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O       OooOOo
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o           O
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O           o
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O           O
"""


def creaVector(n):
    """
    Crea un vector nuevo inicializado con valores None.
    El vector tiene n + 1 posiciones, donde la posición 0
    representa el número de posiciones llenas del vector.

    Nota: la clase vector está diseñada para manejar enteros.

    ------------------------------------------------------------

    Parámetros de entrada:

    n - el tamaño del vector (int)

    Valores de salida:

    El vector.
    """
    v = [None] * (n + 1)
    v[0] = 0
    return v


# En la documentación esta función se conoce como construyeVector,
# pero realmente lo que hace es inicializar sus valores.
def inicializaVector(V, n, rango):
    """
    Inicializa todas las posiciones de un vector con valores
    enteros aleatorios entre 1 y un limite superior
    rango.

    ------------------------------------------------------------

    Parámetros de entrada:

    V - el vector a modificar (vector)
    n - hasta donde se inicializa el vector (int)
    rango - limite superior del rango de valores posibles (int)



    Valores de salida:
    Ninguno (V es mutable, por lo tanto se modifica el vector original)
    """

    V[0] = n
    for i in range(1, n + 1):
        V[i] = random.randint(1, rango)


def imprimeVector(V, mensaje="Vector sin nombre"):
    """
    Imprime un mensaje y a continuación los valores llenos del vector.

    Se omiten en la impresión las posiciones vacías y la cantidad de posiciones
    llenas del vector.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a imprimir (vector)


    Valores de salida:
    Ninguno
    """

    print("\n", mensaje, end=":\n")
    for i in range(1, V[0] + 1):
        print(V[i], end=", ")


def esVacio(V):
    """
    Función para determinar si un vector está vacío.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a revisar (vector)


    Valores de salida:
    Valor booleano: True si el vector está vacío, False de lo contrario.
    """

    if V[0] == 0:
        return True
    else:
        return False


def esLleno(V, n):
    """
    Función para determinar si un vector está lleno.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a revisar (vector)


    Valores de salida:
    Valor booleano: True si el vector está lleno, False de lo contrario.
    """

    if V[0] == n:
        return True
    else:
        return False


def sumaVector(V):
    """
    Función para obtener la suma de valores de un vector.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector al que se le va a calcular la suma de elementos (vector)


    Valores de salida:
    Valor entero: sumatoria de los elementos del vector.
    """

    suma = 0
    for i in range(1, V[0] + 1):
        suma += V[i]
    return suma


# Implementemos juntos las siguientes funcionalidades


def agregarDato(d, V, n):
    """
    Función para agregar un dato a un vector
    al final.

    ------------------------------------------------------------

    Parámetros de entrada:
    d - el dato a ingresar en el vector (int)
    V - el vector al que se le va a agregar el dato (vector)
    n - el tamaño del vector (int)

    Valores de salida:
    Ninguno (V es mutable, por lo tanto se modifica el vector original)
    """
    if esLleno(V, n):
        print("El vector está lleno.")
    else:
        ultima_posicion = V[0]
        V[ultima_posicion + 1] = d
        V[0] += 1


def mayorDato(V):
    """
    Función para encontrar la posición del
    mayor valor en un vector.

    Si el valor se encuentra repetido, se
    imprime la posición de la primera
    ocurrencia.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a revisar (vector)

    Valores de salida:
    Valor entero: posición del mayor dato en el vector.
    """
    mayor_dato = None
    posicion_mayor_dato = None

    for i in range(1, V[0] + 1):

        # el operador is es el == para comparar con None
        if mayor_dato is None or V[i] > mayor_dato:
            mayor_dato = V[i]
            posicion_mayor_dato = i

    return posicion_mayor_dato


def menorDato(V):
    """
    Función para encontrar la posición del
    menor valor en un vector.

    Si el valor se encuentra repetido, se
    imprime la posición de la primera
    ocurrencia.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a revisar (vector)

    Valores de salida:
    Valor entero: posición del menor dato en el vector.
    """
    menor_dato = None
    posicion_menor_dato = None

    for i in range(1, V[0] + 1):

        # el operador is es el == para comparar con None
        if menor_dato is None or V[i] < menor_dato:
            menor_dato = V[i]
            posicion_menor_dato = i

    return posicion_menor_dato



def intercambiar(V, i, j):
    """
    Función para intercambiar los valores de dos
    posiciones en un vector.

    Si las dos posiciones son inválidas, debe
    imprimir un mensaje de error.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector donde se hará el intercambio (vector)
    i - la primera posición para el intercambio.
    j - la otra posición para el intercambio.

    Valores de salida:
    Ninguno (V es mutable, por lo tanto se modifica el vector original)
    """
    if i > V[0] or j > V[0]:
        print("Indices fuera del rango del vector")
    else:
        aux = V[i]
        V[i] = V[j]
        V[j] = aux
        


"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O         .oOOo.
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o        O
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo       o
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O       OoOOo.
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o       O    O
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O       O    o
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O       `OooO'
"""


def buscarDondeInsertar(V, d):
    """
    Función para encontrar la posición en la que
    insertar un valor en un vector ordenado.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector en el que se va a insertar el valor (vector)
    d - el dato que se desea insertar

    Valores de salida:
    Valor entero: posición en la que se va a insertar el valor.
    """
    pass


def insertar(V, d, k):
    """
    Función para insertar un valor en un vector
    en una posición dada.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector en el que se va a insertar el valor (vector)
    d - el dato que se desea insertar (int)
    k - la posición en la que se va a insertar el valor (int)

    Valores de salida:
    Ninguno (V es mutable, por lo tanto se modifica el vector original)
    """
    pass


"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O         OooOoO
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o             o
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo            O
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O           O
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o          O
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O         o
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O        O
"""


def buscarDato(V, d):
    """
    Función para encontrar la posición de un valor
    en un arreglo.

    Si el valor se encuentra más de una vez, devuelve
    la primera posición en la que se encuentra.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector en el que se hará la búsqueda (vector)
    d - el dato que se desea buscar

    Valores de salida:
    Valor entero: posición en la que se encuentra el valor.
    """
    pass


def borrar(V, i):
    """
    Función para borrar un valor de un vector,
    dada su posición.

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector en el que se va a insertar el valor (vector)
    i - la posición del dato que se desea eliminar (int)

    Valores de salida:
    Ninguno (V es mutable, por lo tanto se modifica el vector original)
    """
    pass
