# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.


class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):          # Objtivo -> Iniciar metodo sem colocar self (instância) ao realizar chamada
        print('Hey')

    @classmethod
    def criar_com_nome_anonimo(cls, idade):            # cls -> "Molde" Self -> "Cookie"      
        print('Hey Anônimo')
        return cls("Anônimo", idade)                     # Retornará uma instância com o nome anônimo
    @classmethod
    def criar_com_50_anos(cls, nome):                  
        print('Hey 50')
        return cls(nome, 50)                    # Retornará uma instância com o nome e idade 50
    

p1 = Pessoa("Pão", 12)
p2 = Pessoa.criar_com_50_anos("Marcos")         # Uso do método 
p3 = Pessoa.criar_com_nome_anonimo(12)

print(f'{p1.nome}, {p1.idade} \n{p2.nome}, {p2.idade} \n{p3.nome}, {p3.idade}')
print(Pessoa.ano)
Pessoa.metodo_de_classe()                 #Exemplo Objetivo -> não necessitar entrar p1 ao chamar metodo_de_classe

# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.


class MinhaClasse:
    @staticmethod
    def minha_funcao():
        print('Oi :)')

# resumindo
# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:    
    def __init__(self, host='LocalHost'):
        self.host = host
        self.user = None
        self.userpassword = None

    def set_user(self, user): 
        self.user = user

    def set_user_passwrd(self, password): 
        self.userpassword = password

    @classmethod
    def new_built_user(cls, cls_method_user='admin', cls_method_passwrd='admin'):
        connection = cls()
        connection.user = cls_method_user
        connection.userpassword = cls_method_passwrd
        return connection

c1 = Connection.new_built_user()

print(vars(c1))
