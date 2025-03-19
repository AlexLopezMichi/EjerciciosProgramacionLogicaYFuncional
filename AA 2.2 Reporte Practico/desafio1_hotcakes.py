def preparar_hotcake():
    return "🥞"

def ordenar_hotcakes(numero_piezas):
    piezas_hotcakes = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezas_hotcakes

hotcakes_familia = ordenar_hotcakes(int(input("Ingresa el número de integrantes en tu familia: ")))

print(hotcakes_familia)