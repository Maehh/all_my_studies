"""
Iterando Strings com While
"""

nome = input('Escreva seu nome: ')
cont = 0
novo_nome = ''

while cont < len(nome)  :     
    novo_nome += nome[cont] + '*'
    cont += 1
print(f'*{novo_nome=}')

