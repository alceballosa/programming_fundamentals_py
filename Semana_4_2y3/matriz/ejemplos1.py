def crear_volumen(filas, columnas, volumen, val):
    mat = [] * filas
    for i in range(filas):
        col = [] * columnas
        for j in range(volumen):
            vol = [val] * volumen
            col.append(vol)
        mat.append(col)

    return mat


def crear_matriz(filas, columnas, val):
    mat = [] * filas
    for i in range(filas):
        a = [val] * columnas
        mat.append(a)

    return mat


val = 20
mi_matriz = crear_matriz(8, 3, val)

print(mi_matriz)

# Si hago mi_matriz[0] = 10, estoy dañando la estructura de la matriz.
# Siempre acceder por los dos índices
mi_matriz[0][0] = 5
print(mi_matriz)

#El acceso por [n,n] no está definido
#mi_matriz[0, 0] = 10
#print(mi_matriz)

filas =len(mi_matriz)
columnas =len(mi_matriz[0])

print(f"El tamaño de matriz es {filas, columnas}")

for i in range(filas):
    print("[ ", end ="")
    for j in range(columnas):
        print(mi_matriz[i][j], end = " ")
    print("]")