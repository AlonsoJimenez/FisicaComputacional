#define:

def trapezoide(limiteI, limiteS, n):
    vecPesos = pesos(limiteS, limiteI, n)
    h = (limiteS-limiteI)/n
    resultado = 0
    empieza = limiteI
    for i in range(n+1):
        resultado += funcion(empieza)*vecPesos[i]
        empieza += h
    return resultado




#La siguiente funcion evalua y consigue el vector de pesos para el trapezoide
def pesos(b, a, n):
    h = (b - a) / n
    vectorPesos = []
    vectorPesos += [h / 2]
    for i in range(n-1):
        vectorPesos += [h]
    vectorPesos += [h/2]
    return vectorPesos



#La siguiente funcion evalua el punto x en la funcion
def funcion(x):
    valor = x**3
    valor = 2*valor
    return valor


#Ejecucion del codigo
print(trapezoide(0,3, 2500))
#%%
