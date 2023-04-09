# Abrir archivo en modo escritura y escribir en él
archivo = open("ejemplo.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

# Abrir archivo en modo lectura y mostrar su contenido
archivo = open("ejemplo.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
