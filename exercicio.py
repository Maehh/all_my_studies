lampada_a = False
lapmada_b = False

nvezes = int(input('Numero de vezes que o interruptor será apertado: '))
n_sequencia_entrada =('Sequencia de interruptores')
nsequencia = {1, 2}


for i in range(nvezes):
    if lampada_a == False:
        lampada_a = True
        continue 
    lampada_a = False

resultado = (lampada_a == True)


print(resultado)
