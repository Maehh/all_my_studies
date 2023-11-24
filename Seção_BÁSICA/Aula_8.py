# Exercicios 1 - 3

'''
num_1 = input('Digite um numero inteiro: ')


if num_1.isdigit() : 
    num_1 = int(num_1) 
    par_ou_impar = num_1 % 2 == 0
    texto_par_impar = ''

    if par_ou_impar:
        texto_par_impar = 'par'
    else :
        texto_par_impar = 'impar'

    print(f'O numero é {texto_par_impar}')
else : 
    print('Digite Apenas um numero.')
'''

# Exercicio 2 - 3 

'''
diz_horas = input('Digite a hora : ')

diz_horas = int(diz_horas)

dia = 0 < diz_horas <= 11
tarde = 11 < diz_horas <= 17
noite = 17 < diz_horas <= 23

if  dia :
    print('Bom dia :)')

elif tarde :
    print('Boa tarde :|')

elif noite :
    print('Boa noite >:(')
else : 
    print(' Digita uma hora seboso')
'''

# Exercicio 3 - 3


nome = input('Digite seu nome : ')
nome_tamanho = len(nome)

def testnome():

    if nome_tamanho <= 4 :
        print('Seu nome é curto')

    elif 4 < nome_tamanho <= 6 :
        print('Seu nome é Medio')

    elif nome_tamanho > 6 :
        print('Seu nome é longo')




