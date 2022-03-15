from random import choice

jogadas = ['pedra','papel','tesoura']
vencedor = 0

while(vencedor != 1):
    jogada = input('Escolha Pedra/Papel/Tesoura: ')
    jogada.lower()
    comp = choice(jogadas)
    print('A máquina escolheu',comp)
    
    if (jogada == 'pedra' and comp == 'pedra'):
        print('Empate!')
    elif (jogada == 'pedra' and comp == 'papel'):
        print('Derrota!')
    elif (jogada == 'pedra' and comp == 'tesoura'):
        print('Vitória!')
        vencedor = 1
    elif (jogada == 'papel' and comp == 'papel'):
        print('Empate!')
    elif (jogada == 'papel' and comp == 'tesoura'):
        print('Derrota!')
    elif (jogada == 'papel' and comp == 'pedra'):
        print('Vitória!')
        vencedor = 1
    elif (jogada == 'tesoura' and comp == 'tesoura'):
        print('Empate!')
    elif (jogada == 'tesoura' and comp == 'pedra'):
        print('Derrota!')
    elif (jogada == 'tesoura' and comp == 'papel'):
        print('Vitória')
        vencedor = 1
    else:
        print('Inválido!')