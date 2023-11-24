import json

dicionario = {

  "nome": "Luiz Otávio 2",
  "sobrenome": "Miranda",
  "enderecos": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2","numero": 55}
  ],

  "altura": 1.8,
  "numeros_preferidos": [2, 4, 6, 8, 10],
  "dev": True,
  "nada": None
}

with open('Aula_35_Json.json', 'w', encoding='utf-8') as file :
    json.dump(dicionario, file, ensure_ascii=False,
              indent=2)
    

with open('Aula_35_Json.json', 'r', encoding='utf-8') as file :

    file_json_convert = json.load(file)
    
    if file_json_convert['dev'] == True:
        print('dev True')
    else:
        print('dev False')