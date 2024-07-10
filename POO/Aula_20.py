# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arq, modo):
    try:
        print('Abrindo arq.')
        arquivo = open(caminho_arq, modo, encoding='utf8')
        yield arquivo
    except Exception as err:
        print('Erro: ', err)
    finally:  
        print('Fechando arq.')
        arquivo.close()


class MyOpen:

    def __init__(self, caminho_arq, modo):
        self.caminho_arq = caminho_arq
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Enter - Abrindo arq.')
        self._arquivo = open(self.caminho_arq, self.modo, encoding='utf8')

        return self._arquivo
    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit - Fenchando arq.')
        self._arquivo.close()

        raise class_exception(*exception_.args).with_traceback(traceback_)
    
        print(class_exception)
        print(exception_)
        print(traceback_)

        return True     # "Tratei a exceção"

with my_open('Arquivo_teste_aula_20(1).txt', 'w') as teste:
    teste.write('OIIIIIII',2)
    

