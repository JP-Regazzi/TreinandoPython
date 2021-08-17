l1 = float(input('Digite o tamanho de um lado do triângulo '))
l2 = float(input('Digite o tamanho de outro lado do triângulo '))
l3 = float(input('Digite o tamanho do ultimo lado do triângulo '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('O triangulo é equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triangulo é isósceles')
    else:
        print('O triangulo é escaleno')
else: print('Os lados selecionados não formam triângulo')