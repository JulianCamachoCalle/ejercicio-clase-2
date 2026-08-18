"""Calculadora muy basica de ejemplo."""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", sumar(2, 3))
    print("5 - 1 =", restar(5, 1))
    print("4 * 3 =", multiplicar(4, 3))
    print("10 / 2 =", dividir(10, 2))
