# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

'''my code
todo = []
undo = []

def commands(entry):

    entry = entry.lower()
    if entry == "desfazer":
        return True
    if entry == "refazer":
        return False
    if entry == "mostrar_lista":
        return "A"
    return None

while True:
    user = input("Commandos: [Desfazer], [Refazer], [Mostrar_lista] \n")
    
    user_check = commands(user)

    if user_check == None:
        todo.append(user)
        continue
    elif user_check == "A" :
        print(*todo, sep="\n")
        continue
    elif user_check and todo:
        undo.append(todo.pop())
        continue
    elif not user_check and undo:
        todo.append(undo.pop())
        continue
   

    else: 
        print('Commando não processado')
'''
        


todo = []
undo = []

def list_check(tasks):
    if not tasks:
        print('Não há nada da lista')
        return
    
    print('Lista:', *tasks, sep='\n')

def undo_list(tasks):
    if not tasks:
        print('Não há nada para desfazer')
        return       
    undo.append(todo.pop())

def redo_list(tasks):
    if not tasks:
        print('Não há nada para refazer')
        return
        
    todo.append(undo.pop())
def user_content_check(usrinput):
    if not usrinput:
        print('Não há nada para ser colocado')
        return

    todo.append(usrinput)


def export_to_json(list_to_export):
    with open("List_Json_file.json", 'w', encoding="utf8") as file:
        json.dump(list_to_export, file, ensure_ascii=False, indent=2)

while True:
    user = input("Commandos: [Desfazer], [Refazer], [Listar], [Exportar] \n")
           

    commandlist = {
        'desfazer' : lambda : undo_list(todo), 
        'refazer' : lambda : redo_list(undo),
        'listar' : lambda : list_check(todo),
        'exportar' : lambda : export_to_json(todo),
        }
    if user in commandlist:
        commandlist[user]()
    else:
        user_content_check(user)



    # if user.lower() == "desfazer":
    #     undo_list(todo)
    #     continue
    # elif user.lower() == "refazer":
    #     redo_list(undo)
    #     continue
    # elif user.lower() == "listar":
    #     list_check(todo)
    #     continue
    # else:
    #     user_content_check(user)
    #     continue