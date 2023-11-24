# Escopo da classe e de métodos da classe
import os

class Animal:
    #nome = 'leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'Valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome}, Está comendo, {alimento}'
    
    def executar(self, *args, **Kwargs):
        return self.comendo(*args, **Kwargs)
    

leao = Animal('Leão')
print(leao.nome)
print(leao.executar('Ovo Frito, CU, Sochicha'))


os.system('cls')
# Mantendo Estados dentro da classe

class Camera:

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando..')
            return
        
        print(f'{self.nome}, está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando..')
            return
        
        print(f'{self.nome}, Parou de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome}, Não pode fotografar filmando')
            return
        print(f'{self.nome} Está Fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c2.fotografar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print(c1.filmando)
print(c2.filmando)
