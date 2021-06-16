from claseLSL import LSL

"""
EJEMPLOS CON UNA LISTA SIMPLEMENTE LIGADA EN ORDEN
"""

mi_LSL = LSL()

mi_LSL.insertarOrdenado(10)
mi_LSL.imprimirLista()
mi_LSL.insertarOrdenado(5)
mi_LSL.insertarOrdenado(21)
mi_LSL.insertarOrdenado(21)
mi_LSL.imprimirLista()
print("La longitud de mi LSL es", len(mi_LSL))