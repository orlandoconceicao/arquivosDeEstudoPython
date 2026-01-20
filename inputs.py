                                #INPUTS

#faturamento = 1000    # Forma erradda de fazer
#custo = 200 

faturamento = input("Preencha o faturamento(Apenas com números)")
faturamento = faturamento.replace("R$", "").replace(",", ".")
faturamento = float(faturamento) 
custo = 200

lucro = faturamento - custo 
print(lucro)

# Pode fazer também 

vendas_dia_01 = float(input("Faturamento dia 01: "))
vendas_dia_02 = float(input("Faturamento dia 02: "))

print(vendas_dia_01 + vendas_dia_02)

                                # Atividade
                                
#Peça ao usuário:
    #Seu nome
    #Sua idade
    #Sua altura (em metros)
#Mostre na tela
    # Uma frase descrevendo a pessoa
    
nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
altura = float(input("digite sua altura(Apenas números)"))

print(f"Meu nome é {nome}, tenho {idade} anos e minha altura é de {altura}")

