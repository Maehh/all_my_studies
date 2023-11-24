primeiro_val = input('Digite um valor: ')
segundo_val = input('Digite outro: ')

if primeiro_val.isdigit() and segundo_val.isdigit() :
    
    if primeiro_val > segundo_val :
        print('{} é maior que {}'.format(primeiro_val, segundo_val))
    elif primeiro_val < segundo_val :
        print('{} é maior que {}'.format(segundo_val, primeiro_val))
    else :
        print(' Os valores são iguais')
else :
    print('Digite um numero')
