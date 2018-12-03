# -*- coding: utf-8 -*-


# Devolve a matriz de dados...!
def get_dados():
    return [[7, 8, 9], [4, 5, 6], [1, 2, 3]]


# Pega os dicionários para a matriz de dados
def get_dics():
    dados = get_dados()

    el_dic = {}
    pos_dic = {}

    for x, line in enumerate(dados):
        for y, e in enumerate(line):
            pos_dic[(x, y)] = e
            el_dic[e] = (x, y)

    return el_dic, pos_dic


el_dic, pos_dic = get_dics()


# Pega a posição no dicionário de posições na matriz com a devida chave de valor na matriz...!
def get_x_y(pc):
    return el_dic[pc]


# Pega a posição no dicionário de valor na matriz com a devida chave de posição na matriz...!
def get_el(x, y):
    return pos_dic[(x, y)]


# Uma posição é válida na matriz fornecida?
def valid_pos(x, y, len_x, len_y):
    if x < 0 or y < 0:
        return False

    return x < len_x and y < len_y


# popula o dicionário da lista de posições possíveis.
def populate_lista_pos_dic():
    lista_pos = {}

    dados = get_dados()

    line = dados[0]
    len_x, len_y = len(line), len(dados) # Vê os tamanhos da matriz de dados

    # Varre por todos os itens da matriz de dados...
    for i in range(1, len_y * len_x + 1):
        t_p = get_x_y(i)
        x, y = t_p
        candidate_pos = []

        for t in ((1, 2), (2, 1)):
            d_a, d_b = t
            for a in (-d_a, d_a):
                for b in (-d_b, d_b):
                    c_x = x + a
                    c_y = y + b
                    if valid_pos(c_x, c_y, len_x, len_y):
                        candidate_pos.append((c_x, c_y))

        lista_pos[(x, y)] = candidate_pos

    return lista_pos



lista_pos_dic = populate_lista_pos_dic()


# Função auxiliar que pega os próximos movimentos possíveis para o cavalo, dada uma posíção!
def get(pc):
    lista = []

    x_pc, y_pc = get_x_y(pc)

    lista_pos = lista_pos_dic[(x_pc, y_pc)]

    for t in lista_pos:
        lista.append(get_el(*t))

    return lista


# Função auxiliar recursiva para popular a lista com as listas desejadas!
def f_aux(listas, n):
    # Caso base desta função recursiva!
    if len(listas[0]) == n:
        return listas

    result = list()
    for lista in listas:
        p = lista[-1]
        nova = get(p) # pega novas posições possíveis!
        n_ls = [] # lista de novas listas...
        for el in nova: # Para cada posição nova...
            sub = [i for i in lista]
            sub.append(el) # popula uma nova sublista a partir da lista dada acrescida com a nova
                           # posição...
            n_ls.append(sub) # acrescenta a nova sublista...
        result.extend(n_ls) # acrescenta, na lista final, as novas listas possíveis...

    return f_aux(result, n) # chamada recursiva para preencher as listas até o tamanho ideal!


def f(p, n):
    result = list()
    if p > 0 and p < 10 and n > 0:
        return f_aux([[p,],], n)

    return result


if __name__ == "__main__":
    assert 8 in get(1)
    assert 6 in get(1)
    assert 7 in get(2)
    assert 9 in get(2)
    assert 8 in get(3)
    assert 4 in get(3)
    assert 9 in get(4)
    assert 3 in get(4)
    assert not len(get(5))
    assert 7 in get(6)
    assert 1 in get(6)
    assert 6 in get(7)
    assert 2 in get(7)
    assert 1 in get(8)
    assert 3 in get(8)
    assert 4 in get(9)
    assert 2 in get(9)
    p = int(input('Insira p: '))
    n = int(input('Insira n: '))
    r = f(p, n)
    print 'resultado:', r
