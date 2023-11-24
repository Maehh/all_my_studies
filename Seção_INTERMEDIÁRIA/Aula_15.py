# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}


lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc2 = { 
    chave: valor
    for chave, valor in lista

}

s1 = {i for i in range(10)}

print(dc)
print(dc2)
print(s1)

# isinstace - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

lista2 = [item*2 if isinstance(item, (int, float))
else item
for item in lista

]

for item in lista :
    if isinstance(item, set):
        print("SETS")
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print("STRINGS")
        print(item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)):
        print("INT")
        print(item + item)
    else :
        print("OUTROS")
        print(item)

print(lista2)

