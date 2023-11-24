from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
'''
def deduces_func(acumulator, produto):          # Acumulador atualiza o valor retornado 
    print(f'{acumulator=}')
    print(produto)
    return acumulator + produto['preco']            

total = reduce(
    deduces_func,
    produtos,
    0            # Valor inicial do arg 'acumulator' em deduces_func
)'''

total = reduce(
    lambda ac, p : ac + p['preco'],                 # MESMA BOSTA COM LAMBDA ^^^^^ 
    produtos,
    0  )

print(total)

# for p in produtos:
#     total += p['preco']

# print(total)