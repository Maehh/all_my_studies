# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class PublicClass:
    def __init__(self):
        self.atribute = 'This is public'
        self._protected = 'This is protected'
        self.__private = 'THIS is private'

    def public_method(self):
        return 'This is a public method'
    
    def _protected_method(self):
        raise PermissionError('This is a protected method')
        
    def __private_method(self):
        raise PermissionError('THIS IS A PRIVATE METHOD!')

p = PublicClass()

# print(p._protected_method())
p._PublicClass__private_method()                # <- name is altered so you can't use it outside the Class Object
                                    # _PublicClass__private_method <- Name mangling
p.__private_method() # <- NO!

