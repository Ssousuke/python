palavra = input('Digite a palavra chave: ')
palpite = input('Digite a letra do palpite: ')
if len(palpite) > 1:
    print('Você só pode chutar uma letra!')
    palpite = input('Digite a letra do palpite: ')
else:
    if palpite in palavra:
        print(f'Você acertou a letra: {palpite}')
    else:
        print('Você errou!')
