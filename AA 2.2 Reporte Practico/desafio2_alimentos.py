def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def calcular_bonus(num_porciones):
        if num_porciones > 2:
            return "Coca Gratis"
        else:
            return ""

def ordenar_alimento(preparar_comida, num_porciones):
    porciones_alimento = [preparar_comida() for _ in range(num_porciones)]
    return porciones_alimento + [calcular_bonus(num_porciones)]

pizza_para_grupo = ordenar_alimento(preparar_pizza, int(input("¿Cuantas pizzas quieren?: ")))
hamburguesa_para_grupo = ordenar_alimento(preparar_hamburguesa, int(input("¿Cuantas hamburguesas quieren?: ")))
hotdog_para_grupo = ordenar_alimento(preparar_hotdog, int(input("¿Cuantos hotdogs quieren?: ")))

print(pizza_para_grupo)
print(hamburguesa_para_grupo)
print(hotdog_para_grupo)
