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
