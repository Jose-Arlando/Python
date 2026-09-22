class Veiculo:
    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__valor = valor

    """
        para criar o setter, eu preciso criar o property antes para poder visualizar o valor do atributo
    """
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano > 1886:
            self.__ano = ano
        else:
            print("Ano inválido")

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self.__valor = valor
        else:
            print("Valor inválido")

    @property
    def mostrar_info(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nValor: {self.valor}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, valor, portas):
        super().__init__(marca, modelo, ano, valor)
        self.portas = portas

    def acelerar(self):
        return f"Carro {self.modelo} acelerando"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, valor, cilindrada):
        super().__init__(marca, modelo, ano, valor)
        self.cilindrada = cilindrada

    
    def acelerar(self):
        return f"Moto {self.modelo} acelerando"

class Concessionaria:
    def __init__(self):
        self.__veiculos = []

    @property
    def veiculos (self):
        return self.__veiculos

    def adicionar(self, veiculo):
        self.veiculos.append(veiculo)

m1 = Moto("Yamara", "ninja", 2018, 3000, 900)
ca1 = Carro("Mercedes", "C180", 2019, 32000, 4)
print(m1.acelerar())
c1 = Concessionaria()
c1.adicionar(ca1)
c1.adicionar(m1)
# print(c1.veiculos)
for veiculo in c1.veiculos:
    print(veiculo.mostrar_info)
    print("-"*20)

