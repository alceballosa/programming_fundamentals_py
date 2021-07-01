import random
from test2 import diccionario_importado

diccionario_numeros = {}

for i in range(5):
    numero = random.randint(1,10)
    print(diccionario_numeros)
    diccionario_numeros[numero] = diccionario_numeros.get(numero, 0) + 1
    print("---------------------")

    
for key in diccionario_numeros.keys():
    print(key, "aparece", diccionario_numeros[key],"veces")


for value in diccionario_numeros.values():
    print(value)