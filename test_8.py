from programa import celsius_a_fahrenheit, fahrenheit_a_celsius

def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212
    assert celsius_a_fahrenheit(-40) == -40  # Caso especial donde Celsius y Fahrenheit coinciden

def test_fahrenheit_a_celsius():
    assert fahrenheit_a_celsius(32) == 0
    assert fahrenheit_a_celsius(212) == 100
    assert fahrenheit_a_celsius(-40) == -40  # Caso especial donde Celsius y Fahrenheit coinciden
