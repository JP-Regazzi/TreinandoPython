signo = ''
while signo == '':
    dia = int(input('Digite o dia de seu nascimento '))
    mes = input('Digite o mês de seu nascimento ')
    if mes.lower() == 'janeiro':
        if dia >= 20:
            signo = 'aquário'
        else:
            signo = 'capricórnio'
    if mes.lower() == 'fevereiro':
        if dia >= 19:
            signo = 'peixes'
        else:
            signo = 'aquário '
    if mes.lower() == 'março' or 'marco':
        if dia >= 21:
            signo = 'áries'
        else:
            signo = 'peixes'
    if mes.lower() == 'abril':
        if dia >= 20:
            signo = 'touro'
        else:
            signo = 'áries'
    if mes.lower() == 'maio':
        if dia >= 21:
            signo = 'gêmeos'
        else:
            signo = 'touro'
    if mes.lower() == 'junho':
        if dia >= 22:
            signo = 'câncer'
        else:
            signo = 'gêmeos'
    if mes.lower() == 'julho':
        if dia >= 23:
            signo = 'leão'
        else:
            signo = 'câncer'
    if mes.lower() == 'agosto':
        if dia >= 23:
            signo = 'virgem '
        else:
            signo = 'leão'
    if mes.lower() == 'setembro':
        if dia >= 23:
            signo = 'libra'
        else:
            signo = 'virgem'
    if mes.lower() == 'outubro':
        if dia >= 23:
            signo = 'escorpião'
        else:
            signo = 'libra'
    if mes.lower() == 'novembro':
        if dia >= 22:
            signo = 'sagitário'
        else:
            signo = 'escorpião'
    if mes.lower() == 'dezembro':
        if dia >= 22:
            signo = 'capricórnio'
        else:
            signo = 'sagitário'
    if signo == '':
        print('Por favor, digite o dia em números e o mês com letras!')
print(f'Seu signo é {signo}')
