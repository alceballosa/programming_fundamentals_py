from claseVecAP import altaPrecision

vap1 = altaPrecision(n=50)
vap1.asignaValor("2000")
vap1.imprimeVector()

vap2 = altaPrecision(n=50)
vap2.asignaValor("100")
vap2.imprimeVector()

# vap3 = vap1 + vap2
# vap3.imprimeVector()

# Probando la multiplicación

vap3 = 0*vap2

vap2.asignaValor(10)
vap2.imprimeVector()
vap3.imprimeVector()
