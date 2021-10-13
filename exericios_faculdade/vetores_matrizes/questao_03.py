# Leia um vetor com 10 números inteiros. Escreva os elementos
# do vetor eliminando elementos repetidos.

vetor = []
for i in range(0, 10):
    valor = int(input(f'{i+1}º - '))
    if not valor in vetor:
        vetor.append(valor)
print(vetor)
