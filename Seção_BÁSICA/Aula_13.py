# While else
string = 'Marqu inhos'
i = 0

while i < len(string) :
    letra = string[i]

    if letra == ' ' :
        break
    print(letra)

    i += 1
    
else :
    print('SIM')
print('NAO')
