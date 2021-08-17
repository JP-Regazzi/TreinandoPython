numerador = int(input('Digite o numerador '))
denominador = int(input('Digite o denominador '))
quociente = numerador//denominador
resto = numerador % denominador
voltas = 1000
resposta = f'{quociente}.'
while voltas > 0 and resto > 0:
    numerador = resto * 10
    quociente = numerador // denominador
    resposta += str(quociente)
    resto = numerador % denominador
    voltas -= 1
print(f'O resultado e {resposta}')
