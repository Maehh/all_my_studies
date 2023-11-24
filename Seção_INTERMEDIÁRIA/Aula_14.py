# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v) :
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for jorje in range(10) :
    lista.append(jorje)
# print(lista)

lista = [num*2 for num in range(10)]
print(lista)

# Mapeamento de Listas

# Mapeamento é criar outra lista a partir de outros
# dados ou não necessariamente do conteudo de uma lista.
# O conteudo pode ser modificado ou não durante esse processo

produtos = [
    {'nome' : 'p1', 'preco' : 20},
    {'nome' : 'p2', 'preco' : 10},
    {'nome' : 'p3', 'preco' : 30},
]
# Criando uma nova lista aumentando 5% nas vendas da chave preço acima, 

novos_produtos = [
    {**produto, 'preco' : produto['preco'] * 1.05}  # Desempacota-se 'produto' e cria uma chave preco com o valor
                                                    # produto['preco'] * 1.05 (aumento de 5%)
    if produto['preco'] > 20 else {**produto}       # if - Apenas será multiplicado se o preco for maior que 20
    for produto in produtos                         # Este processo será aplicado para cada produto na lista produtos
    if produto['preco'] >= 20 and produto['preco'] > 10 # Filtro : Apenas Mostrará os preços menores que 20
]
# print(*novos_produtos, sep='\n')
# p(novos_produtos)


# FILTROS

# O que vem na esquerda do For é mapeamento, o que vem na direita é filtro.
# Já o filtro é selecionando qual valor passa ou não dentro da lista

lista = [n for n in range(10) if n < 5] # Filtro if : Apenas Mostrará os preços menores que 5

print(lista)

'''
Outros Exemplos
'''

# lista = []

# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))


'''
Relembrando :
    Lado esquerdo do for: Mapeamento
    Lado direito do for : Filtro
'''

# lista = [(x, y) 
#         for x in range(3)
#         for y in range(3)
#         ]

# lista = [
#         [x for x in range(3)]
#          for x in range(3)
#         ]

lista = [
    [letra + 'A' if letra == 'G' else letra for letra in 'Gustavo']
    for x in range(3)
    
]

print(*lista, sep='\n')