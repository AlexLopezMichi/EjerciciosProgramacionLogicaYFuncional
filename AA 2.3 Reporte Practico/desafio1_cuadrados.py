'''
A partir del código base modifica la función cuadradosLista utilizando cualquier
combinación de map(), filter(), ó reduce().

La función debería devolver un nuevo arreglo que contenga los cuadrados unicamente de 
los enteros positivos (los números decimales no son enteros) cuando se le pase un 
arreglo de números reales.
Un ejemplo de un arreglo de números reales es [-3, 4.8, 5, 3, -3.2].

Nota: La función no debe usar ningún tipo de bucles for o while ni la función forEach().
'''

def cuadradosLista(arreglo):

    cuadrados = map(lambda x: x**2, filter(lambda x: x > 0 and isinstance(x, int), arreglo))
    return list(cuadrados)

cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)
