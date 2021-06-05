from claseVector import vector

n = int(input("Entre tamaño del primer vector: "))
a = vector(n)
a.construyeVector(a.tamagno())
m = int(input("Entre tamaño del segundo vector: "))
b = vector(m)
b.construyeVector(m)
a.seleccion()
b.seleccion()
c = vector(m + n)
i = 1
j = 1


# Intercala datos mientras ambos vectores aún tengan datos
# Siempre toma el valor menor entre los dos arreglos, ojo
# que estos estan ordenados.
while i <= a.posicionesUsadas() and j <= b.posicionesUsadas():
    if a.retornaDato(i) < b.retornaDato(j):
        c.agregarDato(a.retornaDato(i))
        i = i + 1
    else:
        c.agregarDato(b.retornaDato(j))
        j = j + 1

# Si quedaron sobrando datos en a, los agrega todos al final
while i <= a.retornaDato(0):
    c.agregarDato(a.retornaDato(i))
    i = i + 1

# Si quedaron sobrando datos en b, los agrega todos al final
while j <= b.retornaDato(0):
    c.agregarDato(b.retornaDato(j))
    j = j + 1


# Cuando ya no quedan datos por intercalar en a ni en b,
# se muestra el resultado.
a.imprimeVector("Vector 1 de prueba")
b.imprimeVector("Vector 2 de prueba")
c.imprimeVector("Vector resultado de la intercalación")
