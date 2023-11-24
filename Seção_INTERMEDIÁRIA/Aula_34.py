'''
Ambientes virtuais em Python (venv)
Um ambiente virtual carrega toda a sua instalação
do Python para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do
ambiente virtual será usada.
venv é o módulo que vamos usar para
criar ambientes virtuais.
Você pode dar o nome que preferir para um
ambiente virtual, mas os mais comuns são:
venv env .venv .env

comandos pip:
    pip freeze
    pip install [nome package] 
    pip install [nome package] --upgrade
    pip intall pip --upgrade

'''
import os 

# ARQUIVOS
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


archive_path = 'E:\\Trabalhos\\Cursos_python\\Pasta_arquivo\\'
archive_path += 'aula_texto.txt'

# folder = open('texto2.txt', 'w')

# folder.close()


# with open(archive_path, "w+") as folder:
#     ...
#     folder.write('DAAAAAAAAANNM\n')
#     folder.write('DAAAAAAAAANNM\n')
    

#     folder.write("GOD")
#     folder.writelines(('*' * 20, '\n'))
#     folder.writelines(('OHHHHHHHH \n', 'MYGAAREHHHHHH'))

#     folder.seek(0,0)
#     # print(folder.read())
#     print(folder.readline())
#     print(folder.readline())
#     print(folder.readline().strip())
#     print(folder.readline().strip())

#     for linha in folder.readlines():
#         print(linha.strip())c

# with open(archive_path, "r") as folder:
#     print(folder.read())


archive_path2 = "Aula_texto2.txt"
with open(archive_path2, "w", encoding='utf8') as folder:
    folder.write("AÇUCARÂOO")


# os.remove(archive_path)
# os.unlink(archive_path)
# os.rename(archive_path2, "CUUUUUUUUU")

