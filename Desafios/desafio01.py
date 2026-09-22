class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade >=0:
            self.__idade = idade
        else:
            print("Idade inválida")

    @property
    def mostrar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

lista_pessoas = [
    Pessoa("Jose", 19),        
    Pessoa("Rosi", 20)
]
idade = int(input("idade"))
lista_pessoas[0].idade = idade
   
print(lista_pessoas[0].mostrar)     
print(lista_pessoas[1].mostrar)     
