# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Cachorro:
    nome_cientifico = 'Canis lupus familiaris'
    ano_atual = 2023

    def __init__(self, nome, idade, raca=None, genero=None):
        self.nome = nome     
        self.idade = idade  
        self.raca = raca    
        self.genero = genero

    def get_idade_cachorro(self):
        return Cachorro.ano_atual - self.idade

    def registrar_dog(self, acrchive_name):
        with open(f'{acrchive_name}.json', 'w+', encoding='utf8') as file:
            json.dump(vars(self), file, ensure_ascii=False)


def importar_dog(archive_name_load):
    with open(f'{archive_name_load}', 'r') as file:
        return Cachorro(**json.load(file))

c1 = Cachorro('Marcos', 4, 'Golden_retriever')
c2 = Cachorro('Apolle', 2, 'Salsicha', 'F')
c1.registrar_dog('Cachorro_1')
c2.registrar_dog('Cachorro_2')
c3 = importar_dog('Cachorro_1.json')
c4 = importar_dog('Cachorro_2.json')

# c5 = Cachorro('Mel', 5, 'Caramelho', 'F')
# c5.registrar_dog('Informações sobre mel')
# mel = importar_dog('Informações sobre mel.json')

# print(vars(mel))




