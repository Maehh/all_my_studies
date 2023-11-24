# WHILE -> REPETICOES INFINITAS
# FOR -> REPETICOES FINITAS

txt = 'Hello World'

 # FOR -> PARA CADA LETRA OU NUMERO DA VAR TXT, SERÀ ADICIONADO A VARIAVEL 'LETRA'
for letra in txt :
    print(letra)


# RANGE -> range(start, stop, step)
# RANGE -> INTERVALO DE NUMREOS PRE DEFINIDOS
# RANGE NAO DEPENDE DO FOR

# ex :
numeros = range(0, 10, 1) # Valor de 0 a 9, contando de 1 em 1


for valor in numeros :
    print(valor)


# Como o for funciona

'''
    Iteravel -> str, range, etc (__Iter__) 
    Iterador -> Quem sabe como entregar um valor por vez
    Next -> Me entregue o proximo valor
    Iter -> Me entregue o seu Interador
'''
# for letra in nome 
# nome = 'luiz'
# texto = iter(nome)

# while True :
#     try :
#         letra = next(texto)
#         print(nome)
#     except StopIteration :
#             break
    

# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())