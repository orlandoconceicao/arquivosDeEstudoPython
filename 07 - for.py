                                # FOR
                                
# for i in range()
# for cria um laço de repetição.
# i é a variável que muda a cada repetição.
# in indica que i percorre valores dentro de algo.
# range() gera uma sequência de números para o loop.
for i in range(5):
    print("Executar 5 vezes")
    
lista_precos = [1000, 2000, 3000, 4000]

taxa_imposto = 0.1

for preco in lista_precos:
    imposto = preco * taxa_imposto
    #print(f"O preço do produto e de {preco}, com o imposto de {imposto}")
    

# Atividade 01
# Produtos de até 1000 pagam 10%. Produtos acima de 1000 pagam 15% de imposto
for preco in lista_precos:
    if preco > 1000:
        taxa = .15
    else:
        taxa = .1
    imposto = taxa * preco
    #print(f"O preço do produto e de {preco}, com imposto de {imposto}")
    
# Atividade 02
# mesma regra de imposto da atividade um mas quero conseguir calcular o total de imposto somado de todos os produtos
total_imposto = 0
for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else: taxa = 0.1
    imposto = taxa * preco 
    total_imposto = total_imposto + imposto # pode fazer assim tambem total_imposto += imposto
#print("Todal de imposto", total_imposto)

# Atividade 03
# Calcular percentual de crescimento => 500 / 100 - 1
vendas_25 = {"jan": 100, "fev": 200, "mar": 300}
vendas_26 = {"jan": 500, "fev": 600, "mar": 700}

for mes in vendas_26:
    valor_25 = vendas_25[mes]
    valor_26 = vendas_26[mes]
    crescimento = valor_26 / valor_25 - 1
print(f"no mês de {mes} o crescimento foi de {crescimento:.1%}")
    