from claseLSL import LSL


class Pila(LSL):
    def __init__(self):
        LSL.__init__(self)

    def apilar(self, d):
        self.insertarAlPrincipio(d)

    def imprimirPila(self):
        """
        Recorre la pila y la imprime con formato
        """
        nodo = self.primerNodo()
        indice = 0
        print("\nPila:\n")
        while not self.finDeRecorrido(nodo):
            if nodo.liga is None:
                repr_liga = ""
            else:
                repr_liga = "\n"

            print(f"[p{indice}|{nodo.retornarDato()}]{repr_liga}", end="")
            nodo = nodo.retornarLiga()
            indice = indice + 1
        print("\n")

    def desapilar(self):
        dato = self.primero.retornarDato()
        self.eliminar(self.primero, anterior=None)
        return dato
