# Formatação de arquivo JSON
    # Objetivo de preparar os arquivos para tranformação dos dados em ferramenta de ETL
import os 
import json
# 1) Obter os nomes dos arquivos JSON na pasta atual de forma ordenada (Abrir pasta: CTRL+K CTRL+O)
file_path = "."
for root, dirs, files in os.walk(file_path):        ## Varredura dos arquivos no diretório especificado
    file_names = (files)                            ## Salva os nomes dos arquivos em uma lista
for i in range(0, len(file_names)):                 ## Varredura de cada elemento da lista
    file_names[i] = file_names[i].strip(".json")    ## Remove a extensão ".json"
    file_names[i] = int(file_names[i])              ## Converte em numero inteiro (Fim do loop)
file_names.sort()                                   ## Reorganiza os nomes numericamente em ordem crescente
# 2) Escrever em cada arquivo JSON o seu proprio nome (ID dos deputados) e formatar o JSON final
for i in range(0, len(file_names)):                 ## Varredura de cada elemento da lista de nomes
    json_path = ('C:/PENTAHO/Workspace/Deputados/Despesas/'+str(file_names[i])+'.json')
    json_file = open(json_path, 'r')  
    json_data = json.load(json_file)
    json_data = json_data['dados']
    for j in range(0, len(json_data)):
        json_data[j] = json_data[j]['valorDocumento']
    json_final = [('id', file_names[i]), ('valorTotal', sum(json_data))]
    json_final = dict(json_final)
    json_object = json.dumps(json_final, indent=4)
    json_file.close()
    json_file = open(json_path, 'w') 
    json_file.write(json_object) 
    json_file.close()
    # Escrever todos os dados em um arquivo JSON final
    if i == 0:
        json_file = open('C:\PENTAHO\Workspace\Deputados\DespesasTotais.json', 'a')
        json_file.write('{ "dados": ['+json_object+', ')
        json_file.close()   
    elif i != (len(file_names)-1):
        json_file = open('C:\PENTAHO\Workspace\Deputados\DespesasTotais.json', 'a')
        json_file.write(json_object+', ')
        json_file.close()
    else:
        json_file = open('C:\PENTAHO\Workspace\Deputados\DespesasTotais.json', 'a')
        json_file.write(json_object+']}')
        json_file.close()