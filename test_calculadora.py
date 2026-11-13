from calculadora import sumar

def test_sumar():
    assert sumar(2, 4) == 6
    assert sumar(-1, 1) == 0
