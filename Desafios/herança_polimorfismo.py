class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    @property
    def acelerar(self):
        return "veiculo acelerando"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    @property
    def acelerar(self):
        return "carro acelerando"

c1 = Carro("Ferrari", "Puro sangue", "vermelho")
v1 = Veiculo("Volvo", "caminhão")

print(c1.acelerar)
print(v1.acelerar)
