import random

from claseLSL import LSL

mi_lista = LSL()
for i in range(3):
    mi_lista.insertarAlFinal(random.randint(0, 10))

mi_lista.imprimirLista()

nodo0 = mi_lista.primerNodo()
nodo1 = mi_lista.primerNodo().retornarLiga()
nodo2 = nodo1.retornarLiga()

mi_lista.intercambiar(nodo0, nodo1, nodo2)

mi_lista.imprimirLista()
