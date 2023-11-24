'''
Imprecisão com float
'''


import decimal
num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')   # Tipo_3 : decimal - Quando precisar de um numero bem preciso
num3 = num1 + num2
num4 = 0.0328518171
print(f'{num3:.2f}')        # Tipo_1 : Format
print(round(num3, 1))       # Tipo_2 : Round             
print(num3)


'''
 Splits, Joints e strip
'''

frase = '     olha so olha so        ,               seu gordo     '
lista_palavras_cruas = frase.split(',')

lista_frases_organizadas = []

for i, frase in enumerate(lista_palavras_cruas) :
   lista_frases_organizadas.append(lista_palavras_cruas[i].strip()) 


print(lista_palavras_cruas)
print(lista_frases_organizadas)

frases_unidas = '-'.join('abc')
print(frases_unidas)


''' Lista dentro de Listas '''

sala = [['ovo', 'pao'], ['jorje', 'maria'], ['sua mae',]]

for i in sala :
    print(f'sala {i} :')
    for coisa in i :
        print(coisa)