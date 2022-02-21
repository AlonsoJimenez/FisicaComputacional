#define:


#Funcion derivacion centrada
def centrada(x, h):
    numerador = funcionDerivada(x + h) - funcionDerivada(x - h)
    resultado = numerador / (2 * h)
    return resultado

#Funcion encuentra el valor en la misma
def funcionDerivada(x):
    valor = 2*(x**3)
    return valor
