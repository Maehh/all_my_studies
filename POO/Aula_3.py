# __dict__ e vars para atributos de uma sintância


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 100


    def get_ano_nascimento(self):
      #  return self.ano_atual - self.idade
        return Pessoa.ano_atual - self.idade
    

dados = {'nome': 'João', 'idade' : 12}
p1 = Pessoa(**dados)
p2 = Pessoa('Maria', 15)

# Pessoa.ano_atual = 0

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# p1.__dict__['Outra'] = 'Coisa'
# p1.__dict__['Nome'] = 'Cus'
# del p1.__dict__['nome']
# p1.nome = 'Oi'
# del p1.nome
# print(p1.nome)
# print(p1.__dict__)

print(vars(p1))