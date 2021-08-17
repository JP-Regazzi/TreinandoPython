x = float(input('Digite a coordenada das abscissa '))
y = float(input('Digite a coordenada das ordenadas '))
if x == 0:
    if y > 0:
        print('Direção principal N')
    else:
        print('Direção principal S')
elif y/x > 1 or y/x < -1:
    if y > 0:
        print('Direção principal N')
    else:
        print('Direção principal S')
elif y/x == -1:
    if x > 0 and y < 0:
        print('Direção principal SE')
    else:
        print('Direção principal NW')
elif y == x:
    if x > 0:
        print('Direção principal NE')
    else:
        print('Direção principal SW')
else:
    if x > 0:
        print('Direção principal E')
    elif x < 0:
        print('Direção principal W')
