# -*- coding: utf-8 -*-


# Função auxiliar que pega os próximos movimentos possíveis para o cavalo, dada uma posíção!
def get(pc):
    lista = []
    dados = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

    primeiro_elemento_segunda_sublista = 4
    primeiro_elemento_primeira_sublista = 7

    if pc < primeiro_elemento_segunda_sublista:
        index = 2 # índice da terceira sublista
    elif pc < primeiro_elemento_primeira_sublista:
        index = 1 # índice da segunda sublista
    else:
        index = 0 # índice da primeira sublista

    cur_line = dados[index]

    cur_x = cur_line.index(pc)

    deslocamento_cavalo_direcao_um = 1
    deslocamento_cavalo_direcao_dois = 2

    # Avalia e preenche a lista com o(s) deslocamento(s) possível(is) do cavalo!
    for cur_ind, line in enumerate(dados):
        if abs(cur_ind - index) == deslocamento_cavalo_direcao_um:
            for cur_y, e in enumerate(line):
                if abs(cur_y - cur_x) == deslocamento_cavalo_direcao_dois:
                    lista.append(e)
        elif abs(cur_ind - index) == deslocamento_cavalo_direcao_dois:
            for cur_y, e in enumerate(line):
                if abs(cur_y - cur_x) == deslocamento_cavalo_direcao_um:
                    lista.append(e)

    return lista


# Função auxiliar!
def f_aux(lista, n):
    if len(lista) == n:
        return lista

    result = list()
    p = lista[-1]
    nova = get(p) # pega novas posições possíveis!
    for el in nova: # para cada nova posição possível...
        sub = [i for i in lista]
        sub.append(el) # popula uma nova sublista a partir da lista dada acrescida com a nova posição...
        result.append(f_aux(sub, n)) # propaga recursivamente todas as listas possíveis com esta posição...

    return result


def f(p, n):
    result = list()
    if p > 0 and p < 10 and n > 0:
        return f_aux([p,], n)

    return result


if __name__ == "__main__":
    p = int(input('Insira p: '))
    n = int(input('Insira n: '))
    r = f(p, n)
    print 'resultado:', r
