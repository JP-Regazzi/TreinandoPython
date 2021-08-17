def multiplos_de_7(n):
    lista = []
    for numero in range(n):
        if numero / k == numero // k:
            lista += [numero]
    return lista


k = int(input("Digite um número para fazer papel de k "))
print(multiplos_de_7(int(input('Digite um número para que receba todos os menores que ele, e múltiplos de k '))))
