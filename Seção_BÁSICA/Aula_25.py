# Empacotamento de desempacotamento em chamadas de FUNÇÔES
sala = [['ovo', 'pao'], ['jorje', 'maria'], ['sua mae',]]

joj = ['CU', 'cuason',1 , 2, 3, 'cuaccons' ]

aaaa = 'kjasfjkjjjasjkjkaskjdkjasdkjaskaa'
a, b, *_, c = joj

# for nome in joj :
#     print(nome, end=' ', sep=' ')

'''
end='' Coloca algum caractere no final de cada elemento
sep='' Coloca alguma separacao em cada elemento
'''
# print(*sala, end='', sep='\n')



'''
Operação Tenaria (Condicional em uma linha)
<valor> if <condicao>  else <outro valor>
'''



condicao = 10 == 11
mam = 'Valor' if condicao else 'Outro valor'
print(mam)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
