# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def previous_val_chck(val, list_sample):
    for val_check in list_sample:
        if val in val_check:
            return True
    return False

def zipper(list_1, list_2, *args, **kwargs):
    result = []
    if len(list_1) > len(list_2):
        for a in list_1:
            for b in list_2:
                if previous_val_chck(a, result):
                    continue
                if previous_val_chck(b, result):
                    continue
                result.append((a , b))
                
        return result
    
    else:
        for a in list_2:
            for b in list_1:
                if previous_val_chck(a, result):
                    continue
                if previous_val_chck(b, result):
                    continue
                result.append((b , a))

        return result       
print(zipper(lista1, lista2))


# Solução + Aula

from itertools import zip_longest

def zipper(list_1, list_2):
    max_interval = min(len(list_1), len(list_2))
    return [(list_1[i], list_2[i]) for i in range(max_interval)]

print(zipper(lista1, lista2))
print(list(zip(lista1, lista2)))
print(list(zip_longest(lista1, lista2)))
