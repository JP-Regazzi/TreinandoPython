lista, lista_divisores, i = eval(input('coloque uma lista de numeros ')), [], 0
for numero in lista:
    for divisor in range(2, numero + 1):
        if numero % divisor == 0:
            lista_divisores += [divisor]
for x in lista_divisores:
    if lista_divisores.count(x) == len(lista):
        print(f'O número {x} é o menor divisor comum de {lista}')
        i = 1
        break
if i == 0:
    print(f'Os números {lista} são primos entre si')
