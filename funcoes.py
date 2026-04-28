# Jorge-Altair
import random

def rolar_dados(n):
    import random
    lista_dado = []
    for i in range(n):
        d = random.randint(1, 6)
        lista_dado.append(d)
    return lista_dado
def guardar_dado(dr,dg,n):
    dg.append(dr[n])
    del dr[n]
    lista = [dr,dg]
    return lista

