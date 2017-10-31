def generar_impares():
    impar = 1
    while True:
        yield impar
        impar = impar + 2

def generar_letras():
    letra = 97
    while True:
        yield chr(letra)
        letra = letra + 1


if __name__ == "__main__":
    impar = generar_impares()
    for n in impar:
        print(n)
        if n > 99:
         break

    letra = generar_letras()
    for n in letra:
        print(n)
        if n > 'm':
            break









