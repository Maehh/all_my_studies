# # try, except, else e finally
# a = 18
# b = 0
# print('linha 1')
# c = a/b

# try:
#     a = 18
#     b = 0
#     print('linha 1'[10000])
#     # print(b[0])
#     c = a/b
# except ZeroDivisionError:
#     print('Divididididi')
# except NameError:
#     print('ERRARRAR')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexErro')
#     print('MSG: ', error)
#     print('Nome: ', error.__class__.__name__)
# except Exception:
#     print('Erro desconheeheehenehene')


# try :
#     print('JORjer')
#     # 8/0
# except ZeroDivisionError:
#     print('NÂO')
# else:
#     print(':DDDDD')
# finally:
#     print('AAAAAAAAAAAAA')


# raise - Lançando exeções

print(123)
# raise ValueError('NOOOOOOOO')
print(456)

def checar_erro(e):
    if e == 0:
        raise ZeroDivisionError('MERMAO')
    
def deve_SEEEr(f):

    if not isinstance(f, (float, int)):
        raise TypeError(f'Erro ERRR {f} ta escrito errado')
    
    return True

def divide(n, m):
    checar_erro(m)
    deve_SEEEr(n)
    deve_SEEEr(m)
    return int(n/m)

print(divide(8, 2))
