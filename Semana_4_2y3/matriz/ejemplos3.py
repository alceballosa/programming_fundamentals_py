from claseMatriz import matriz

m1 = matriz(4, 4)
m2 = matriz(4, 4)

m1.llenarMatrizAleatoriamente(10)
m2.llenarMatrizAleatoriamente(10)

m1.imprimeMatrizPorFilas()
m2.imprimeMatrizPorFilas()

m3 = m1 + m2
m3.imprimeMatrizPorFilas()

print(m3)
