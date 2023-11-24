# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 50/2?',
        'Opções': ['2', '80', '50', '25'],
        'Resposta': '25',
    },
]

# Funções
def select_perguntas(indice_list) :
    tupla_perg = perguntas[indice_list]['Pergunta'], perguntas[indice_list]['Opções'], perguntas[indice_list]['Resposta']
    return list(tupla_perg)

def calculo_perguntas(usuario, pergunta) :   
    if usuario in pergunta[1]:
        if usuario in pergunta[2] :
            return True
        return False
    return None


#Inicio Código
acertos = 0
for i in range(len(perguntas)):

    pergunta = select_perguntas(i)
    
    print(f'Pergunta : {pergunta[0]} \n Opções :')

    for cont, opc in enumerate(pergunta[1]) :
        print(f'{cont}) {opc}')
    usuario = input()

    os.system('cls')

    if calculo_perguntas(usuario, pergunta) :
        print('Correto!')
        acertos += 1
    elif calculo_perguntas(usuario, pergunta) != None :
        print(f'INCORRETO! Resposta : {pergunta[2]}')

    else :
        print('Item não está entre as opções')

print(f'{acertos=}')
    