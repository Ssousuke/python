class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def imc(self):
        imc = (self.peso / (self.altura * self.altura))
        return imc

    def result_imc(self):
        if self.imc() < 18.5:
            print('Magreza!')
        elif self.imc() >= 18.5 and self.imc() <= 24.9:
            print('Normal!')
        elif self.imc() >= 25 and self.imc() <= 29.9:
            print('SobrePeso!')
        elif self.imc() >= 30 and self.imc() <= 39.9:
            print('Obsidade!')
        else:
            print('Obseidade Grave!')

    def show_imc(self):
        print(f'{self.nome}, tem {self.idade} anos de idade, tem {self.altura} metros de altura e {self.peso} de peso!')
        print(f'Seu imc é de: {self.imc()}')


if __name__ == '__main__':
    pessoa = Pessoa("Wesley Matheus da Silva Farias", 22, 1.63, 76.5)
    pessoa.show_imc()
    pessoa.result_imc()
