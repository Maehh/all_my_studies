'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)

'''
# # Desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y) :
#     return x + y


def soma(*args):
    total = 0
    for i in args :
        total += i
    return total


x = soma(1, 2, 3, 4, 5, 6)

y = soma(1,2,5,16,8,1,3,321,65,1)

numeros = 1,2,5,16,8,1,3,321,65,1

print(*numeros)

z = soma(*numeros)

print(z)
