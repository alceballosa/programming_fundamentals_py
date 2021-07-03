from matematicas import *
import math

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