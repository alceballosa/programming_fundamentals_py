from claseLSL import LSL
import random


mi_LSL = LSL()


print("Llenamos la lista...")
for i in range(6):
    mi_LSL.insertarOrdenado(random.randint(1,100))
mi_LSL.imprimirLista()

posicion = 5
dato = mi_LSL[posicion]
print(f"Dato en la posición {posicion}: {dato}")

#print("\nProbemos varios valores...")
#posicion = 7
#dato = mi_LSL[posicion]
#print(f"Dato en la posición {posicion}: {dato}")