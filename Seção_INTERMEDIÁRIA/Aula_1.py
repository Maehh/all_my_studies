'''
FUNÇÔES 

def nomefuncao() :
    ...

Podem ser definidas Parâmetros para se preencher com argumentos
Por padrâo, retorna None


def nomefuncao(a, b , c) :    <- Parâmetros(a, b, c) - Ao adicionar parâmetros, eles precisam ser 
    print('A')                preenchidos por argumentros na execução

nomefuncao(1, 2, 3)          <- Argumentos ex: (1, 2, 3)

'''

def saudacao(nome='Sem nome'):
    print(f'Olá {nome} !')

saudacao()

'''
Argumentos Nomeados e Não nomeados

'''


def soma(x, y, z) :
    #  Definição
    print(f'{x + y - z=}')

print(soma(y=1, x=2, z=1))      # <- Argumento nomeado
soma(1, 2, 7)                 # <- Argumento não nomeado

print(1, 2, 3, sep='-cu-')  # <- Argumento nomeado


'''
    Valores Padrão para parâmetros de funções
    Nonetype e None
    Refatorar : Editar código
    'Um código nunca está pronto, ele sempre pode melhorar'
'''

def soma(x, y, z=None) :               
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z )
    else :
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(4, 45, 7)
soma(10, 100)


