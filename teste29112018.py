# -*- coding: utf-8 -*-

import cProfile

def get_dados():
    return [[7, 8, 9], [4, 5, 6], [1, 2, 3]]


# Para cada elemento, mapeia os outros elementos alcançáveis via um salto simples do cavalo!
elem_dic = {1 : (6, 8), 2 : (7, 9),
            3 : (4, 8), 4 : (3, 9),
            5 : tuple(), 6 : (1, 7),
            7 : (2, 6), 8 : (1, 3),
            9 : (2, 4)}


def get_available_positions(pc):
    return elem_dic[pc]


def f_aux(listas, n):
    # Caso base desta função recursiva!
    if len(listas[0]) == n:
        return listas

    result = list()

    for lista in listas:
        novas_pos_s = get_available_positions(lista[-1])
        lista1 = lista[:]
        lista1.append(novas_pos_s[0])
        lista.append(novas_pos_s[1])
        result.append(lista1)

    listas.extend(result)

    return f_aux(listas, n)


def f(p, n):
    if p > 0 and p < 10 and n > 0:
        if p == 5:
            return list()

        return f_aux([[p,],], n)

    return list()


if __name__ == "__main__":
    p = int(input('Insira p: '))
    n = int(input('Insira n: '))
    r = f(p, n)

    cProfile.run('s = f(p, n)')

    print 'len(f):', len(r)
    # print 'resultado:', r
