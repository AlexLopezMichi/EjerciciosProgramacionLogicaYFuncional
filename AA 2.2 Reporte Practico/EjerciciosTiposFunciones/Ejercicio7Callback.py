## 4. Funciones Callback

# Ejercicio 1: Usar callbacks para procesar datos
def procesar_datos(datos, callback):
    return [callback(d) for d in datos]

def convertir_a_mayusculas(texto):
    return texto.upper()

datos = ["python", "java", "c++"]
print(procesar_datos(datos, convertir_a_mayusculas))