from claseMatriz import matriz

m = matriz(2, 10)

m.imprimeMatrizPorFilas()

m.imprimeMatrizPorColumnas()

m.llenarMatrizAleatoriamente(100)

m.imprimeMatrizPorFilas()

m.intercambiarFilas(1, 2)

m.imprimeMatrizPorFilas()

m.intercambiarColumnas(2, 3)

m.imprimeMatrizPorFilas()


vsum = m.sumarFilas()
vsum.imprimeVector()

vsum2 = m.sumarColumnas()
vsum2.imprimeVector()


vtr = m.traspuesta()
vtr.imprimeMatrizPorFilas()

vtr = vtr.traspuesta()
vtr.imprimeMatrizPorFilas()
