import random

from claseLSL import LSL
from claseLSL import Estudiante

mi_lista = LSL()
for i in range(5):
    mi_lista.insertarAlFinal(Estudiante(random.randint(0, 100)))

mi_lista.imprimirLista()

# nodo1_prev = mi_lista[0]
# nodo1 = mi_lista[1]

# nodo2_prev = mi_lista[3]
# nodo2 = mi_lista[4]

# mi_lista.intercambiar(nodo1, nodo1_prev, nodo2, nodo2_prev)
mi_lista.ordenamientoPorSeleccion()

mi_lista.imprimirLista()
