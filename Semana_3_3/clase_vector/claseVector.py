import random


class vector:
    def __init__(self, n):
        """
        Crea un vector nuevo inicializado con valores None.
        El vector tiene n + 1 posiciones, donde la posición 0
        representa el número de posiciones llenas del vector.

        Nota: la clase vector está diseñada para manejar enteros.

        ------------------------------------------------------------

        Parámetros de entrada:
        n - el tamaño del vector (int)

        Valores de salida:
        Ninguno
        """
        self.n = n
        self.V = [None] * (n + 1)
        self.V[0] = 0

    def construyeVector(self, n, r=100):
        """
        Inicializa todas las posiciones de un vector con valores
        enteros aleatorios entre 1 y un limite superior
        rango.

        ------------------------------------------------------------

        Parámetros de entrada:
        n - hasta donde se inicializa el vector (int)
        r - limite superior del rango de valores posibles (int)

        Valores de salida:
        Ninguno
        """
        self.V[0] = n
        for i in range(1, n + 1):
            self.V[i] = random.randint(1, r)

    def imprimeVector(self, mensaje="vector sin nombre:\t"):
        """
        Imprime un mensaje y a continuación los valores llenos del vector.

        Se omiten en la impresión las posiciones vacías y la cantidad de posiciones
        llenas del vector.

        ------------------------------------------------------------

        Parámetros de entrada:
        mensaje - el mensaje que se quiere mostrar antes del vector (str)

        Valores de salida:
        Ninguno
        """

        print("\n", mensaje, end=" ")
        for i in range(1, self.V[0] + 1):
            print(self.V[i], end=", ")
        print()

    # FUNCIÓN NUEVA
    def posicionesUsadas(self):
        """
        Función para obtener la cantidad de posiciones llenas
        en el vector.

        ------------------------------------------------------------

        Valores de salida:
        Valor entero: Posiciones llenas en el vector.
        """
        return self.V[0]

    def __len__(self):
        return self.V[0]

    def __str__(self):
        return str(self.V)

    # FUNCIÓN NUEVA
    def tamagno(self):
        """
        Función para determinar el tamaño máximo de un vector

        ------------------------------------------------------------

        Valores de salida:
        Valor entero: tamaño del vector
        """
        return self.n

    # FUNCIÓN NUEVA
    def asignaNumeroElementos(self, m):
        """
        Función para asignar el número de elementos llenos del vector

        Si el vector "se encoge", convierte los elementos sobrantes en None.

        Si el tamaño "se agranda", convierte los nuevos elementos llenos en 0.

        ------------------------------------------------------------
        Parámetros de entrada:
        m - el nuevo numero de elementos llenos del vector (int)

        Valores de salida:
        Ninguno
        """

        if m > self.n:
            print(f"El vector no puede tener un # de elementos mayor a {self.n}.")
            return
        elif m == self.V[0]:
            print("El vector ya tiene ese tamaño.")
            return
        elif m > self.V[0]:
            # Convierte todos los elementos que no estaban llenos en 0.
            for i in range(1, self.V[0] + 1):
                if self.V[i] is None:
                    self.V[i] = 0
        else:
            # Convierte todos los elementos que quedan por fuera en None
            for i in range(self.V[i] + 1, self.n + 1):
                self.V[i] = None
            self.V[0] = m

    def esVacio(self):
        """
        Función para determinar si un vector está vacío.

        ------------------------------------------------------------

        Valores de salida:
        Valor booleano: True si el vector está vacío, False de lo contrario.
        """

        if self.V[0] == 0:
            return True
        else:
            return False

    def esLleno(self):
        """
        Función para determinar si un vector está lleno.

        ------------------------------------------------------------

        Valores de salida:
        Valor booleano: True si el vector está lleno, False de lo contrario.
        """

        if self.V[0] == self.n:
            return True
        else:
            return False

    def sumaDatos(self):
        """
        Función para obtener la suma de valores de un vector.

        ------------------------------------------------------------

        Valores de salida:
        Valor entero: sumatoria de los elementos del vector.
        """

        suma = 0
        for i in range(1, self.V[0] + 1):
            suma += self.V[i]
        return suma

    def agregarDato(self, d):
        """
        Función para agregar un dato a un vector
        al final.

        ------------------------------------------------------------

        Parámetros de entrada:
        d - el dato a ingresar en el vector (int)

        Valores de salida:
        Ninguno
        """
        if self.esLleno():
            print("El vector está lleno.")
        else:
            ultima_posicion = self.V[0]
            self.V[ultima_posicion + 1] = d
            self.V[0] += 1

    # FUNCIÓN NUEVA
    def asignaDato(self, d, i):
        """
        Función para asignar un dato a una posición del vector.

        ------------------------------------------------------------

        Parámetros de entrada:
        d - el dato a asignar en el vector (int)
        i - la posición en la que se va a asignar el dato (int)

        Valores de salida:
        Ninguno
        """
        if i > self.V[0]:
            print("Indice fuera del rango de valores llenos del vector")
        else:
            self.V[i] = d

    # FUNCIÓN NUEVA
    def retornaDato(self, i):
        """
        Función para obtener el dato que está en una posición dada del vector

        ------------------------------------------------------------

        Parámetros de entrada:
        i - la posición del dato que se quiere retornar (int)

        Valores de salida:
        valor entero: el dato que se encuentra en la posición seleccionada.
        """
        if i > self.V[0]:
            print("Indice fuera del rango de valores llenos del vector")
        else:
            return self.V[i]

    def mayor(self):
        """
        Función para encontrar la posición del
        mayor valor en un vector.

        Si el valor se encuentra repetido, se
        imprime la posición de la primera
        ocurrencia.

        ------------------------------------------------------------

        Valores de salida:
        Valor entero: posición del mayor dato en el vector.
        """
        mayor_dato = None
        posicion_mayor_dato = None

        for i in range(1, self.V[0] + 1):

            # el operador is es el == para comparar con None
            if mayor_dato is None or self.V[i] > mayor_dato:
                mayor_dato = self.V[i]
                posicion_mayor_dato = i

        return posicion_mayor_dato

    def menor(self):
        """
        Función para encontrar la posición del
        menor valor en un vector.

        Si el valor se encuentra repetido, se
        imprime la posición de la primera
        ocurrencia.

        ------------------------------------------------------------

        Valores de salida:
        Valor entero: posición del menor dato en el vector.
        """
        menor_dato = None
        posicion_menor_dato = None

        for i in range(1, self.V[0] + 1):

            # el operador is es el == para comparar con None
            if menor_dato is None or self.V[i] < menor_dato:
                menor_dato = self.V[i]
                posicion_menor_dato = i

        return posicion_menor_dato

    def intercambiar(self, i, j):
        """
        Función para intercambiar los valores de dos
        posiciones en un vector.

        Si las dos posiciones son inválidas, debe
        imprimir un mensaje de error.

        ------------------------------------------------------------

        Parámetros de entrada:
        i - la primera posición para el intercambio.
        j - la otra posición para el intercambio.

        Valores de salida:
        Ninguno
        """
        if i > self.V[0] or j > self.V[0]:
            print("Indices fuera del rango de valores llenos del vector")
        else:
            aux = self.V[i]
            self.V[i] = self.V[j]
            self.V[j] = aux

    # FUNCIÓN QUE ESTABA EN ordenamiento.py
    def seleccion(self):
        """
        Función para ordenar un vector mediante el método
        de ordenamiento por selección.

        Más información:
        https://www.ecured.cu/Algoritmo_de_ordenamiento_por_selecci%C3%B3n

        ------------------------------------------------------------

        Valores de salida:
        Ninguno
        """

        for i in range(1, self.V[0]):
            k = i
            for j in range(i + 1, self.V[0] + 1):
                if self.V[j] < self.V[k]:
                    k = j
            self.intercambiar(i, k)

    def buscarDondeInsertar(self, d):
        """
        Función para encontrar la posición en la que
        insertar un valor en un vector ordenado.

        ------------------------------------------------------------

        Parámetros de entrada:
        d - el dato que se desea insertar

        Valores de salida:
        Valor entero: posición en la que se va a insertar el valor.
        """
        i = 1
        while i <= self.V[0] and self.V[i] < d:
            i = i + 1
        return i

    # Caso de polimorfismo
    def insertar(self, d, i=0):
        """
        Función para insertar un valor en un vector
        en una posición dada.

        ------------------------------------------------------------

        Parámetros de entrada:
        d - el dato que se desea insertar (int)
        k - la posición en la que se va a insertar el valor (int)

        Valores de salida:
        Ninguno
        """

        if self.esLleno():
            print("Vector lleno, no se puede insertar")
            return
        elif i > self.V[0]:
            print("Posición fuera del rango de posiciones del vector.")
            return

        if i == 0:
            i = self.buscarDondeInsertar(d)

        for j in range(self.V[0], i - 1, -1):
            self.V[j + 1] = self.V[j]
        self.V[i] = d
        self.V[0] += 1

    def buscarDato(self, d):
        """
        Función para encontrar la posición de un valor
        en un arreglo.

        Si el valor se encuentra más de una vez, devuelve
        la primera posición en la que se encuentra.

        ------------------------------------------------------------

        Parámetros de entrada:
        d - el dato que se desea buscar

        Valores de salida:
        Valor entero: posición en la que se encuentra el valor.
        """
        i = 1
        while i <= self.V[0] and self.V[i] != d:
            i = i + 1
        if i <= self.V[0]:
            return i
        return -1

    def borrarDatoEnPosicion(self, i):
        """
        Función para borrar un valor de un vector,
        dada su posición.

        ------------------------------------------------------------

        Parámetros de entrada:
        V - el vector en el que se va a insertar el valor (vector)
        i - la posición del dato que se desea eliminar (int)

        Valores de salida:
        Ninguno (V es mutable, por lo tanto se modifica el vector original)
        """
        if i > self.V[0] or i <= 0:
            print("Posición fuera del rango de posiciones del vector.")
            return

        for j in range(i, self.V[0]):
            self.V[j] = self.V[j + 1]
        self.V[0] = self.V[0] - 1

    # FUNCIÓN NUEVA

    def borrarDato(self, d):
        """
        Función para buscar y borrar un valor de un vector.

        ------------------------------------------------------------

        Parámetros de entrada:
        d - el dato que se desea eliminar (int)

        Valores de salida:
        Ninguno
        """
        i = self.buscarDato(d)
        if i != -1:
            self.borrarDatoEnPosicion(i)
        else:
            print("Dato no encontrado.")
