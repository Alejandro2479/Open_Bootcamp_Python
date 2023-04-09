import pickle

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

# Crear un objeto de la clase Vehiculo
coche = Vehiculo('rojo', 4, 2)

# Guardar el objeto en un archivo usando pickle
with open('coche.pkl', 'wb') as archivo:
    pickle.dump(coche, archivo)

# Cargar el objeto desde el archivo usando pickle
with open('coche.pkl', 'rb') as archivo:
    coche_cargado = pickle.load(archivo)

# Imprimir los atributos del objeto cargado
print('Color:', coche_cargado.color)
print('Ruedas:', coche_cargado.ruedas)
print('Puertas:', coche_cargado.puertas)
