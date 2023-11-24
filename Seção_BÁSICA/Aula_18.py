"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""

# txt = 'ABCDE'
# lista = [123, 'cu', True, 'Jorge', 1.25, ['cu', 25, 10]]
# lista.append(200)
# ultimo_valor = lista.pop()
# lista.append(2543)
# lista.append('AHAHA')

# del lista[0]

# lista.insert(4, '7')

# print(f'{ultimo_valor=} \n', lista)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b 
lista_a.extend(lista_b)  # <- Não Retorna nada de volta (None)
print(lista_a)