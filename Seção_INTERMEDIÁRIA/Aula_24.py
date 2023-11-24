# Variaveis livres + nonlocals (locals, globals)

print(globals())
def fora(x):
    a = x

    def dentro():
        print(locals)
        # print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(11)

print(dentro1())
print(dentro2())

def concatenate(string_ini):
    final_val = string_ini

    def intern(concarternated_val=''):
        nonlocal final_val
        final_val += concarternated_val
        return final_val
    return intern

c = concatenate('a')
print(c('b')) 
print(c('c')) 
print(c('d')) 


# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)


def funct_creator(func):     # 3 Função decoradora recebe string_invert e Cria função decorada 

    def intern(*args,**kwargs):     # 4 - Função decorada recebe argumentos ('jorje')   

        for arg in args:               # 5 - para cada arg (letra) em 'jorje' checa se é int via função is_string
            is_string(arg)              
        result = func(*args, **kwargs)  # 6 - junta tudo em result, funct como string_invert e *args/**kwargs como
                                        # argumentos (string_invert('jorje'))

        return result               # FIM Função decorada e retorno da função
    return intern

@funct_creator                  # 2 - função string_invert é jogada para dentro da função funct_creator
def string_invert(string):          
    print(string_invert.__name__)
    return string[::-1]

def is_string(param): 
    if not isinstance(param, str):
        raise TypeError('param must be String')


# num_check_string = funct_create(string_invert)


inver = string_invert(123)      # 1 - Chama Função string_invert com o argumento 'jorje' 
print(inver)                        # 7 - resultado da operação.



