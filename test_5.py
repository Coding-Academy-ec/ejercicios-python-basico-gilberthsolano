import math
from programa import suma, area_circulo

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 5) == 4

def test_area_circulo():
    assert abs(area_circulo(1) - math.pi) < 1e-9  # Área de un círculo con radio 1 debería ser π
    assert abs(area_circulo(2.5) - (math.pi * 2.5 ** 2)) < 1e-9  # Área con radio 2.5
