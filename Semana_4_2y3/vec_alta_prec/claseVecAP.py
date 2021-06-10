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
        for i in range(1, self.n + 1):
            self.V[i] = None
        self.V[0] = self.n

    def asignaValor(self, valor):
        valor_cadena = str(valor)
        if len(valor_cadena) > self.n:
            print("Valor muy grande para asignar")
        else:
            self.reiniciar()
            i = -1
            while i >= -len(valor_cadena):
                self.asignaDato(int(valor_cadena[i]), i)
                i = i - 1
            self.V[0] = self.n - len(valor_cadena)

    # vec1, vec2
    # vec1+vec2

    def sumaYacarreo(self, a, b=0):
        global acarreo
        s = a + b + acarreo
        if s > 9:
            acarreo = s // 10
            s = s - 10
        else:
            acarreo = 0
        return s

    def retornaDato(self, i):
        if i > self.n:
            print("Indice fuera del rango de valores llenos del vector")
        else:
            return self.V[i]

    def __add__(self, b):
        global acarreo
        i = self.tamagno()
        j = b.tamagno()
        k = max(i, j) + 2  # tamaño del vector resultado
        resultado = altaPrecision(k)
        acarreo = 0
        while i > self.V[0] and j > b.V[0]:
            r = self.sumaYacarreo(self.retornaDato(i), b.retornaDato(j))
            resultado.asignaDato(r, k)
            i = i - 1
            j = j - 1
            k = k - 1
            #resultado.imprimeVector()
            print("-----------")
        while i > self.V[0]:
            r = self.sumaYacarreo(self.retornaDato(i), 0)
            resultado.asignaDato(r, k)
            i = i - 1
            k = k - 1
        while j > b.V[0]:
            r = self.sumaYacarreo(b.retornaDato(j))
            resultado.asignaDato(r, k)
            j = j - 1
            k = k - 1
        if acarreo > 0:
            resultado.asignaDato(acarreo, k)
            k = k - 1
        resultado.V[0] = k
        return resultado
