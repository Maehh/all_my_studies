# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um ou mais Fabricantes
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome, motor=None):
        self._nome = nome
        self._motor = motor
        self.fabricantes = list()

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    def registrar_fabricantes(self, *fabricantes):
        for fabricante in fabricantes:
            self.fabricantes.append(fabricante)

    def informacoes_do_carro(self):
        print(f'Nome do carro: {self.nome}')
        print(f'Motor: {self.motor.nome}')
        print('Fabricantes do Carro:')
        for fabricante in self.fabricantes:
            print(f'{fabricante._nome}')


class Motor:
    def __init__(self, nome, *carros):
        self.nome = nome
        self.carros = list(carros)

class Fabricante:
    def __init__(self, nome):
        self._nome = nome

carro = Carro('Corola')
toyota = Fabricante('Toyota')
honda = Fabricante('Honda')
motor_v8 = Motor("Motor V8")

carro.motor = motor_v8
carro.registrar_fabricantes(toyota, honda)
carro.informacoes_do_carro()

