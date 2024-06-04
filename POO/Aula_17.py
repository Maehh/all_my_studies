# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


class MyError(Exception):

    ...
class MyError_2(Exception):
    ...


def levantar():
    exception_ = MyError('You made an error at line: 12  :D')
    exception_.add_note('Tradução: Erro cometido na linha: 12')
    raise exception_ 

try:
    
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print('\n')
    exception_ = MyError_2('You made another error')
    exception_.add_note('Você realizou outro erro')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error