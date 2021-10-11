class Calculadora:
    def soma(*args):
        soma = 0
        for numeros in args:
            soma += numeros
        return soma

    def divisao(inicial, *args):
        for numeros in args:
            inicial /= numeros
        return inicial

    def multiplicacao(*args):
        multiplicacao = 1
        for numeros in args:
            multiplicacao *= numeros
        return multiplicacao

    def subtracao(inicial, *args):
        for numeros in args:
            inicial -= numeros
        return inicial


if __name__ == "__main__":
    soma = Calculadora.soma(10, 10, 10)
    print(soma)

    divisao = Calculadora.divisao(100, 2, 2)
    print(divisao)

    multi = Calculadora.multiplicacao(5, 5, 2)
    print(multi)

    sub = Calculadora.subtracao(100, 50, 10)
    print(sub)
