# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

'''from typing import Any


class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, name, *args: Any, **kwds: Any) -> Any:
        print(f'{name} está Chamando: {self.phone}' )

        return 1234

callme = CallMe('0012345678987')

retorno = callme('Gustavo')

print(retorno)'''

# Classes decoradoras (Decorator Classes)


class Multiplicar:                  # 1- Criada Class Decoradora
    def __init__(self, multiplicador) -> None:          # Classe com método init (recebe argumento Multiplicador)
        print('__init__')
        self._multiplicador = multiplicador

    def __call__(self, func):                   # 2 - Criado Método Call (Onde a função será executada)
       
       def interna(*args, **kwds):              # 3 - Func. interna criada para guardar argumentos da função "soma()"
            resultado = func(*args, *kwds)      # Resultado executa função..
            return resultado * self._multiplicador    # ..e retorna resultado multiplicado pelo self._multiplicador inserido 
       return interna                                  # 4 - Função interna chamada 
        

@Multiplicar(10)         # DECORATOR                           # 5 - Adicionado a classe decoradora a função soma()
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 2)
print(dois_mais_dois)

'''
Resumo: 
    Para que uma Class decoradora possa funcionar com a função, é necessário definir onde a função será executada dentro da
classe, no exemplo acima foi ultilizado o método __call__, mas também pode ser usado no método __init__ ou em outro método,
desde que a função possa ser guardada dentro da classe antes do uso.


'''