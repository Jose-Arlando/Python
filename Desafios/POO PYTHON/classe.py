class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Bom dia! me chamo {self.nome}, prazer! tenho {self.idade} anos")
    def maior_de_idade(self):
        if self.idade > 18:
            print(f"{self.nome} maior de idade")
        else:
            print(f"{self.nome} menor de idade")

a = Aluno("José", 17)
b = Aluno("Rosi", 20)

print(a.nome)
print(b.nome)

a.apresentar()
b.apresentar()

a.maior_de_idade()
b.maior_de_idade()

for alunos in Aluno:
    print(Aluno.nome)