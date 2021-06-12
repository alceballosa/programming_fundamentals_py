from claseMatriz import matriz

m1 = matriz(3, 3)

m1.llenarMatrizAleatoriamente(6)
m1.imprimeMatrizPorFilas()
print()
print("Suma de la diagonal: ", m1.sumaDiagonal())
print("Suma de la diagonal secundaria: ", m1.sumaDiagonalSecundaria())

print("Suma de la triangular superior: ", m1.sumaTriangularSuperior())
print(
    "Suma de la triangular estrictamente superior: ",
    m1.sumaTriangularEstrictamenteSuperior(),
)

print("Suma de la triangular inferior: ", m1.sumaTriangularInferior())
print(
    "Suma de la triangular estrictamente inferior: ",
    m1.sumaTriangularEstrictamenteInferior(),
)
