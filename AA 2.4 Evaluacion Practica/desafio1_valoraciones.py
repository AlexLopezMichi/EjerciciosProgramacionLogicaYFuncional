from functools import reduce

# Aspectos comunes a evaluar y asignaturas
aspectos = ["Temas impartidos", "Practicas realizadas", "Herramientas utilizadas", "Complejidad de la asignatura"]
asignaturas = ["Matemáticas", "Física", "Programación"]

def ingresar_valoraciones(aspectos):
    """
    Solicita al usuario ingresar valoraciones para cada aspecto dado en la lista.

    Args:
        aspectos (list): Lista de aspectos a calificar.

    Returns:
        list: Valoracion ingresadas por el usuario.
    """
    return list(map(lambda aspecto: int(input(f"Valoración para {aspecto} (1-10): ")), aspectos))

def recolectar_respuestasAsignatura(n, aspectos):
    """
    Recolecta las valoraciones de 'n' alumnos para una asignatura específica.

    Args:
        n (int): Número de alumnos.
        aspectos (list): Lista de aspectos a calificar.

    Returns:
        list: Lista de listas con las calificaciones de cada alumno.
    """
    return list(map(lambda alumno: (print(f"\n=== Alumno {alumno + 1} ===") or ingresar_valoraciones(aspectos)), range(n)))

def recolectarRespuestas(asignaturas, num_alumnos):
    """
    Recolecta respuestas para todas las asignaturas.

    Args:
        asignaturas (list): Lista de nombres de asignaturas.
        num_alumnos (int): Número total de alumnos.

    Returns:
        list: Lista de respuestas por asignatura.
    """
    return list(map(lambda asignatura: (print(f"\n--- {asignatura} ---") or recolectar_respuestasAsignatura(num_alumnos, aspectos)), asignaturas))

def calcular_promedios(respuestas):
    """
    Calcula el promedio por aspecto para una asignatura.

    Args:
        respuestas (list): Lista de listas con las valoraciones por alumno.

    Returns:
        list: Promedios de cada aspecto.
    """
    transpuesta = list(zip(*respuestas))
    return list(map(lambda aspecto: round(reduce(lambda x, y: x + y, aspecto) / len(aspecto), 2), transpuesta))

def sumar_puntosAlumno(respuestas):
    """
    Calcula la suma total de puntos por alumno.

    Args:
        respuestas (list): Lista de listas con las valoraciones por alumno.

    Returns:
        list: Puntos totales por alumno.
    """
    return list(map(lambda cal: reduce(lambda x, y: x + y, cal), respuestas))

def calcular_sumaPuntosAlumnos(respuestas):
    """
    Calcula la suma total de puntos de todos los alumnos.

    Args:
        respuestas (list): Lista de listas con las valoraciones por alumno.

    Returns:
        int: Suma total de puntos.
    """
    return reduce(lambda valoraciones, alumno: valoraciones + sum(alumno), respuestas, 0)

def calcular_promedioGeneral(puntos, respuestas):
    """
    Calcula el promedio general de una asignatura.

    Args:
        puntos (int): Suma total de puntos de los aspectos por asignatura.
        respuestas (list): Lista de listas con las valoraciones por alumno.

    Returns:
        float: Promedio general de la asignatura.
    """
    cantidad_valoraciones = reduce(lambda valoraciones, alumno: valoraciones + len(alumno), respuestas, 0) 
    return round(puntos / cantidad_valoraciones, 2) if cantidad_valoraciones > 0 else 0.0

def calcular_promedioTotalPuntos(puntosTotales, numAlumnos):
    """
    Calcula el promedio de puntos obtenidos por los alumnos.

    Args:
        puntosTotales (int): Suma total de puntos de todos los alumnos.
        numAlumnos (int): Número total de alumnos.

    Returns:
        float: Promedio de puntos por los alumnos.
    """
    return round(puntosTotales / numAlumnos, 2) if numAlumnos > 0 else 0.0

def resumen_valoraciones(respuestas, umbral=6):
    """
    Genera un resumen con la cantidad total de valoraciones, 
    cuántas están por debajo del umbral, y el porcentaje que representan.

    Args:
        respuestas (list): Lista de listas con las valoraciones de cada alumno.
        umbral (int): Valor mínimo aceptable (por defecto 6).

    Returns:
        dict: Diccionario con total, bajas y porcentaje.
    """
    total_valoraciones = reduce(lambda acc, alumno: acc + len(alumno), respuestas, 0)
    valoraciones_bajas = reduce(lambda acc, alumno: acc + len(list(filter(lambda x: x < umbral, alumno))), respuestas, 0)
    
    porcentaje_bajas = round((valoraciones_bajas / total_valoraciones) * 100, 2) if total_valoraciones > 0 else 0.0
    
    return {
        "total": total_valoraciones,
        "bajas": valoraciones_bajas,
        "porcentaje_bajas": porcentaje_bajas
    }

def mostrar_resultados(asignatura, promedios, totales, puntos, respuestas, numAlumnos):
    """
    Muestra los resultados de la evaluación para una asignatura específica.

    Args:
        asignatura (str): Nombre de la asignatura.
        promedios (list): Promedios por aspecto.
        totales (list): Puntos totales por alumno.
        puntos (int): Suma total de puntos.
        respuestas (list): Valoraciones por alumno.
        numAlumnos (int): Número total de alumnos.
    """
    promedio_general = calcular_promedioGeneral(puntos, respuestas)
    promedio_total = calcular_promedioTotalPuntos(puntos, numAlumnos)
    resumen = resumen_valoraciones(respuestas)

    print(f"\n--- Resultados para {asignatura} ---")
    print("\n".join(map(lambda x: f"{x[0]}: {x[1]}", zip(aspectos, promedios))))
    print(f"\nPromedio general de la asignatura: {promedio_general}")
    print("\n" + "\n".join(map(lambda t: f"Alumno {t[0]+1}: {t[1]} puntos", enumerate(totales))))
    print(f"Suma total de puntos: {puntos}")
    print(f"Promedio de puntos de alumnos: {promedio_total}")
    print(f"\nValoraciones totales: {resumen['total']}")
    print(f"Valoraciones menores a 6: {resumen['bajas']} ({resumen['porcentaje_bajas']}%)")

def main():
    """
    Función principal que ejecuta la encuesta de evaluación de asignaturas.
    """
    print("Encuesta de Evaluación de Asignaturas")
    num = int(input("¿Cuántos alumnos participarán? "))

    respuestas_por_asignatura = recolectarRespuestas(asignaturas, num)

    list(map(
        lambda datos: mostrar_resultados(
            datos[0],
            calcular_promedios(datos[1]),
            sumar_puntosAlumno(datos[1]),
            calcular_sumaPuntosAlumnos(datos[1]),
            datos[1],
            num
        ),
        zip(asignaturas, respuestas_por_asignatura)
    ))

main()