'''from itertools import count

count() é um iterador sem fim
Diferente do range(), que é apenas iterável, finito e necessita de um valor

c1 =  count(step=20)

for i in c1:
    if i > 100:
        break
    print(i)
'''

# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']

    ]

for i in combinations(pessoas, 2):
    print(*i)

for i in permutations(pessoas, 2):
    print(*i)

for i in product(*camisetas):
    print(*i)
