"""
Try - Tentar executar Codigo
Except - Erro detectado

"""

num_str = input('Numero')

try :
    num_float = float(num_str)
    print(f'Dobro : {num_float * 2}')
except :
    print('a')

#if num_str.isdigit() :
#    num_float = float(num_str)
#    print(f'Dobro : {num_float * 2}')
#else :
#    print('Cu')

