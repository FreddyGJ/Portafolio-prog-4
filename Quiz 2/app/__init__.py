def letras():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    yield "E"
    yield "F"
    yield "G"
    yield "H"
    yield "I"
    yield "J"
    yield "K"
    yield "L"
    yield "M"

def numeros_impares():
    num = 1
    while True:
        yield num
        num = num + 2

if __name__ == "__main__":
    numeros = numeros_impares()
    for n in numeros:
        if n > 99:
            break
        else:
            print(n)

    letras = letras()
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))
    print(next(letras))