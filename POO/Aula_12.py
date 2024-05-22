# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# class MinhaString(str):
#     def lower(self):
#         print(f'Chamou Lower da classe: {self.__class__.__name__}')
#         return super().lower()


# string = MinhaString('OI')

# print(string.lower())

class A:           

    def __init__(self, atributo_novo):
        self.atributo_novo = atributo_novo

    def metodo(self):
       print('A') 

class B(A):                                 # O Super ".metodo()" Desta Classe (B) é A 

    def __init__(self, atributo_novo):
        super().__init__(atributo_novo)
        
        
    def metodo(self):
       super().metodo()
       print('B')

class C(B):
    
    def metodo(self):
       super(C, self).metodo()                  # O Super ".metodo()" Desta Classe (C) é B 
       print('C')


c = C('oi')

print(c.atributo_novo)

# c.metodo()
# print(C.mro())