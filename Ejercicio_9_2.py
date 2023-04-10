from functools import reduce

def suma_impares(lista):
    impares = list(filter(lambda x: x % 2 != 0, lista))
    return reduce(lambda x, y: x + y, impares)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La suma de los números impares es:", suma_impares(lista))
