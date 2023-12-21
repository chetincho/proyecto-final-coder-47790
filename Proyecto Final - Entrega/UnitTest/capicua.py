# Definicion: Dado un texto determinar si el mismo es capicua.


def invertir_texto(texto):
    
    texto_invertido = ""
    for caracter in texto:
        texto_invertido = caracter + texto_invertido
    
    return texto_invertido




# Prueba con "RECONOCER"
texto_original = "reconocer"
texto_invertido = invertir_texto(texto_original)

if texto_original == texto_invertido:
    print(f"El texto {texto_original} es capicua")
    print(texto_original)
    print(texto_invertido)
else:
    print(f"El texto {texto_original} no es capicua")
    print(texto_original)
    print(texto_invertido)


# Prueba con saippuakivikauppias - Una palabra finlandesa que significa "vendedor de piedras de jabón".
texto_original = "saippuakivikauppias"
texto_invertido = invertir_texto(texto_original)

if texto_original == texto_invertido:
    print(f"El texto {texto_original} es capicua")
    print(texto_original)
    print(texto_invertido)
else:
    print(f"El texto {texto_original} no es capicua")
    print(texto_original)
    print(texto_invertido)


# Prueba con numeros
texto_original = "181818181818181"
texto_invertido = invertir_texto(texto_original)

if texto_original == texto_invertido:
    print(f"El texto {texto_original} es capicua")
    print(texto_original)
    print(texto_invertido)
else:
    print(f"El texto {texto_original} no es capicua")
    print(texto_original)
    print(texto_invertido)


# Prueba fallido con pepe
texto_original = "pepe"
texto_invertido = invertir_texto(texto_original)

if texto_original == texto_invertido:
    print(f"El texto {texto_original} es capicua")
    print(texto_original)
    print(texto_invertido)
else:
    print(f"El texto {texto_original} no es capicua")
    print(texto_original)
    print(texto_invertido)