class MediaAluno:
    notas = []

    def add_notas(self, nota):
        self.notas.append(nota)

    def calcula_notas(self):
        soma = 0
        for x in self.notas:
            soma += x
        media = (soma / len(self.notas))
        return media

    # def soma(self):
    # return sum(self.notas)


if __name__ == "__main__":
    aluno1 = MediaAluno()
    x = 8
    while x > 0:
        try:
            nota = int(input(f'Digite a {x}º: '))
            if 0 <= nota <= 10:
                aluno1.add_notas(nota)
                x -= 1
            else:
                print('A nota deve estar entre 0 e 10!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    print(aluno1.calcula_notas())
