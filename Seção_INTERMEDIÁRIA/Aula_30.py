from functools import partial
from types import GeneratorType


# Map - para mapear dados
# é um iterator e generator que se esgota 
# caso precise da variável é só converter em list


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def increase_percentage(value, percentage):
    return round(value * percentage, 2)

increase_10_perc = partial(increase_percentage, percentage=1.1)


# new_products = [
#     {**p, 'preco' : increase_10_perc(p['preco'])}
#       for p in produtos
#     ]

def change_prod_name(p):
    return {**p, 'preco' : increase_10_perc(p['preco'])}


new_products = map(
    change_prod_name, produtos
)

new_products2 = list(map(
    lambda x : {**x, 'preco': 2}, produtos
    
))

print(*new_products, sep='\n')
print(*new_products2, sep='\n')
print(new_products.__iter__)
print(isinstance(new_products, GeneratorType))

print(list(new_products))