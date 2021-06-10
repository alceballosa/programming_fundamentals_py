from claseVector import vector


class altaPrecision(vector):
    def __init__(self, n):
        vector.__init__(self, n)
        self.V[0] = n

    def imprimeVector(self, mensaje="vector sin nombre:"):
        print("\n", mensaje)
        for i in range(self.V[0] + 1, self.n + 1):
            print(self.V[i], end="")
        print()

    def reiniciar(self):
        for i in range(1, self.n+1):
            self.V[i] = None
        self.V[0] = self.n

    def asignaValor(self, valor):
        valor_cadena = str(valor)
        if len(valor_cadena) > self.n:
            print("Valor muy grande para asignar")
        else:
            self.reiniciar()
            #indexar una cadena por [::-1] la invierte
            i = -1
            while i >= -len(valor_cadena):
                self.asignaDato(int(valor_cadena[i]), i)
                i = i-1
            self.V[0] = self.n - len(valor_cadena)
