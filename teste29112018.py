# -*- coding: utf-8 -*-


def get_dados():
    return [[7, 8, 9], [4, 5, 6], [1, 2, 3]]


def get_elem_dic():
    return {1 : (6, 8), 2 : (7, 9),
            3 : (4, 8), 4 : (3, 9),
            5 : tuple(), 6 : (1, 7),
            7 : (2, 6), 8 : (1, 3),
            9 : (2, 4)}


elem_dic = get_elem_dic()


def get(pc):
    return elem_dic[pc]


def f_aux(listas, n):
    # Caso base desta função recursiva!
    if len(listas[0]) == n:
        return listas

    result = list()
    for lista in listas:
        p = lista[-1]
        novas_pos_s = get(p)
        new_lst_s = lista * len(novas_pos_s)

        iterator = 0
        for indice, el in enumerate(novas_pos_s):
            for i in range(iterator, iterator + len(lista)):
                new_lst_s[i].append(el)
            iterator += len(novas_pos_s)
        result.extend(new_lst_s)

    return f_aux(result, n)


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
    print 'len(f):', len(r)
    # print 'resultado:', r
