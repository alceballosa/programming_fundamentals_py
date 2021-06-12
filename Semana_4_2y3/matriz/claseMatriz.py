import random

from claseVector import vector


class matriz:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mat = [] * (m + 1)
        for i in range(m + 1):
            a = [0] * (n + 1)
            self.mat.append(a)

    def llenarMatrizAleatoriamente(self, rango):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.mat[i][j] = random.randint(1, rango)

    def numeroFilas(self):
        return self.m

    def numeroColumnas(self):
        return self.n

    def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre: "):
        print("\n", mensaje)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                print(self.mat[i][j], end="\t")
            print()

    def imprimeMatrizPorColumnas(self, mensaje="Matriz sin nombre: "):
        print("\n", mensaje)
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                print(self.mat[j][i], end="\t")
            print()

    def intercambiarFilas(self, i, j):
        for k in range(1, self.n + 1):
            aux = self.mat[i][k]
            self.mat[i][k] = self.mat[j][k]
            self.mat[j][k] = aux

    def intercambiarColumnas(self, i, j):
        for k in range(1, self.m + 1):
            aux = self.mat[k][i]
            self.mat[k][i] = self.mat[k][j]
            self.mat[k][j] = aux

    def sumarFilas(self):
        v = vector(self.m)
        for i in range(1, self.m + 1):
            s = 0
            for j in range(1, self.n + 1):
                s = s + self.mat[i][j]
            v.agregarDato(s)
        return v

    def sumarColumnas(self):
        v = vector(self.n)
        for i in range(1, self.n + 1):
            s = 0
            for j in range(1, self.m + 1):
                s = s + self.mat[j][i]
            v.agregarDato(s)
        return v

    def traspuesta(self):
        c = matriz(self.n, self.m)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                c.mat[j][i] = self.mat[i][j]
        return c

    def __add__(self, other):

        if self.n != other.n or self.m != other.m:
            print("Los tamaños de las matrices deben ser iguales")
            return None
        else:
            c = matriz(self.n, self.m)
            for i in range(1, self.n + 1):
                for j in range(1, self.m + 1):
                    c.mat[i][j] = self.mat[i][j] + other.mat[i][j]
            return c

    def __mul__(self, b):
        c = matriz(self.m, self.n)
        if type(b) == int:
            for i in range(1, self.m + 1):
                for j in range(1, self.n + 1):
                    c.mat[i][j] = self.mat[i][j] * b
            return c

        if self.n != b.m:
            print("Matrices no se pueden multiplicar. ", end="")
            print("El número de columnas de self es diferente", end="")
            print("del número de columnas de b")
            return None
        c = matriz(self.m, b.n)
        for i in range(1, self.m + 1):
            for j in range(1, b.n + 1):
                c.mat[i][j] = 0
                for k in range(1, self.n + 1):
                    c.mat[i][j] = c.mat[i][j] + self.mat[i][k] * b.mat[k][j]
        return c

    def __rmul__(self, b):
        return self * b
