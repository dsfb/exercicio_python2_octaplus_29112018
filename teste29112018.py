# -*- coding: utf-8 -*-


def get_dados():
    return [[7, 8, 9], [4, 5, 6], [1, 2, 3]]


# Para cada elemento retorna os outros elementos alcançáveis via um salto simples do cavalo!
def get_elem_dic():
    return {1 : (6, 8), 2 : (7, 9),
            3 : (4, 8), 4 : (3, 9),
            5 : tuple(), 6 : (1, 7),
            7 : (2, 6), 8 : (1, 3),
            9 : (2, 4)}


def get_available_positions(pc):
    return get_elem_dic()[pc]


def f_aux(listas, n):
    # Caso base desta função recursiva!
    if len(listas[0]) == n:
        return listas

    result = list()
    for lista in listas:
        novas_pos_s = get_available_positions(lista[-1])
        if novas_pos_s:
            lista1, lista2 = lista[:], lista
            lista1.append(novas_pos_s[0])
            lista2.append(novas_pos_s[1])
            result.extend([lista1, lista2])

    if not result:
        return result

    return f_aux(result, n)


def f(p, n):
    if p > 0 and p < 10 and n > 0:
        return f_aux([[p,],], n)

    return list()


if __name__ == "__main__":
    p = int(input('Insira p: '))
    n = int(input('Insira n: '))
    r = f(p, n)
    # print 'len(f):', len(r)
    print 'resultado:', r
