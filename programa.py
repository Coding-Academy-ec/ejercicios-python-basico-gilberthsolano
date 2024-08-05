def imprimir_nombre():
    # Aquí se imprime el nombre en la pantalla
    print("Gilbert Solano")

if __name__ == "__main__":
    # Se llama a la función imprimir_nombre() para ejecutarla
    imprimir_nombre()


# 2 Escribe un programa que calcule la suma de los números del 1 al 10.
def suma_1_al_10():
    suma = sum(range(1, 11))  # Se utiliza la función sum() para calcular la suma del rango del 1 al 10
    return suma  # Se devuelve el resultado de la suma

if __name__ == "__main__":
    resultado = suma_1_al_10()  # Se llama a la función suma_1_al_10() para obtener el resultado
    print(resultado)  # Se imprime el resultado de la suma


# 3 Crea variables para almacenar tu edad, nombre y estatura, e imprímelas en pantalla.
def imprimir_datos_personales(nombre, edad, estatura):
    print(f"Nombre: {nombre}\nEdad: {edad}\nEstatura: {estatura}")  # Se imprimen en pantalla los datos personales recibidos como argumentos

if __name__ == "__main__":
    # Se definen las variables con los datos personales
    nombre = "Gilbert Solano"
    edad = 30
    estatura = 1.75
    # Se llama a la función imprimir_datos_personales() para mostrar los datos
    imprimir_datos_personales(nombre, edad, estatura)



# 4 Escribe un programa que determine si un número ingresado por el usuario es par o impar.
def par_o_impar(numero):
    if numero % 2 == 0:  # Se verifica si el número es divisible por 2
        return "par"  # Si es divisible, se devuelve "par"
    else:
        return "impar"  # Si no es divisible, se devuelve "impar"

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))  # Se solicita al usuario que ingrese un número
    print(par_o_impar(num))  # Se imprime si el número ingresado es par o impar



# 5 Crea una función que calcule el área de un círculo dado su radio.
import math
def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area  # Se devuelve el área calculada

# Define la función suma si también la estás probando.
def suma(a, b):
    return a + b

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    print(f"El área del círculo es: {area_circulo(radio)}")  # Se imprime el área calculada del círculo

     

# 6 Define una función que reciba dos números como argumentos y devuelva su suma.
def suma(a, b):
    return a + b  # Se devuelve la suma de los dos números recibidos como argumentos

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))  # Se solicita al usuario que ingrese el primer número
    num2 = int(input("Ingrese el segundo número: "))  # Se solicita al usuario que ingrese el segundo número
    print("La suma es:", suma(num1, num2))  # Se imprime la suma de los dos números ingresados




import math

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area  # Se devuelve el área calculada

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    print("El área del círculo es:", area_circulo(radio))  # Se imprime el área calculada del círculo


import math

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Fórmula de conversión de Celsius a Fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # Fórmula de conversión de Fahrenheit a Celsius

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))  # Solicita al usuario la temperatura en grados Celsius
    print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))  # Imprime la temperatura convertida a grados Fahrenheit

    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))  # Solicita al usuario la temperatura en grados Fahrenheit
    print("Temperatura en Celsius:", fahrenheit_a_celsius(fahrenheit))  # Imprime la temperatura convertida a grados Celsius


