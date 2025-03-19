def preparar_cafeA():
    return "Café Americano"

def preparar_cafeO():
    return "Café Olla"

def ordenar_cafe(preparar_cafe, num_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe

cafe_para_grupoA = ordenar_cafe(preparar_cafeA, 3)
cafe_para_grupoB = ordenar_cafe(preparar_cafeO, 5)

print(cafe_para_grupoA)
print(cafe_para_grupoB)