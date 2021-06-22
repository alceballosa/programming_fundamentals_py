import random



class Estudiante:
    def __init__(self, id):
        self.id = id
        self.notas = []
        for i in range(5):
            self.notas.append(random.randint(0, 5))

    #igual a
    def __eq__(self, other):
        son_iguales = self.id == other.id
        return son_iguales

    #mayor que
    def __gt__(self, other):
        mayor_que = self.id > other.id
        return mayor_que

    #diferente de
    def __ne__(self, other):
        diferente = self.id != other.id
        return diferente


class nodoSimple:
    def __init__(self, d=None):
        self.dato = d
        self.liga = None

    def asignarDato(self, d):
        self.dato = d

    def asignarLiga(self, x):
        self.liga = x

    def retornarDato(self):
        return self.dato

    def retornarLiga(self):
        return self.liga


class LSL:
    def __init__(self):  # Constructor
        self.primero = None
        self.ultimo = None

    def primerNodo(self):
        return self.primero

    def ultimoNodo(self):
        return self.ultimo

    def esVacia(self):
        return self.primero is None

    def finDeRecorrido(self, p):
        return p is None

    def imprimirLista(self):
        """
        Recorre la lista y la imprime con formato
        """
        nodo = self.primerNodo()
        indice = 0
        print("Lista: ")
        while not self.finDeRecorrido(nodo):
            if nodo.liga is None:
                repr_liga = ""
            else:
                repr_liga = "->"

            print(f"[p{indice}|{nodo.retornarDato()}]{repr_liga}", end="")
            nodo = nodo.retornarLiga()
            indice = indice + 1
        print("\n")

    def insertarAlPrincipio(self, d):
        """
        Ingresa un dato en un nuevo nodo al principio de la lista.
        No mantiene el orden de la lista.
        """
        nuevo = nodoSimple(d)
        primero = self.primerNodo()
        if primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.liga = self.primero
            self.primero = nuevo

    def insertarAlFinal(self, d):
        """
        Ingresa un dato en un nuevo nodo al final de la lista.
        No mantiene el orden de la lista.
        """
        nuevo = nodoSimple(d)
        primero = self.primerNodo()
        if primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.liga = nuevo
            self.ultimo = nuevo

    def buscarDondeInsertar(self, dato):
        """
        Busca el nodo después del que debería ir un nuevo valor en una LSL.

        Si el elemento va a ser el primero de la lista o si la lista está vacía,
        devuelve None.
        """
        nodo = self.primerNodo()
        despues_de = None
        while not self.finDeRecorrido(nodo) and nodo.retornarDato() < dato:
            despues_de = nodo
            nodo = nodo.retornarLiga()
        return despues_de

    def insertarOrdenado(self, dato):
        """
        Inserta un dato en una LSL ordenada. Este método mantiene el orden.
        """
        despues_de = self.buscarDondeInsertar(dato)
        nuevo = nodoSimple(dato)
        self.colocarDespues(nuevo, despues_de)

    def colocarDespues(self, nuevo, despues_de):
        """
        Esta función coloca un nuevo nodo después de otro en
        una LSL.
        """
        # Pueden darse dos casos si el valor de 'despues_de' es None:
        if despues_de is None:
            # Si el primero es None, significa que la lista está vacía
            if self.primero is None:
                self.ultimo = nuevo
            # De lo contrario, nuestro nuevo nodo va a ser el primero
            # de una lista que ya tiene valores
            else:
                nuevo.asignarLiga(self.primero)

            self.primero = nuevo
            return

        # Si el valor de 'despues_de' no es None, significa
        # que va en una posición intermedia o en la última.
        nuevo.asignarLiga(despues_de.retornarLiga())
        despues_de.asignarLiga(nuevo)
        if despues_de == self.ultimo:
            self.ultimo = nuevo

    def longitud(self):
        """
        Obtiene la longitud de la LSL.
        """
        nodo = self.primerNodo()
        n = 0
        while not self.finDeRecorrido(nodo):
            n = n + 1
            nodo = nodo.retornarLiga()
        return n

    def __len__(self):
        """Retorna la longitud de la lista con el operador len()"""
        return self.longitud()

    def buscarDatoYAnterior(self, dato):
        """
        Busca el nodo que contiene un dato y el nodo anterior a este.

        Si el dato está más de una vez en la lista, se toma la primera aparición.

        _________________________
        Si el dato es el primero:

        anterior -> None
        nodo -> primero
        _________________________
        Si el dato es el último:

        anterior -> penultimo
        nodo -> ultimo
        _________________________
        Si el dato no está:

        anterior -> ultimo
        nodo -> None
        """
        anterior = None
        nodo = self.primerNodo()
        while not self.finDeRecorrido(nodo) and nodo.retornarDato() != dato:
            anterior = nodo
            nodo = nodo.retornarLiga()
        return nodo, anterior

    def borrarDato(self, dato):

        """
        Busca un dato en la lista. Si lo encuentra, lo elimina.
        """

        nodo, anterior = self.buscarDatoYAnterior(dato)

        if nodo is None:
            print("Dato no está en la lista")
            return
        else:
            self.eliminar(nodo, anterior)

    def eliminar(self, nodo, anterior):
        """
        Se elimina un nodo. Para esto, primero se desconecta el
        anterior del nodo a eliminar y la conexión se reemplaza
        por la del nodo siguiente.
        """
        if anterior is None:
            self.primero = nodo.retornarLiga()
            if self.esVacia():
                self.ultimo = None
        else:
            anterior.asignarLiga(nodo.retornarLiga())
            if nodo == self.ultimo:
                self.ultimo = anterior

    def __getitem__(self, index):
        """
        Sobrecarga para poder acceder a los datos de la lista por su posición: mi_lsl[0]
        , mi_lsl[2]...
        """
        if self.esVacia():
            raise IndexError("Lista vacía.")
        else:
            nodo = None
            j = 0
            while j <= index:
                if j == 0:
                    nodo = self.primero
                else:
                    nodo = nodo.liga

                if nodo is None:
                    raise IndexError("Valor por fuera de los límites de la lista.")
                j += 1
            return nodo.dato
