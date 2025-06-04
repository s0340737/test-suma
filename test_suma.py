# archivo: test_ejemplo.py

def sumar(a, b):
    return a + b

def test_sumar_correcto():
    assert sumar(2, 3) == 5

def test_sumar_falla():
    assert sumar(2, 2) == 5  # Esto fallará
