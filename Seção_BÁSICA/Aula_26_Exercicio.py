import random 
import sys

CPF_Cru = input('Digite um CPF para encontrar os dois digitos: ')
CPF_refinado = ''
soma_cpf = 0
calculo_cpf1 = 0
contador_reg1 = 0
char_repetido = ''

# for num in CPF_Cru :
#     if num.isdigit() :
#         CPF_refinado += f'{num}'                       # CPF TESTES 761.747.530-69 / 948.576.510-09 / 184.510.530-33

CPF_refinado = CPF_Cru.replace('.', '').replace('-', '').replace(' ', '')

validacao1 = len(CPF_refinado) == 11

primeiros9_Digitos = CPF_refinado[:9]

validacao2 = CPF_refinado[0] * len(CPF_refinado) != CPF_refinado

if validacao1 and validacao2:
    contador_reg1 = 10
    for digito1 in CPF_refinado[:9] :
        soma_cpf += int(digito1) * contador_reg1
        contador_reg1 -= 1

    calculo_cpf1 = (soma_cpf * 10) % 11

    soma_cpf = 0

    contador_reg2 = 11
    for digito1 in CPF_refinado[:10] :
        soma_cpf += int(digito1) * contador_reg2
        contador_reg2 -= 1

    calculo_cpf2 = (soma_cpf * 10) % 11
    

    print(f'Primeiro DIgito : {0}') if calculo_cpf1 > 9 else print(f'Primeiro DIgito : {calculo_cpf1}')
    print(f'Segundo DIgito : {0}') if calculo_cpf2 > 9 else print(f'Segundo DIgito : {calculo_cpf2}')

    cpf_gerado = f'{primeiros9_Digitos}{calculo_cpf1}{calculo_cpf2}'

    if cpf_gerado == CPF_refinado :         
        print('CPF valido')
    else :
        print('CPF invalido')

