# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade' : 12,
    'altura' : 200
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_args_nomeados(*args, **kwargs):
    print(kwargs)

mostro_args_nomeados(nome='AAA', qlq=123)