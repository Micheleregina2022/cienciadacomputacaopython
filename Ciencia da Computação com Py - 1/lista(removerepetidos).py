#cria-se uma segunda lista com cada elemento diferente da outra lista,
# apresenta-se a lista criada em ordem crescente (L.SORT)

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [2, 4, 2, 2, 3, 3, 1]

lista = remove_repetidos(lista)
print (lista)