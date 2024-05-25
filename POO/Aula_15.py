# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.


# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, ABCMeta, abstractmethod

class Log(metaclass=ABCMeta):
    ...


class Log(ABC):
    def __init__(self, foo):
        self._foo = foo

    @property
    # @abstractmethod
    def foo(self):
        return self._foo
    
    @foo.setter
    @abstractmethod
    def foo(self, foo):   ...         # <--- Não necessário colocar setter para abstract method
        # self._foo = foo
    

class LogPrintMixin(Log):
    def __init__(self, foo):
        super().__init__(foo)

    @property
    def foo(self):
        return self._foo
    
    @Log.foo.setter
    def foo(self, foo):
        self._foo = foo



l = LogPrintMixin('Bah')

print(l.foo)


