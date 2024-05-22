# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def speak_class_name(self):
        print(self.__class__.__name__)

    def say_hi(self):
        print(f"My name is {self.nome} {self.sobrenome}! And I'm a {self.__class__.__name__}")
    


class Cliente(Pessoa):
    
    def scream(self):
        print('AAAAAAAAAAAAA')

class Aluno(Pessoa):
    
    def study(self):
        print("I no no wanna :(")

c1 = Cliente('Jorje', 'Marcos')

c2 = Aluno('Maria', 'Eduarda')

c1.say_hi()
c2.say_hi()
c1.scream()
c2.study()
# c2.scream()

