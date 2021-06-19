from claseCola import Cola
import random

cola = Cola()

for i in range(4):
    cola.encolar(random.randint(1,10))

cola.imprimirCola()

cola.encolar(6)
cola.imprimirCola()

d = cola.desencolar()
print(f"El dato {d} sale de la cola.")

d = cola.desencolar()
print(f"El dato {d} sale de la cola.")

sig = cola.siguiente()
print(f"El siguiente dato por salir de la cola es {sig}")

cola.imprimirCola()


d = cola.desencolar()
print(f"El dato {d} sale de la cola.")

d = cola.desencolar()
print(f"El dato {d} sale de la cola.")

cola.imprimirCola()

d = cola.desencolar()
print(f"El dato {d} sale de la cola.")

d = cola.desencolar()
print(f"El dato {d} sale de la cola.")

cola.imprimirCola()