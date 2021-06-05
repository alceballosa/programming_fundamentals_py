from claseVector import vector

n = int(input("Entre tamaño del vector: "))
vec = vector(n)

porcion_a_llenar = vec.tamagno() // 2
vec.construyeVector(porcion_a_llenar, 100)
vec.imprimeVector("Vector de prueba creado")
vec.agregarDato(13)
vec.imprimeVector("Vector con dato agregado")
vec.seleccion()
vec.imprimeVector("Vector ordenado ascendentemente")
i = vec.buscarDondeInsertar(39)
vec.insertar(39, i)
vec.imprimeVector("Vector con dato 39 insertado")
vec.insertar(44)
vec.imprimeVector("Vector con dato 44 insertado")
