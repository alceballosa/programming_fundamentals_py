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
vector.inicializaVector(vec1, 16, 99)
vector.imprimeVector(vec1, "Vector inicializado aleatoriamente")
print("Resultado de preguntar si el vector está vacío:", vector.esLleno(vec1))



# %%
# Borrar dos datos en un vector
for i in range(2):
    pos_borrar = int(input("Ingrese la posición para borrar en el vector: "))
    vector.borrar(vec1, pos_borrar)
vector.imprimeVector(vec1, "Vector tras borrar datos")


#%%
# Agregar un dato nuevo al final
dato_nuevo = int(input("Ingrese un valor para añadir al vector"))
vector.agregarDato(50, vec1, tamano)



#%%
# Agregar un dato nuevo en una posición arbitraria


#%%
# Obtener el menor y el mayor dato del arreglo

#%%
# Intercambiar los valores de dos posiciones en el vector


#%%
# Ordenar un vector


#%%
# Insertar un dato en un vector ordenado


#%%
# Buscar un dato en un vector ordenado
