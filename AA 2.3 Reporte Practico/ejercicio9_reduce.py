from functools import reduce

#Lista de jugadores
jugadores =[
    {"nombre":"Chloe", "edad": 22},
    {"nombre":"Chiwis", "edad": 23},
    {"nombre":"Mango", "edad": 24},
    {"nombre":"Vini", "edad": 25}
]

#Usar reduce para obtener la suma de las edades de los jugadores
suma_edades = reduce(lambda acumulador, jugador: acumulador + jugador["edad"], jugadores, 0)
print(suma_edades)