## 5. Funciones Lambda

# Ejercicio 2: Filtrar números pares de una lista con lambda
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)
