# Estado de sensores (simulados como constantes)
humedad_suelo = 'baja'
temperatura = 35
hora = 20
pronostico_lluvia = False

# ¿Es una hora adecuada para regar?
def hora_adecuada(h):
    return h < 10 or h > 18

# ¿Cuándo se debe activar el sistema de riego?
def activar_riego(humedad, lluvia, hora_actual):
    return humedad == 'baja' and not lluvia and hora_adecuada(hora_actual)

# Diagnóstico del sistema
def estado_riego():
    if activar_riego(humedad_suelo, pronostico_lluvia, hora):
        return 'Activado'
    else:
        return 'No activado'

# Alerta por calor extremo
def alerta_calor(temp):
    return temp >= 32

# Recomendación del sistema
def recomendacion():
    if activar_riego(humedad_suelo, pronostico_lluvia, hora) and alerta_calor(temperatura):
        print('Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.')
    else:
        print('Sin recomendaciones especiales para el riego.')

# Ejecución de funciones o "consultas"
if __name__ == '__main__':
    print("Estado del riego:", estado_riego())
    recomendacion()
    print("Hora adecuada:",hora_adecuada(hora))
    print("Alerta por calor:", alerta_calor(temperatura))
    print("Pronostico lluvia:", pronostico_lluvia)