## 3. Funciones de Orden Superior

# Ejercicio 2: Retornar una función según el tipo de operación
def obtener_operacion(operacion):
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    if operacion == 'suma':
        return sumar
    elif operacion == 'resta':
        return restar

op = obtener_operacion('suma')
print("Resultado de la suma:", op(5, 3))