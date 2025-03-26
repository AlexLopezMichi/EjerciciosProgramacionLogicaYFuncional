#Lista de jugadores
jugadores =[
    {"nombre":"Chloe", "edad": 22},
    {"nombre":"Chiwis", "edad": 23},
    {"nombre":"Mango", "edad": 24},
    {"nombre":"Vini", "edad": 25}
]


#Usar filter para obtener los jugadores mayores de 23 años
jugadores_mayores = list(filter(lambda jugador: jugador["edad"] > 23, jugadores))

print(jugadores_mayores)