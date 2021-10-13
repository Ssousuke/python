# Faça um programa que preencha um vetor com 10 números reais, calcule e mostre
# a quantidade de números negativos e a soma dos números positivos desse vetor.

vetor = []
for i in range(0, 10):
    valor = int(input())
    vetor.append(valor)

negativos = 0
positivos = 0
for i in vetor:
    if i < 0:
        negativos += 1
    else:
        positivos += 1

print(f'Positivos: {positivos}, Negativos: {negativos}')
