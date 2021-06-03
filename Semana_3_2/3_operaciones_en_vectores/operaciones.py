# %%
import busqueda
import ordenamiento
import vector

# %%
# Creación del vector
tamano = 30
vec1 = vector.creaVector(tamano)
vector.imprimeVector(vec1, "Vector al comenzar")
print("Resultado de preguntar si el vector está vacío:", vector.esVacio(vec1))


# %%
# Inicialización del vector
vector.inicializaVector(vec1, tamano//2, 99)
vector.imprimeVector(vec1, "Vector inicializado aleatoriamente")
print("Resultado de preguntar si el vector está vacío:", vector.esLleno(vec1, tamano))


#%%
total = vector.sumaVector(vec1)
print("El total de valores en vector es:",total)


#%%
# Agregar un dato nuevo al final
dato_nuevo = int(input("Ingrese un valor para añadir al vector: "))
vector.agregarDato(dato_nuevo, vec1, tamano)
vector.imprimeVector(vec1, "Vector tras agregar "+str(dato_nuevo))

#%%
# Obtener el menor y el mayor dato del arreglo

mayor = vector.mayorDato(vec1)
menor = vector.menorDato(vec1)

print(f"El mayor dato está en {mayor} -> {vec1[mayor]} y el menor está en {menor} -> {vec1[menor]}")



#%%
# Intercambiar los valores de dos posiciones en el vector
pos1 = 2
pos2 = 11

vector.imprimeVector(vec1, "Vector antes del intercambio")
vector.intercambiar(vec1, pos1, pos2)
vector.imprimeVector(vec1, "Vector después del intercambio")

# %%
# Borrar dos datos en un vector
for i in range(2):
    pos_borrar = int(input("Ingrese la posición para borrar en el vector: "))
    vector.borrar(vec1, pos_borrar)
vector.imprimeVector(vec1, "Vector tras borrar datos")




#%%
# Agregar un dato nuevo en una posición arbitraria





#%%
# Ordenar un vector


#%%
# Insertar un dato en un vector ordenado


#%%
# Buscar un dato en un vector ordenado
