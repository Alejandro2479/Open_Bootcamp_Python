class Vehículo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
class Coche(Vehículo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
mi_coche = Coche('Rojo', 4, 5, 200, 2000)

print(f"Mi coche es de color {mi_coche.color}, tiene {mi_coche.ruedas} ruedas y {mi_coche.puertas} puertas.")
print(f"Alcanza una velocidad máxima de {mi_coche.velocidad} km/h y tiene una cilindrada de {mi_coche.cilindrada} cc.")
