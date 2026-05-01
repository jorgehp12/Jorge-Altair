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
def calcula_pontos_soma(l):
    n = 0
    for numero in l:
        n += numero
    return n
def calcula_pontos_sequencia_baixa(l):
    n = 0
    if 1 in l and 2 in l and 3 in l and 4 in l:
        n += 15
    elif 2 in l and 3 in l and 4 in l and 5 in l:
        n += 15
    elif 3 in l and 4 in l and 5 in l and 6 in l:
        n += 15
    return n
def calcula_pontos_sequencia_alta(l):
    n = 0
    if 1 in l and 2 in l and 3 in l and 4 in l and 5 in l:
        n += 30
    elif 2 in l and 3 in l and 4 in l and 5 in l and 6 in l:
        n += 30
    return n
def calcula_pontos_full_house(l):
    contagem = {}
    for i in l:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
    if len(contagem) == 2 and 2 in contagem.values() and 3 in contagem.values():
        total = 0
        for i in l:
            total += i
        return total
    return 0
def calcula_pontos_quadra(dados):
    for valor in dados:
        if dados.count(valor) >= 4:
            total = 0
            for dado in dados:
                total += dado
            return total
    return 0
def calcula_pontos_quina(dados):
    for valor in set(dados):
        if dados.count(valor) >= 5:
            return 50
    return 0
