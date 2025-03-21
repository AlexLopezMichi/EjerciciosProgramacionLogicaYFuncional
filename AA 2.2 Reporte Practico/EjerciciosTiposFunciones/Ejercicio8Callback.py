## 4. Funciones Callback

# Ejercicio 2: Simular una operación asincrónica con callback
def operacion_asincrona(resultado, callback):
    print("Procesando operación...")
    callback(resultado)

def mostrar_resultado(resultado):
    print("Resultado obtenido:", resultado)

operacion_asincrona(42, mostrar_resultado)