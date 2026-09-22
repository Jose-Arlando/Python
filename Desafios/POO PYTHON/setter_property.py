class Carro:
    def __init__(self, marca, modelo, cor, ano ):
        self.marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def ano(self):
        return self.__ano

    @property
    def tudo(self):
        return f"marca: {self.marca}\nmodelo: {self.modelo}\ncor: {self.cor}\nano:{self.ano}" #retornou uma string

    @modelo.setter
    def setterModelo(self, nome):
        self.__modelo = nome

    @cor.setter
    def setterCor(self, cor):
        self.__cor = cor

    @ano.setter
    def setterAno(self, ano):
        self.__ano = ano


c1 = Carro("toyota", "corola", "preto", 2019)
print(c1.modelo)
print(c1.cor)
print(c1.ano)
c1.setterModelo = "yaris"
print(c1.tudo)
