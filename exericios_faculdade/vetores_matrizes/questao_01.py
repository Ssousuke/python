# Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
# Imprima o vetor, o maior elemento e a posição que ele se encontra.

vetor = []
for i in range(0, 10):
    valor = int(input(f'Digite o {i+1}º número: '))
    vetor.append(valor)

maior = 0
posicao = 0

for indice, valor in enumerate(vetor):
    if valor > maior:
        maior = valor
        posicao = indice

print(f'Número: {maior}, Posição: {posicao}')
