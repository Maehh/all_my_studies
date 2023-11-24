# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [1, 3, 25, 22, 854, 200, 10, 11, -1, 110]

# lista.sort(reverse=True)
# # sorted(lista)
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item) :
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista :
#     print(item)


# VERSÂO LAMBDA

def exibir(lista) :
    for item in lista :
        print(item)
    print()
# lista.sort(key=lambda item: item['nome'])

s1 = sorted(lista, key=lambda item: item['nome'])
s2 = sorted(lista, key=lambda item: item['sobrenome'])

# print(s1)
exibir(s1)
exibir(s2)

# Funções Lambda complexas

def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

               # Def | Parâm | Return | Argumentos 
# print(executa(lambda   x, y   : x + y,    2, 3),

#     executa(soma(2, 3))
# )


# Outro Exemplo

# def criar_multiplicador(multiplicador):
#     def multiplica(num):
#         return num * multiplicador
#     return multiplica

# duplica = criar_multiplicador(2)

# duplica = executa(
#     lambda m: lambda n: n*m, 2
# )

# print(duplica(2))

# FUNÇÔES COMPLEXAS NÂO SAO RECOMENDADOS ESCREVER EM LAMBDA

print(
    executa(lambda *args : sum(args, 1, 2, 3, 4))
    )