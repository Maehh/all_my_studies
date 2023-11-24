# Tipos Imutaveis, Built-in, etc

# Tipos Str, Int, Bool, Float e outros são IMUTAVEIS

# Str, Int, Bool, Float São OBJETOS 
# Cada um tem seu metodo ex:

# x = 'oi'
# x = x.capitalize()
# x = x.zfill(3)
# print(x)


condicao = 'CU'
condicao2 = True
bob = 1
contador = 0



while True :
    nome = input('Digite "CU"  : ')

    if condicao == nome :
        nome *= 12
        print(nome)
        break




while condicao2 :  
    print(bob)
    bob *= (1 + 1) 
    condicao2 = bob <=15





while contador != 100 :
    contador += 1
    if (contador % 2) != 0 :
        
        continue
    print(contador)
    