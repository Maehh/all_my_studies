#   Copiar um valor para outro 

lista_a = ['ovo', 'ovo', 'ovo']
lista_b = lista_a.copy()

lista_a.insert(0, 'OVOH')
print(lista_b)

#   For in tipo list

for letra in lista_a :
    print(letra, type(letra))
    