import os 

PALAVRA_SECRETA = "Bolinho"
print('Bem vindo ao Caça Palavras')
letras_ditas = ''
tentativas = 0


while True :

    resposta = input('Digite uma letra : ')

    if resposta == '0' :
        print('Fim')
        break

    if len(resposta) > 1 :
        print('Digite Uma letra')
        continue

    if resposta in PALAVRA_SECRETA :
        letras_ditas += resposta

    palavra_formatada = ''
    
    for letra_secreta in PALAVRA_SECRETA :
        if letra_secreta in letras_ditas :

            palavra_formatada += letra_secreta

        else : palavra_formatada += '*'
    tentativas += 1


    print(f"{palavra_formatada}, {tentativas=}")
    

    if palavra_formatada == PALAVRA_SECRETA :
        os.system('cls')
        print(f'Parabéns, a palavra era {PALAVRA_SECRETA} \n FIM DE JOGO')
        palavra_formatada = ''
        letras_ditas = ''
        tentativas = 0
        continue

# for i in PALAVRA_SECRETA :

#     if (resposta == i) and (resposta not in palavra_formatada) :
#         palavra_formatada += resposta
#     else : 
#         palavra_formatada += '*'


# palavra = "Robson"
# palavraimagem = '#' *len(palavra)
# palavraformatada = ''
# x = input('teste')

# for i in palavra :

#     if x == i :
#         palavraformatada += x
#     else : 
#         palavraformatada += '#'

# print(palavraformatada)