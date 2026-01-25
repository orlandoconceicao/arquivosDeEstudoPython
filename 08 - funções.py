                                # FUNÇÃO
                                
# O codigo tem que ter uma fução para cada objetivo

# Começar com um (def) para definir uma função
# def variavel(lista)
# e no final return
# def - adicionar variavel - ()oque precisa receber para calcular

# Pratica 01
# Produtos de até 1000 pagam 10%. Produtos acima de 1000 pagam 15% de imposto
# Usado para executar a função varias vezes

lista_precos = [1500, 1000, 800, 2000]

def calcular_imposto(lista_precos):
    imposto_total = 0
    for preco in lista_precos:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

imposto_lista1 = calcular_imposto(lista_precos)
print(f"Imposto da lista 01 é de: {imposto_lista1}")

lista2_precos = [1000, 2000, 4000, 3000, 7000, 6000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(f"Imposto da lista 02 é de: {imposto_lista2}")

# Usando funções para casos especificos com o exemplo anterior
lista_precos = [1500, 1000, 800, 2000]

def definir_taxa_de_imposto(preco):
    if preco > 1500:
        taxa = 0.20
    elif preco > 1000: 
        taxa = 0.15
    else:
        taxa = 0.1
    return taxa # Esse return taxa faz que a variavel taxa exista fora da função e não sendo so local

def calcular_imposto(lista_precos):
    imposto_total = 0
    for preco in lista_precos:
        taxa = definir_taxa_de_imposto(preco)# Si a taxa for atualizar muda a função definir_taxa_de_imposto
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

imposto_lista1 = calcular_imposto(lista_precos)
print(f"Imposto da lista 03 é de: {imposto_lista1}")

# Função sem return
# Usado para fazer uma tarefa expecifica
def meu_nome_e_idade():
    print("Meu nome e Orlando e tenho 17 anos")
    print("Faço 18 anos, nesse mesmo ano que estamos")
meu_nome_e_idade()