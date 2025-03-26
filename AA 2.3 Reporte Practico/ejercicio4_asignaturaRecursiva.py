asignaturas_viii = ["Programacion Logica"]

def agregar_asignatura(lista):
    asignatura = input('Ingresa una asignatura o exit para salir: ')
    if asignatura == 'exit':
        return lista
    return agregar_asignatura(lista + [asignatura])
    
print(agregar_asignatura(asignaturas_viii)) #Recursion
    