                                # MÓDULOS E BIBLIOTECAS

import os # Puxar modulos e bibliotecas se usa o import

# Mostra o local que estou codando
print(os.getcwd())

# Listar todos arquivos do local que eu estou
lista_arquivos = os.listdir()
print(lista_arquivos)

# A pasta 10.1 tem arquivos dentro
lista_arquivos2 = os.listdir("10.1 - arq.txt") # Coloca o nome da pasta (aqui)
print(lista_arquivos2)

# Atividade pratica
# Colocar todos arquivos txt nas pastas de seus anos expecificos

for nome_arquivo in lista_arquivos2:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"10.1 - arq.txt/{nome_arquivo}", f"10.1 - arq.txt/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"10.1 - arq.txt/{nome_arquivo}", f"10.1 - arq.txt/23/{nome_arquivo}")
            
# Como instalar bibliotecas
# Por exemplo a request que e muito usada e não vem abaixada
# abre o terminal e coloca : pip install requests
# requests pega informações e devolve em dicionarios

import requests
# Para pegar informação externa por exemplo de um site faz
link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(link)
print(resposta)# Se der <response [200]>é porque deu certo
# Formato de requisição usado muito para code desse tipo para enviar infomaçoes para voce o Json()
dic = resposta.json()
for moeda in dic:
    conversao_moeda = dic[moeda]
    valor_moeda = conversao_moeda["bid"]
    print(moeda,"=>", valor_moeda)
