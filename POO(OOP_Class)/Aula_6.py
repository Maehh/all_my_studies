# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):                # <- Meu código  - ENCAPSULAMENTO DE DADOS
        # Private protected public
        self.cor_tinta = cor 

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456


###################################
caneta = Caneta('Azul')                     # - Código cliente

print(caneta.cor)                     
print(caneta.cor)                     
print(caneta.cor)                     
print(caneta.cor)                     
print(caneta.cor)                     



'''
class Caneta:
    def __init__(self, cor):                # <- Meu código  - ENCAPSULAMENTO DE DADOS
        # Private protected public
        self.cor_tinta = cor 

    def get_cor(self):
        return self.cor_tinta


###################################
caneta = Caneta('Azul')                     # - Código cliente

#print(caneta.cor)                      # <- XXXXX
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())'''