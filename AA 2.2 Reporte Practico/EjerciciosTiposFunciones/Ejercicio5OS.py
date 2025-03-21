## 3. Funciones de Orden Superior

# Ejercicio 1: Aplicar una función a una lista de números
def aplicar_funcion(lista, funcion):
    resultado = []
    for x in lista:
        resultado.append(funcion(x))
    return resultado

def cuadrado(x):
    return x ** 2

print(aplicar_funcion([1, 2, 3, 4], cuadrado))

