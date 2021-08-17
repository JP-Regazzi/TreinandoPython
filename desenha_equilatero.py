n = int(input('Digite um número para ser a base de um triângulo equilátero '))
i = n
for linha in range(1, 1 + n):
    print((i-linha) * ' ', linha * '* ')