class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}\nNota: {self.nota}")
        
    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}")
