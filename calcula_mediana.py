print('Por favor, utilize apenas algarismos e pontos para representar os números')
n1 = float(input('Digite o primeiro número '))
n2 = float(input('Digite o segundo número '))
n3 = float(input('Digite o terceiro número '))
r = 0
if n1 > n2 > n3 or n3 > n2 > n1:
    r = n2
elif n1 > n3 > n2 or n2 > n3 > n1:
    r = n3
else:
    r = n1
print(f'A mediana é {r}')
