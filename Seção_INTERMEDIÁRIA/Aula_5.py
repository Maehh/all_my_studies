'''
Higher Order functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns 
(strings, inteiros, etc...)
'''

def saudacao(msg, nome, *_) :
    return f'{msg}, {nome} !!!!'


def execute(funcao, *args):
    return funcao(*args)


v = execute(saudacao, "DOM BIA", "MARKOKOS", "PNCCCC","AHAHAHAHA")

print(v)



'''
Closure e funções que criam outras funções

'''

def criarsaudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'  
    return saudar


falar_bom_dia = criarsaudacao('bom dia')
falar_BOM_DIOO = criarsaudacao('bom DIO')

print(falar_bom_dia('FOF'))
print(falar_BOM_DIOO('FEF'))


for nome in ['Marlos', 'PAPP', 'COCK']:
    print(falar_bom_dia(nome))
    print(falar_BOM_DIOO(nome))
