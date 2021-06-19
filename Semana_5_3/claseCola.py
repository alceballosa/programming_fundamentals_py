from claseLSL import LSL


class Cola(LSL):
    def __init__(self):
        """
        Constructor.
        Llama al constructor de la lista simplemente ligada.
        """
        LSL.__init__(self)

    def imprimirCola(self):
        """
        Imprime la cola con un formato interesante.
        """
        nodo = self.primerNodo()
        indice = 0
        print("\nCola:\n")
        while not self.finDeRecorrido(nodo):
            if nodo.liga is None:
                repr_liga = "... fin de la cola"
            else:
                repr_liga = "\n"

            print(f"[p{indice}|{nodo.retornarDato()}]{repr_liga}", end="")
            nodo = nodo.retornarLiga()
            indice = indice + 1
        print("\n")

    def encolar(self, dato):
        """
        Coloca un dato al final de la cola.
        """
        self.insertarAlFinal(dato)

    def desencolar(self):
        """
        Saca el dato que está en la primera posición en la cola.

        Retorna el dato.
        """
        if self.esVacia():
            print("La cola está vacía, no hay nada para desencolar.")
            return None
        else:
            d = self.primero.retornarDato()
            self.eliminar(self.primero, None)
            return d

    def siguiente(self):
        """
        Dice cuál es el próximo en salir de la cola -es decir, el primero-.
        """
        return self.primero.retornarDato()
