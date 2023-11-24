# Exercício - Adiando execução de funções
def soma(x):
    def acao(y):
        return x + y
    return acao


def multiplica(x):
    def acao(y):
        return x * y
    return acao


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_dez(2))


