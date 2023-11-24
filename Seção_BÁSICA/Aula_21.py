#  Desempacotamento de Dados + Tuplas

nomes = ['RRobson', 'Thiagoh', 'Mamo']
nome1, nome2, nome3 = nomes

#   OU
nome1, nome2, nome3 = ['RRobson', 'Thiagoh', 'Mamo']

#   Resto das var desempacotadas

_, nome2, *resto = ['RRobson', 'Thiagoh', 'Mamo']

print(nome2)

# Tuplas - LISTA IMUTAVEL

nomess = 'robson', 'Nomes', 'cock'

try :
    nomess[2] = 'RUR'
except :
    print('Deu nao')

# Transformar Tuplas em Listas e vice versa

jorjes = '1', '2', '3'
jorjes = list(jorjes)
print(type(jorjes))
jorjes = tuple(jorjes)
print(type(jorjes))


# ENUMERAÇÂO DE LISTAS

# pao = list(enumerate(nomess))
#                       TUPLA           TUPLA       TUPLA
#   print(pao)  -> [(0, 'robson'), (1, 'Nomes'), (2, 'cock')] 

for item in enumerate(nomess) :
    print(item)

# DESEMPACOTAMENTO COM FOR

for item in enumerate(nomess) :
    a, b = item
    print(a, b)

# OU

for indice, nome in enumerate(nomess) :
    print(indice, nome)


#   Outro Exemplo

for tupla_enumerada in enumerate(nomess) :
    print('For da Tupla: ')
    for valor in tupla_enumerada :
        print(f'\t{valor}')