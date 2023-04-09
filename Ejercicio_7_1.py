def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b
  
# Ejemplo del import del modulo si estuviera en otro archivo:
import calculadora

a = 10
b = 5

resultado_suma = calculadora.sumar(a, b)
resultado_resta = calculadora.restar(a, b)
resultado_multiplicacion = calculadora.multiplicar(a, b)
resultado_division = calculadora.dividir(a, b)

print(f"La suma de {a} y {b} es {resultado_suma}")
print(f"La resta de {a} y {b} es {resultado_resta}")
print(f"La multiplicación de {a} y {b} es {resultado_multiplicacion}")
print(f"La división de {a} y {b} es {resultado_division}")
