                                # CONDICIONAIS
                                
#if comparacao/condição:
    # O que eu quero que aconteça se essa condição for verdadeira
    # Tem que ter o tab aqui 
#else:
    # O que eu quero que aconteça se essa condição for falsa
    # Pode ter varias linhas no if e no else
# So pode ter else se tiver if antes
# Para fechar if else e so começar outra coisa sem o tab

# Exemplo 01

faturamento = 1000
custo = 2000

lucro = faturamento - custo

if lucro >= 0:
    print("Deu lucro de:", lucro)
else: 
    print("Deu prejuizo de", lucro)
    
print("Acabou")

# exemplo 02

produtos = ["arroz", "feijão", "batata"]
novo_produto = input("Digite o nome do produto:")

if novo_produto in produtos:
    print("Esse produto ja existe")
else: 
    print(f"{novo_produto} adicionado com sucesso")
    produtos.append(novo_produto)
print(produtos)

# Exemplo 03

vendas = 200

if vendas >= 15000:
    bonus = 500
else:
    if vendas >= 5000:
        bonus = 100
    else:
        bonus = 0
        
print(f"O funcionário ganhou {bonus} de bônus")

# Usando elif

vendas2 = 20000

if vendas2 >= 15000:
    bonus2 = 500
elif vendas2 >= 5000:
    bonus2 = 100
else: 
    bonus2 = 0
    
print(f"O funcionário de vendas2 ganhou {bonus2} de bônus")

# Exemplo 03

vendas_empresa = 200_000
meta_empresa = 100_000
vendas_funcionario = 17000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus3 = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus3 = 100
else:
    bonus3 = 0
print(f"O funcinário ganhou {bonus3} de bônus")

    


    

