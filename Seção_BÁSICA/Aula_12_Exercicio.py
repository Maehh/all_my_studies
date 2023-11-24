# CALCULADORA WHILE

while True : 
    
    OPERADORES = '+-/*'
    val1 = 0
    val2 = 0

    entrada_saida = input('Bem vindo a calculadora \n Digite [C]ontinuar ou [S]air \n ').lower()
    leitor1 = entrada_saida.startswith('s') or entrada_saida == 'sair'
    leitor2 = entrada_saida.startswith('c') or entrada_saida == 'continuar'

    
    if  leitor1 :
        print('Programa Terminado.')
        break

    elif leitor2 : 
 
        val1 = input('Digite o primeiro valor : \n')
        val2 = input('Digite o segundo valor : \n')
        operador = input('Digite a operação a ser feita [*], [+], [-], [/] \n')

        try :
            val1 = float(val1)
            val2 = float(val2)
            valido = True
        except :
            valido = None
        
        if valido == None :
            print('Um dos dois valores estão invalidos.')
            continue

        operador_leitor = (operador not in OPERADORES) or len(operador) > 1

        if operador_leitor :
            print('[OPERAÇÂO INVALIDA]')
            continue
        print('Operação abaixo :')
        if operador == '+' :
            print(f'{val1} + {val2}=', val1 + val2 )
        elif operador == '-' :
            print(f'{val1} - {val2}=', val1 - val2 )
        elif operador == '*' :
            print(f'{val1} * {val2}=', val1 * val2 )
            
        elif operador == '/' :
            if val2 != 0 :
                print(f'{val1} / {val2}=', val1 / val2 )
            else :
                print('Valor nao pode ser divido por ZERO')
                continue

        else :
            print('Nao deveria estar aqui')
            break
    else :
        print('[ENTRADA INCORRETA]')
        continue
