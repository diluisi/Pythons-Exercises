from functools import reduce
import math

def moda(lista):
    freq = {}
    for i in lista:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    return sorted(freq.items(), key = lambda kv: kv[1], reverse = True)[0][0]

def media(lista):
    return reduce(lambda x, y: x + y, lista) / len(lista)

def variancia(lista):
    md = media(lista)
    sse = sum((i - md) ** 2 for i in lista)
    return sse / (len(lista))

def desvp(lista):
    return math.sqrt(variancia(lista))

def mediana(lista):
    nlista = sorted(lista)
    meio = len(lista)//2

    if len(lista) % 2 == 0:
        return (nlista[meio-1] + nlista[meio]) / 2.0
    else:
        return nlista[meio]

def cov(x,y):
    if len(x) != len(y):
        return
    n = len(x)
    xy = [x[i]*y[i] for i in range(n)]
    mean_x = media(x)
    mean_y = media(y)
    return (sum(xy) - n*mean_x * mean_y) / float(n)

def corr(x,y):
    return cov(x,y)/(desvp(x)*desvp(y))
