class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"
        
vehiculo = Vehiculo("Ford", "Mustang")

# Guardar el objeto en un archivo txt
with open("vehiculo.txt", "w") as file:
    file.write(f"{vehiculo.marca},{vehiculo.modelo}")

# Cargar el objeto desde el archivo txt
with open("vehiculo.txt", "r") as file:
    data = file.read()
    marca, modelo = data.split(",")
    vehiculo_cargado = Vehiculo(marca, modelo)

print(vehiculo_cargado)
