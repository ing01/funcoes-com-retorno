# Algoritmo com função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo). 

import math
def perfeito(n_min, n_max):
    lista = []
    for n in range(n_min, n_max + 1):
        soma = 1
        for div in range(2, math.ceil(math.sqrt(n))):
            if n % div == 0:
                soma += div
                div2 = int(n / div)
                if (div != div2):
                    soma += div2
                if soma > n:
                    break
        if n == soma:
            lista.append(n)
    return lista

print(perfeito(1, 10000))
