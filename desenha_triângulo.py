n = int(input('Digite um número para ser a base de um triângulo reto com base n e altura n '))
i = n
print('Triângulo para direita:\n')
for linha in range(1, 1 + n):
    print('*' * linha)
print('\n')
print('Triângulo para esquerda:\n')
for linha2 in range (1, 1 + n):
    i -= 1
    print(' ' * i, '*' * linha2)