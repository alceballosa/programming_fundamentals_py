from claseLSL import LSL, Estudiante

mis_estudiantes = LSL()
for i in range(3):
    estudiante_nuevo = Estudiante(i)
    mis_estudiantes.insertarOrdenado(estudiante_nuevo)

mis_estudiantes.imprimirLista()
print(mis_estudiantes[0].notas)


### DEFINIR UNA FUNCIÓN EN LA CLASE ESTUDIANTE QUE CALCULE EL PROMEDIO DEL ESTUDIANTE ###

estudiante = mis_estudiantes[0]
promedio = estudiante.obtener_promedio()
print(f"El estudiante {estudiante.id}" tiene un promedio de {promedio})


### ELABORAR UN PEDAZO DE CÓDIGO QUE PERMITA CALCULAR EL PROMEDIO DEL SALÓN ###




### ELABORAR OTRO QUE SAQUE EL MÍNIMO Y EL MÁXIMO, Y QUIÉNES LAS TIENEN

