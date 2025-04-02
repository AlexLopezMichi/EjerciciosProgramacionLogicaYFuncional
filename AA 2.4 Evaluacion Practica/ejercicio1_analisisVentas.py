from functools import reduce

ventasSemana = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

#Calcular el promedio de las ventas
promedioVentas = reduce(lambda promedio, ventas: promedio + ventas, ventasSemana, 0) / len(ventasSemana)

#Convertir las ventas de pesos mexicanos a dolares
ventasDolares = list(map(lambda ventas: round(ventas / 20.45, 2), ventasSemana))

#Filtrar las ventas mayores a 150 dolares
ventasMayores = list(filter(lambda ventas: ventas > 150, ventasDolares))

#Suma total de las ventas mayores a 150 dolares
sumaVentas = reduce(lambda sumaVentas, ventasM: sumaVentas + ventasM, ventasMayores, 0)

print("Lista Original: ", ventasSemana)
print("a) El promedio de ventas en pesos mexicanos es: ", promedioVentas)
print("b) Las ventas de la semana en dolares son: ", ", ".join(map(str, ventasDolares)))
print("c) Las ventas mayores a 150 dolares son: ", ", ".join(map(str, ventasMayores)))
print("d) La suma de las ventas mayores a 150 dolares es: ", sumaVentas)