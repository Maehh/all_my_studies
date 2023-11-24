# ID da variavel
# Flag, is, is not e None


v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

condicao = True
if_detectado = None

if condicao :
    if_detectado = True
    print(True)
else :
    print(False)

print(if_detectado, if_detectado is None)
