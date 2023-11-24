"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
A palavra global faz uma variável do escopo externo ser a mesma
no escopo interno
"""

# x = 1

# def escopo1() :
#     # global x
#     x = 10

#     def escopo2() :
#         # global x
#         x = 11
#         y = 2

#         print(x, y)

#     escopo2()
#     print(x)  

# print(x)
# escopo1()
# print(x)


'''
Retorno das funções (Return)
'''

variavel = print('LOL')
print(variavel)         # <- Retorna None 

def soma(x, y) :
    return x + y

soma1 = soma(1, 1)
soma2 = soma(2, 2)

print(soma1 + soma2)
