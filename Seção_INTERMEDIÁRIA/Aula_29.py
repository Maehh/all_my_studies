# groupby - agrupando valores (itertools)
from itertools import groupby
import copy
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


# def ordena(aluno):
#     return aluno['nota']


# alunos_org = sorted(copy.deepcopy(alunos), key=ordena)
# # print(*alunos_org, sep='\n')

# # Dados prescisam estar ordenados

# # alunos = ['a','a', 'a', 'a', 'a',  'b', 'b', 'b', 'b','a', 'c']
# grupos = groupby(alunos_org, key=ordena)

# for chave, grupo in grupos:
#     print(chave, *list(grupo), sep='\n')

alunos_org2 = sorted(alunos, key=lambda x : x['nota'])

print(*alunos_org2, sep='\n')

for key, group_list in groupby(alunos_org2, key=lambda x : x['nota']):
    print(key, *group_list, sep='\n')
