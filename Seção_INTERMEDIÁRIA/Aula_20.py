# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import Aula_20_m
import sys
import importlib
# try:
#     import sys
#     sys.path.append('E:\Trabalhos\Cursos_Python\Projetos')
#     import Simple_dict_generator as simple
# except ModuleNotFoundError:
#     ...

# mydict = simple.dictgen('Abc', 12, ['Abcde', 0], 'Mark')
# print(mydict)
# x = [1, 2, 3, 4, 5, 6, 4, 6]

# p = Aula_20_m.replicas(x)
print('este modulo se chama:', __name__)
print(Aula_20_m.zonkp)
# print(p)

# print(*sys.path, sep='\n')
for i in range(10):
    importlib.reload(Aula_20_m)
    # print(i)

