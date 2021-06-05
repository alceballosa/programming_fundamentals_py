from claseVector import vector

n = int(input("Entre tamaño del vector: "))
vec = vector(n)

porcion_a_llenar = n // 2
vec.construyeVector(porcion_a_llenar, 100)
vec.imprimeVector("Vector de prueba")
mayda = vec.mayor()
menda = vec.menor()
print("El mayor dato está en la posición ", mayda, "y es", vec.retornaDato(mayda))
print("El menor dato está en la posición ", menda, "y es", vec.retornaDato(menda))
vec.seleccion()
vec.imprimeVector("Vector de prueba ordenado")
