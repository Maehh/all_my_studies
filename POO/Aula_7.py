# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Setter')
        if valor == 'Rozeo':
            raise ValueError('Cor errada')
        self._cor = valor

caneta = Caneta('Zaul')

caneta.cor = 'Rosio'


# getter ---> Obter valor 

print(caneta.cor)


