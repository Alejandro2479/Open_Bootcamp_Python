paises = input("Introduce una lista de países separados por comas: ")
lista_paises = set(paises.split(","))

print("Lista de países: ", ", ".join(sorted(lista_paises)))
