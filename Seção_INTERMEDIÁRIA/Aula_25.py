#Decoradores com parametros
def decorator_factory(nome):          # Função que pega os parametros do decorador

    def funct_factory(func):                    # Função decoradora recebe função (Obrigatorio)
        print(f'decorador: {nome} \nfunção:  {func}')

        def aninhada(*args, **kwargs):      # Inner Function ou Nested Function - Executa função

            print(f'aninhada, argumentos:  {args}, {kwargs}')
            res = func(*args,**kwargs)
            final = f'{res} {nome}'
            return final
        
        return aninhada
    
    return funct_factory



@decorator_factory('4')
@decorator_factory('3')
@decorator_factory('2')
@decorator_factory('1')
def soma(x, y, **kwargs):
    return x + y

# multiplica = decorator_factory()(lambda x, y : x * y)


ten_plus_five = soma(10, 5, pao=152, jorje=20000000)
# ten_times_five = multiplica(10, 5)

print(ten_plus_five)
# print(ten_times_five)