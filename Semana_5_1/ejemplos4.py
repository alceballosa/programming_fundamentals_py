from claseLSL import LSL
import random


mi_LSL = LSL()


print("Llenamos la lista...")
mi_LSL.insertarOrdenado(1)
mi_LSL.insertarOrdenado(50)
mi_LSL.insertarOrdenado(101)
for i in range(3):
    mi_LSL.insertarOrdenado(random.randint(1,100))
mi_LSL.imprimirLista()
print("La longitud de mi LSL es", len(mi_LSL))


print("\nBorramos el primer dato...")
mi_LSL.borrarDato(1)
mi_LSL.imprimirLista()

print("\nBorramos el último dato")
mi_LSL.borrarDato(101)
mi_LSL.imprimirLista()

print("\nBorramos un dato intermedio")
mi_LSL.borrarDato(50)
mi_LSL.imprimirLista()