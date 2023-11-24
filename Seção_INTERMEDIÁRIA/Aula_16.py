# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

# dir, hasattr e getattr em Python

string = 'Luiz'
metodo = 'upper'

# print(string)
if hasattr(string, metodo):
    print('Existe UPPERPERPEPREPrjnrjnujasrdousdjsfdkjasdd')
    print(getattr(string, metodo))


#  Mais sobre O __iter__ e __next__


# Iterator é uma CLASSE - Com dois métodos (__iter__ e __next__)

iterable = ['eu', 'tenho', 'cu']
iterator = iter(iterable)  # Tem o __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator expression, iterables, e Iteratiors em python 
import sys

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))

print(sys.getsizeof(generator))

for n in generator :
    if n > 500:
        break
    print(n)







