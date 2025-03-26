asignaturas_viii = ["Programacion Logica"]
nuevalista = [asignaturas_viii, "Programacion Web"]

print(asignaturas_viii)
print(nuevalista)

def agregar_asignatura(lista, asignatura):
    return lista + [asignatura]

print(agregar_asignatura(asignaturas_viii,input('Ingresa una asignatura: ')))