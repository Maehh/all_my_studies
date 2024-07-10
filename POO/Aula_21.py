# Funções decoradoras e decoradores com classes

def meur_repr(self) -> str:
    self.class_name = self.__class__.__name__
    self.class_dict = self.__dict__
    self.class_repr = f'{self.class_name}, ({self.class_dict})'
    return self.class_repr


def adiciona_repr(cls):
    cls.__repr__ = meur_repr
    return cls

def falar_nome_func(metodo):
    
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'
        
        return resultado
    return interno


# class MyReprMixin():

#     def __repr__(self) -> str:
#         self.class_name = self.__class__.__name__
#         self.class_dict = self.__dict__
#         self.class_repr = f'{self.class_name}, ({self.class_dict})'

#         return self.class_repr

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
    
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @falar_nome_func
    def falar_nome(self):
        return f'O planeta é {self.nome}.'

brasil = Time('Brasil')
portugal = Time('Portugal')


terra = Planeta('Terra')
marte = Planeta('Marte')
print(terra.falar_nome())

# print(f'{brasil!r}')
# print(f'{terra!r}')
