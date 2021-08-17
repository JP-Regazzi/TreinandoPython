l = eval(input('Digite uma lista '))


def ordena_insercao(lista):
    lf = []
    while lista:
        minimo = lista[0]
        for numero in lista:
            if numero < minimo:
                minimo = numero
        lf.append(minimo)
        lista.remove(minimo)
    return lf


print(ordena_insercao(l))

# x = [1, 2, 3, 4]
# y = [5, 6, 7, 8]


# def produto_vetorial(a, b):
#     soma_final = []
#     for i in range(len(a)):
#         soma_final += [a[i]*b[i]]
#     return soma_final
#
#
# print(produto_vetorial(x, y))
#
#
# def coluna(M, i):
#     lista_coluna = []
#     for linhas in range(len(M[0])):
#         lista_coluna += [M[linhas][i]]
#     return lista_coluna
#
#
# matriz = eval(input('Digite M '))
# index = int(input('Digite a coluna '))
# print(coluna(matriz, index))
