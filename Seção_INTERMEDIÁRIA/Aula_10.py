# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1= set() <- Vazio
# s1 = {'luiz', 1, 2, 3} # <- Com dados
# print(s1)



# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 2, 3, 1, 2, 3, 2, 3, 1, 2, 3, 2, 3]
# s1 = set(l1)
# print(s1)
# print(3 in s1)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('AAAAAAA')
# s1.update(('Olá Mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá Mundo')
# print(s1)

# Operadores úteis:
# união "|" união (union) - Une
# intersecção "&" (intersection) - Itens presentes em ambos
# diferença "-" Itens presentes APENAS no primeiro set 
# diferença simétrica "^" - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2

s3 = s1 & s2

s3 = s1 - s2
s3 = s2 - s1

s3 = s1 ^ s2

print(s3)

# Exemplo de Uso OTIMIZAÇÂO AULA EXERCICIO 17

letras = set()

while True :
    letra = input('Digite :')
    letras.add(letra)

    print(letras)