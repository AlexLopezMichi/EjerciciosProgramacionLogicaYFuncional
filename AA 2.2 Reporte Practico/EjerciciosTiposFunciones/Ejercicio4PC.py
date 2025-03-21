## 2. Funciones de Primera Clase

# Ejercicio 2: Pasar funciones como argumentos
def ejecutar_operacion(funcion, x, y):
    return funcion(x, y)
# Las funciones sumar y restar son ejemplos de funciones de 
# primera clase, ya que se usan como objetos y se pasan como 
# argumentos a otra función.
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

print("Suma:", ejecutar_operacion(sumar, 3, 7))
print("Resta:", ejecutar_operacion(restar, 8, 7))