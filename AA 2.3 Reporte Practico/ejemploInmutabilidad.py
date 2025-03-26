#Ejemplo 1
variable_globlal = 10

def aumentar_variable():
    return variable_globlal + 1 #No se modifica la variable global, se retorna una nuevo valor

print(aumentar_variable())

#Ejemplo 2 inmutabilidad, funcion pura y sin efectos secundarios
def contar_palabras(texto):
    return len(texto.split()) #Separa el texto en palabras y cuenta cuanta la cantidad

oracion = "El tema de hoy es la inmutabilidad en Python"
print(contar_palabras(oracion))

#Ejemplo 3 Uso correcto de la funcion pura
contador_global = 0

def contar_palabras_no_funcional(texto):
    global contador_global #Se accede a la variable global
    contador_global = len(texto.split()) #Se reasigna la variable global
    
#Uso
texto_ejemplo = "Este es un ejemplo sencillo"
contar_palabras_no_funcional(texto_ejemplo)
print(contador_global)

#Mutabilidad