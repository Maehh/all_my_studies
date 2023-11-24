# from sys import path
# from Aula_21_package.modulo import soma
# from Aula_21_package import modulo 


# print(soma(2, 2))

print(__name__)
# print(*path, sep='\n')


import Aula_21_package

from Aula_21_package import soma, multi

# print(Aula_21_package.__name__)

# print(Aula_21_package.modulo.soma(1, 1))

print(soma(1, 2))
print(multi(2, 2))