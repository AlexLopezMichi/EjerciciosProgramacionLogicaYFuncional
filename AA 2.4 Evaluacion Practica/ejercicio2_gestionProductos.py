alimentosBebidas = ["Frijoles Refritos", "Coca Cola", "Zumo de Naranja", "Cafe de Olla", "Gorditas de Chicharron", "Huevos Motuleños"]
print("Lista Original: ", alimentosBebidas)

#Ordenar lista alfabeticamente
alimentosBebidas.sort() 

#Convertir lista a cadena de nombres
cadenaAlimentosBebidas = ", ".join(map(str, alimentosBebidas))

#Convertir cada nombre de la lista a Slug URL
listaSlug = list(map(lambda lista: lista.lower().replace(" ","-"), alimentosBebidas))

print("Lista ordenada alfabeticamente: ", alimentosBebidas)
print("a) Lista de Slugs URL: ", listaSlug)
print("b) Cadena de nombres en orden : ", cadenaAlimentosBebidas)
