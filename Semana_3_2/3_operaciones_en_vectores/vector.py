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

    ------------------------------------------------------------

    Parámetros de entrada:

    n - el tamaño del vector (int)

    Valores de salida:

    El vector.
    """

    return [0] * (n + 1)


# En la documentación esta función se conoce como construyeVector,
# pero realmente lo que hace es inicializar sus valores.
def inicializaVector(V, n, rango):
    """
    Inicializa los valores de un vector con valores
    enteros aleatorios entre 1 y un limite superior
    rango.

    ------------------------------------------------------------

    Parámetros de entrada:

    V - el vector a modificar (vector)
    n - el tamaño del vector (int)
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


#Implementemos juntos las siguientes funcionalidades

def agregarDato(d, V, n):
    pass


def mayorDato(V):
    pass


def menorDato(V):
    pass


def intercambiar(V, i, j):
    pass


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
    pass


def insertar(V, d, k):
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
    pass


def borrar(V, i):
    pass
