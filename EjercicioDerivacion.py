#Ejercicico practica clase 18 de febrero

#Funcion derivacion hacia adelante
def adelante(x, h):
    numerador = funcion(x+h) - funcion(x)
    resultado = numerador/h
    return resultado


#Funcion derivacion hacia atras
def atras(x, h):
    numerador = funcion(x) - funcion(x-h)
    resultado = numerador/h
    return resultado

#Funcion derivacion centrada
def centrada(x, h):
    numerador = funcion(x + h) - funcion(x - h)
    resultado = numerador / (2 * h)
    return resultado

#Funcion derivacion diferencias centradas v2.0
def centrada2(x, h):
    numerador = funcion(x - (2*h)) - 8 * funcion(x - h) + 8 * funcion(x + h) - funcion(x + (2*h))
    resultado = numerador / (12*h)
    return resultado


#Funcion matematica a realizar
def funcion(x):
    valor = 2*(x**3)
    return valor

#Ejecutamos e imprimimos el resultado
print(adelante(8, 0.00000000001))
print(atras(8, 0.00000000001))
print(centrada(8, 0.00000000001))
print(centrada2(8, 0.00000000001))




#%%
