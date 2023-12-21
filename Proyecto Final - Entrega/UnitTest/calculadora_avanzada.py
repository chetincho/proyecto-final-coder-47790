# Definicion: Dado dos numeros y un operador definir las pruebas unitarias
# para las operaciones de suma, resta, multiplicación y división.


def calculadora_avanzada(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        if num2 == 0:
            return "Error: Div por cero"
        else:
            return num1 / num2


# -- Prueba de Suma
resultado = calculadora_avanzada(-1, 3, "+")
if resultado == 2:
    print("Prueba de Suma exitosa")
else:
    print("Prueba de Suma fallida")


# -- Prueba de Resta
resultado = calculadora_avanzada(5, 3, "-")
if resultado == 2:
    print("Prueba de Resta exitosa")
else:
    print("Prueba de Resta fallida")


# -- Prueba de Multiplicacion
resultado = calculadora_avanzada(3, 4, "*")
if resultado == 12:
    print("Prueba de Multiplicación exitosa")
else:
    print("Prueba de Multiplicación fallida")


# -- Prueba de División
resultado = calculadora_avanzada(8, 4, "/")
if resultado == 2:
    print("Prueba de División exitosa")
else:
    print("Prueba de División fallida")


resultado = calculadora_avanzada(8, 0, "/")
if resultado == "Error: Div por cero":
    print("Prueba de División con Divisor cero exitosa")
else:
    print("Prueba de División con Divisor cero fallida")


resultado = calculadora_avanzada(0, 5, "/")
if resultado == 0:
    print("Prueba de División con Dividendo cero exitosa")
else:
    print("Prueba de División con Dividendo cero fallida")