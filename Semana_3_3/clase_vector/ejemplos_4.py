import random

from claseVector import vector

n = int(input("Entre tamaño del vector "))
v = vector(n)
v.construyeVector(n // 2)
print("VECTOR CONSTRUIDO, tamaño = ", v.tamagno(), end=",")
print("Posiciones usadas: ", v.posicionesUsadas())
v.imprimeVector("Primer vector construido ")
v.agregarDato(69)
v.imprimeVector("vector luego de agregar el dato 69: ")
v.seleccion()
v.imprimeVector("Vector ordenado ")
s = v.sumaDatos()
print("Los datos suman: ", s)
k = v.posicionesUsadas()
n = v.tamagno()
print("\nLas posiciones usadas son: ", k, "y el tamaño es", n)
v.agregarDato(105)
lleno = False
while not lleno:
    r = random.randint(1, 99)
    v.agregarDato(r)
    lleno = v.esLleno()
v.imprimeVector("vector después de llenarlo con datos aleatorios")
may = v.mayor()
print("\nEl mayor dato es", v.retornaDato(may), end=",")
print("y está en la posición ", may)
v.V[0] = v.V[0] - 5
d = 69
k = v.buscarDato(d)
if k != -1:
    print("\nEl dato", d, "se halla en la posición: ", k)
else:
    print("\nEl dato", d, "no se encontró")
v.seleccion()
v.imprimeVector("Vector despuésde volverlo a ordenar")
i = v.buscarDondeInsertar(13)
v.insertar(13, i)
v.imprimeVector("Vector después de insertar el 13: ")
d = 13
i = v.buscarDato(d)
if i != -1:
    print("\nEl dato", d, "se halla en la posición: ", i)
else:
    print("\nEl dato", d, "no se encontró")
v.borrarDatoEnPosicion(i)
v.imprimeVector("vector después de borrar el 13: ")
v.insertar(39)
v.imprimeVector("Vector después de insertar el 39 en el sitio que es: ")
v.insertar(18, 2)
v.imprimeVector("vector después de insertar el 18 en la posición 2: ")
v.borrarDato(19)
v.imprimeVector("Vector después de borrar el 19: ")
