#Lista de jugadores
jugadores =[
    {"nombre":"Chloe", "edad": 22},
    {"nombre":"Chiwis", "edad": 23},
    {"nombre":"Mango", "edad": 24},
    {"nombre":"Vini", "edad": 25}
]


#Usar map para extraer los nombres de los jugadores

nombre_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))
print(nombre_jugadores)