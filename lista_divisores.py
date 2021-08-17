numero, lista = int(input('Digite um numero natural ')), []
for divisor in range(2, numero):
    if numero % divisor == 0:
        lista += [divisor]
if lista == []:
    if numero == 0:
        print(f'{numero} não é primo')
    else:
        print(f'{numero} é primo')
else:
    print(f'Os divisores de {numero} são: {lista}')
