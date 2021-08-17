t = True
j1 = input('Qual sua jogada, jogador 1? ')
if j1 == 'sair':
    t = False
else:
    j2 = input('Qual a sua jogada, jogador 2? ')
while t:
    if (j1 == 'pedra' or j1 == 'papel' or j1 == 'tesoura') and (j2 == 'pedra' or j2 == 'papel' or j2 == 'tesoura'):
        if j1 == j2:
            print('empate')
        elif j1 == 'pedra' and j2 == 'tesoura' or j1 == 'tesoura' and j2 == 'papel' or j1 == 'papel' and j2 == 'pedra':
            print('O jogador 1 venceu')
        else:
            print('O jogador 2 venceu')
    elif j1 == 'sair' or j2 == 'sair':
        break
    else:
        print('As únicas jogadas possiveis sao "pedra", "papel" ou "tesoura" ')
    j1 = input('Se deseja continuar jogando, digite a jogada do jogador 1, caso contrário, digite "sair" ')
    if j1 == 'sair': break
    j2 = input('Qual a sua jogada, jogador 2? ')
print('\n FIM DE JOGO')
