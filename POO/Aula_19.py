# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class NovaClasse(object):

    def __new__(cls, *args, **kwargs):
        # print('Antes de criar instancia')
        inst = super().__new__(cls)
        # print('Depois de criar instancia')
        # inst.x = 123
        return inst
        
    def __init__(self) -> None:
        print('Depois de criar instancia')

    def __repr__(self) -> str:
        return 'Teste A'

a = NovaClasse()

print(a.x)

# a = object.__new__(NovaClasse)
# a.__init__()