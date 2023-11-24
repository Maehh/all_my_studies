# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'luiz' #str 
# print(string.upper())
# print(isinstance(string, str))

'''class Pessoa:    #"p1" "Marcos"  "Jose"              # MOLDE PARA OBJETOS
    def __init__(self, nome, sobrenome):            # DEFINE ATRIBUTOS DA INSTANCIA
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Marcos', 'José')               # PESSOA(MOLDE) CRIA > INSTÂNCIA OU OBJETO
# p1.nome = 'Luiz'
# p1.sobrenome = 'Jorje'

print(p1.nome)
print(p1.sobrenome)'''


#Métodos em instâncias de Classes em Python
# Hard Coded - Escrito diretamente no codigo

'''class Carro():

    def __init__(self, nome):           # PRIMEIRO METODO
 #       self.nome = 'Fusca'     
        self.nome = nome   
    
    def acelerar(self):                 
        print(f'{self.nome} está acelerando...')

volksvagen = Carro('Fusca')
print(volksvagen.nome)
volksvagen.acelerar()

hotwheels = Carro('Hotwheels')
print(hotwheels.nome)
hotwheels.acelerar()'''


class DoubleMult:
    def __init__(self, val):
        self.value = val
    
    def multiply(self, mval=None):
        if mval != None:
            self.value = self.value*mval
        else : 
            self.value = self.value*2

    def divide(self, dval=None):

        if dval != None:
            self.value = int(self.value/dval)
        else : 
            self.value = int(self.value/2)
        

numero_aleatorio = DoubleMult(2)
numero_aleatorio.multiply(5) 
numero_aleatorio.divide(2)

print(numero_aleatorio.value)

# print(numero_aleatorio.value, isinstance(numero_aleatorio, DoubleMult))