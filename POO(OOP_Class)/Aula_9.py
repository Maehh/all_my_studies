# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

'''
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome 

    def escrever(self):
        return f'{self.nome} está escrevendo'
    

escritor = Escritor('Marcos')
caneta = FerramentaDeEscrever('Bic')
teclado = FerramentaDeEscrever('Multilaser')
escritor.ferramenta = teclado

print(caneta.escrever())
print(escritor.ferramenta.escrever())'''

# O que está acontecendo no código:

'''
1. A classe "Escritor" tem um atributo chamado "_ferramenta"
2. A classe "FerramentaDeEscrever" define uma instância que representa uma ferramenta com um método "escrever"
3. É definido a instância "Caneta" que pode ser definida ao atributo "_ferramenta" da classe
"Escritor", permitindo o uso do método "escrever" dentro do atributo "_ferramenta"
4. Sendo assim, você pode chamar o atributo "escritor.ferramenta" e executar o método que existe
dentro do mesmo, ou seja, escritor.ferramenta.escrever()
5. Isso seria como definir uma função a uma variável, sendo assim necessário apenas executa-lá

6. *Relembrando que esta menção de funções são apenas para referência, o conceito acima está explicando
uma relação de associação entre duas classes simples.

'''


# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).


class Carrinho:

    def __init__(self) :
        self._produtos = []

    def inserir_produtos(self, *info_produto):
        # self._produtos.extend(info_produto)
        # self._produtos += info_produto
        for produto in info_produto:
            self._produtos.append(produto)

    def total(self):
        print(sum([p.preco for p in self._produtos]))
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho_de_compras = Carrinho()
prod1, prod2 = Produto('Maçã', 1.25), Produto('Banana', 0.50)
carrinho_de_compras.inserir_produtos(prod1, prod2)

carrinho_de_compras.listar_produtos()
carrinho_de_compras.total()


# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome 
        self.enderecos = []

    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))        #<--- É criado uma instância dentro da Classe "Cliente"
    
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco) 

    def listar_cliente_info(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando:', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando:', self.rua, self.numero)


cli1 = Cliente("Maria")
cli1.inserir_endereco('Avenida 0001', 12)
cli1.inserir_endereco('Avenida 0025', 245)
cli1.listar_cliente_info()
ender = Endereco('Rua 0251', 500)
cli1.inserir_endereco_externo(ender)

# del cli1

print('----------------FIM CÓDIGO---------------')

        


# RECAPTULANDO:
# SE UM OBJETO SE COMUNICA COM OUTRO = ASSOCIAÇÃO SIMPLES
# SE UM OBJEDO PRECISA DO OUTRO PARA FUNCIONAR = AGREGAÇÃO 
# SE UM OBJETO GERENCIA -> OUTRO CICLO DE VIDA DE OUTRO OBJETO = COMPOSIÇÃO