nome = input('Qual o seu nome :')  #ok
idade = input('Qual a sua idade :') #ok

if nome and idade :    #ok 
    print(f'Seu nome é : {nome}')   #ok 
    print(f'Seu nome invertido é : {nome[::-1]}') #ok 

    if ' ' in nome:   #ok 
        print('Seu nome contém espaços')
    else :  #ok 
        print('Seu nome NÂO contém espaços')
    print(f'Seu nome contem {len(nome)} letras')    #ok 
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')   #ok 
else :
    print('Descule, voce deixou nomes vazios')  #ok 
    