import os

compras = []

while True  :
    select = None

    opc = input('\t =-Lista de Compras-= \n Escolha umas das Opções [A]pagar, [E]screver, [L]istar [X] Sair \n')
    os.system('cls')

    if opc.lower() == 'e' :
        
        select = input('\n Digite algo que queira adicionar na lista:')
        compras.append(select)
        os.system('cls')
        print(f'Você adicionou "{select}" à sua lista.')

    elif opc.lower() == 'a' :

        for num, item in enumerate(compras) :
            print(f'{num}-{item}')

        select = input('Escolha o indice para apagar apagar na lista:')
        os.system('cls')

        try :
            select = int(select)
            del compras[select]
        except : print('Indice Incorreto ou Lista Vazia.')


    elif opc.lower() == 'l' :
        if compras != [] :
            for num, item in enumerate(compras) :
                print(f'{num}-{item}')
        else : print('Nada para listar.')

    elif opc.lower() == 'x' :
        print('FIM')
        break




    # while True :
    #     compras.append(input('Digite algo que queira adicionar na lista:'))
        
    #     if 'sair' in compras[-1].lower() :
    #         print('voce saiu da lista.')
    #         break