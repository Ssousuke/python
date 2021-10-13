# Faça um programa que leia dois vetores de 10 elementos. Crie um
# vetor que seja a intersecção entre os 2 vetores anteriores, ou
# seja, que contém apenas os númerosque estão em ambos os vetores.
# Não deve conter números repetidos.

vetorX = []
vetorY = []

for i in range(0, 3):
    x = int(input(f'{i + 1}º, X: '))
    if not x in vetorY:
        vetorX.append(x)

    y = int(input(f'{i + 1}º, Y: '))
    if not y in vetorX:
        vetorY.append(y)

uniao = []
uniao.extend(set(vetorY + vetorX))
print(uniao)
