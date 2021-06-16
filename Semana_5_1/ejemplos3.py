from claseLSL import LSL

mi_LSL = LSL()

print("\nIntentamos borrar en la lista vacía...")

mi_LSL.borrarDato(1)

print("\nInsertamos un solo dato...")
mi_LSL.insertarOrdenado(10)
mi_LSL.imprimirLista()

print("\nLo borramos...")
mi_LSL.borrarDato(10)
mi_LSL.imprimirLista()


print("\nInsertamos dos más...")
mi_LSL.insertarOrdenado(10)
mi_LSL.insertarOrdenado(20)
mi_LSL.imprimirLista()