# -*- coding: utf-8 -*-

import cProfile


def f(p, n):
    if p > 0 and p < 10 and n > 0:
        # Casos de posições possíveis para o cavalo realizar o(s) salto(s)!
        # A posição 5 não permite que o cavalo consiga realizar um salto!
        if p != 5:
            # Para cada elemento, mapeia os outros elementos alcançáveis via um salto simples do cavalo!
            elem_dic = {1 : (6, 8), 2 : (7, 9),
                        3 : (4, 8), 4 : (3, 9),
                        5 : tuple(), 6 : (1, 7),
                        7 : (2, 6), 8 : (1, 3),
                        9 : (2, 4)}

            listas = [[p,],]

            while len(listas[0]) < n:
                original_len = len(listas)

                for i in range(original_len):
                    lista = listas[i]
                    first_pos, second_pos = elem_dic[lista[-1]]
                    lista1 = lista[:]
                    lista1.append(first_pos)
                    lista.append(second_pos)
                    listas.append(lista1)

            return listas

    return list()


if __name__ == "__main__":
    p = int(input('Insira p: '))
    n = int(input('Insira n: '))
    r = f(p, n)

    cProfile.run('s = f(p, n)')

    print 'len(f):', len(r)
    # print 'resultado:', r
