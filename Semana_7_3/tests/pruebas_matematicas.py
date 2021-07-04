from ..matematicas import *
import math


#Flujo de trabajo usual:

## Se elaboran pruebas por cada función nueva que se añada.
## Cada vez que se cambie una función existente, se ejecutan las pruebas.



def test_suma():
    assert suma(1, 2) == 3

def test_potencia():
    assert potencia(10, 0) == 1
    assert potencia(2, 3) == 8

def test_resta():
    assert resta(-3, 2) == -5

def test_multiplicacion():
    assert multiplicacion(-2, -2) == 4

def test_division():
    assert math.isclose(division(3, 2), 1.5, abs_tol=1e-8)

def test_ordenar():
    listas = [
        [0,1,0,-1,2],
        [1],
        [0,1,2,3]
    ]

    listas_ordenadas = [
        [-1,0,0,1,2],
        [1],
        [0,1,2,3]
                        ]
    for i in range(len(listas)):
        assert ordenar_lista(listas[i]) == listas_ordenadas[i]

