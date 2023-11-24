frase = 'O python e uma linguagem se programação' \
        'multiparadigma' \
        'pytohn foi criado por Guido van Rossum'


ALFABETO = 'abcdefghijklnmopqrstuvwxyzçã'
num_letras_RECENTE = 0
num_letras_ANTERIOR = 0
letra = ''
i = 0

while i < len(ALFABETO) :
    frase = frase.lower()
    num_letras_RECENTE = frase.count(ALFABETO[i])
    

    if num_letras_ANTERIOR <= num_letras_RECENTE :
        num_letras_ANTERIOR = num_letras_RECENTE
        letra = ALFABETO[i]
    i += 1

print(num_letras_ANTERIOR)
print(letra)

# VERSÂO FOR 

'''
frase = 'O python e uma linguagem se programação' \
        'multiparadigma' \
        'pytohn foi criado por Guido van Rossum'


ALFABETO = 'abcdefghijklnmopqrstuvwxyzçã'
num_letras_RECENTE = 0
num_letras_ANTERIOR = 0
letra = ''

for i in ALFABETO :
    frase = frase.lower()
    num_letras_RECENTE = frase.count(i)
    
    if num_letras_ANTERIOR < num_letras_RECENTE :
        num_letras_ANTERIOR = num_letras_RECENTE
        letra = i
        

print(num_letras_ANTERIOR)
print(letra)

'''