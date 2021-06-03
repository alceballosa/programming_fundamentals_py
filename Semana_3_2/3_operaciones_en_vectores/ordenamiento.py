from vector import intercambiar

"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O         .oOOo.
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o        O    o
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo       o    O
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O       `OooOo
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o            O
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O            o
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O       `OooO'
"""


def seleccion(V):
    """
    Función para ordenar un vector mediante el método
    de ordenamiento por selección.

    Más información: https://www.ecured.cu/Algoritmo_de_ordenamiento_por_selecci%C3%B3n

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a ordenar (vector)


    Valores de salida:
    Ninguno (V es mutable, por lo tanto se ordena el vector original)
    """

    for i in range(1, V[0]):
        k = i
        for j in range(i + 1, V[0] + 1):
            if V[j] < V[k]:
                k = j
        intercambiar(V, i, k)


"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O          oO   .oOOo.
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o          O   O    o
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo         o   o    O
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O         O   o    o
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o         o   O    O
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O         O   o    O
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O       OooOO `OooO'
"""


def burbuja(V):
    """
    Función para ordenar un vector mediante el método
    de ordenamiento de burbuja.

    Más información: https://www.ecured.cu/Ordenamiento_de_burbuja

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a ordenar (vector)


    Valores de salida:
    Ninguno (V es mutable, por lo tanto se ordena el vector original)
    """
    for i in range(1, V[0]):
        for j in range(1, V[0] - i + 1):
            if V[j] > V[j + 1]:
                intercambiar(V, j, j + 1)


"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O          oO    oO
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o          O     O
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo         o     o
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O         O     O
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o         o     o
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O         O     O
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O       OooOO OooOO
"""

def insercion(V):
    """
    Función para ordenar un vector mediante el método
    de ordenamiento por inserción.

    Más información: https://www.ecured.cu/Ordenamiento_por_Inserci%C3%B3n

    ------------------------------------------------------------

    Parámetros de entrada:
    V - el vector que se va a ordenar (vector)


    Valores de salida:
    Ninguno (V es mutable, por lo tanto se ordena el vector original)
    """
    for i in range(2, V[0] + 1):
        d = V[i]
        j = i - 1
        while j > 0 and V[j] > d:
            V[j + 1] = V[j]
            j = j - 1

        V[j + 1] = d
