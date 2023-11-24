# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'nome' : 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 900,
# }

# pessoa.setdefault('idade', None)
# print(len(pessoa))
# print(pessoa['sobrenome'])
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print(pessoa['idade'])
# for chave in pessoa.keys():
#     print(chave)
# for chave in pessoa.values():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(f'{chave} : {valor}')
import copy

d1 = {
    'c1' : 1,
    'c2' : 2,
    'li' : [0, 1, 2]
}

# d2 = copy.deepcopy(d1)
# d2['li'][1] = 12
# print(d1)
# print(d2)

nome = d1.pop('c1')
nome2 = d1.popitem()
print(nome)
print(nome2)
print(d1)

# d1.update({
#     'c2' : 12,
#     'li' : [2, 3, 4]
# })
# d1.update(nome='Novo Valor', idade=125)
# tupla = (('nome', 'novo valor'), ('idade', 2000))
tupla = [['nome', 'novo valor'], ['idade', 2000]]
d1.update(tupla)
print(d1)