def soma_algarismos_12(n):  # questao 25
    for numero in range(n):
        soma = 0
        for algarismo in str(numero):
            soma += int(algarismo)
        if soma == 12:
            print(numero)


soma_algarismos_12(int(input('digita um n ai p ver numeros com soma algarismos igual a 12 ')))


def soma_algarismos_12_l(n):  # questao 26
    lista = []
    for numero in range(n):
        soma = 0
        for algarismo in str(numero):
            soma += int(algarismo)
        if soma == 12:
            lista += [numero]
    return lista


print(soma_algarismos_12_l(int(input('de cima saindo em lista '))))
