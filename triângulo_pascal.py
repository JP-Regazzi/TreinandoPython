n = int(input('Digite a quantidade de linhas do Triangulo de Pascal '))
print(f' {0}')
lista = []

for linha in range(1, n):
    resultado = ''
    r_lista = []
    for coluna in range(linha + 1):
        if coluna == linha or coluna == 0:
            resultado += ' 1'
            r_lista += [1]
        else:
            resultado += ' ' + str(int(lista[linha-2][coluna-1]) + int(lista[linha - 2][coluna]))
            r_lista += [int(lista[linha-2][coluna-1])+ int(lista[linha - 2][coluna])]
    print(resultado)
    lista += [r_lista]
