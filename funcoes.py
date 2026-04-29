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
def remover_dado(dr,dg,n):
    dr.append(dg[n])
    del dg[n]
    lista_3 = [dr,dg]
    return lista_3
def calcula_pontos_regra_simples(l):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(l)):
        if l[i] in dic:
            dic[l[i]] += l[i]
    return dic
    

