# Sombrero Seleccionador ISC 🎓

# Inicialización de puntuaciones para cada rama
redes = 0
bases_datos = 0
desarrollo_software = 0
hardware = 0
modelado_3d = 0
gestion_proyectos = 0

print('===============================')
print('🔍 Sombrero Seleccionador ISC 🎓')
print('===============================')

# Pregunta 1
print('\nP1) ¿Qué tipo de actividad disfrutas más?')
print('  1) Configurar y optimizar redes de computadoras')
print('  2) Diseñar esquemas de bases de datos eficientes')
print('  3) Desarrollar aplicaciones y software')
print('  4) Programar microcontroladores y hardware')
print('  5) Crear modelos y animaciones 3D')
print('  6) Gestionar equipos de trabajo en proyectos de software')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2
else:
    print('Respuesta incorrecta.')

# Pregunta 2
print('\nP2) ¿En qué entorno te sientes más cómodo trabajando?')
print('  1) En una sala de servidores o configurando redes')
print('  2) Analizando datos y optimizando bases de datos')
print('  3) Programando en un entorno de desarrollo')
print('  4) Trabajando con placas electrónicas y sensores')
print('  5) Diseñando modelos en software de animación 3D')
print('  6) Coordinando equipos de trabajo y gestionando proyectos')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2
else:
    print('Respuesta incorrecta.')

# Pregunta 3
print('\nP3) ¿Qué te motiva más en un proyecto?')
print('  1) Resolver problemas de conectividad')
print('  2) Administrar grandes volúmenes de datos')
print('  3) Desarrollar aplicaciones innovadoras')
print('  4) Mejorar el rendimiento de hardware y software embebido')
print('  5) Crear contenido visualmente impresionante')
print('  6) Organizar equipos y asegurar el cumplimiento de objetivos')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2
else:
    print('Respuesta incorrecta.')

# Pregunta 4
print('\nP4) ¿Qué herramienta prefieres utilizar en tu trabajo?')
print('  1) Router y switches')
print('  2) SQL y bases de datos')
print('  3) Entornos de desarrollo como VS Code o IntelliJ')
print('  4) Microcontroladores como Arduino o Raspberry Pi')
print('  5) Software de modelado como Blender o Maya')
print('  6) Herramientas de gestión como Jira o Trello')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2
else:
    print('Respuesta incorrecta.')

# Pregunta 5
print('\nP5) ¿Cuál de estos problemas te gustaría resolver?')
print('  1) Mejorar la seguridad y conectividad en redes')
print('  2) Organizar grandes volúmenes de información')
print('  3) Crear aplicaciones para resolver necesidades específicas')
print('  4) Optimizar el rendimiento de dispositivos electrónicos')
print('  5) Diseñar entornos y personajes digitales')
print('  6) Coordinar equipos para lograr entregas exitosas')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2
else:
    print('Respuesta incorrecta.')

# Determinar la rama con mayor puntaje
puntajes = {
    'Redes': redes,
    'Bases de Datos': bases_datos,
    'Desarrollo de Software': desarrollo_software,
    'Programación Hardware': hardware,
    'Modelado 3D': modelado_3d,
    'Gestión de Proyectos de Software': gestion_proyectos
}

rama_recomendada = max(puntajes, key=puntajes.get)

# Mostrar resultados
print('\nResultados:')
for rama, puntos in puntajes.items():
    print(f'{rama}: {puntos} puntos')

print(f'🎓 ¡Tu mejor opción es: {rama_recomendada}! 🎓')