                                # TUPLAS

# Resultado de funções são tuplas
# Tuplas se usa () no lugar de []
# Só da para mudar se criar outra tupla com o mesmo nome/variavel com valores diferentes
tela = (60,"hz")
tela = (120, "hz")
# Tuplas são lista de valores que não poder sem modificados como as listas
# Exemplo 
lista = [1, 2, 3 ,4 ,5]
tupla = (6, 7, 8, 9, 10) 
lista[0] = 123
#tupla[0] = 456         | aqui da erro
print(lista)
#print(tupla)

# Atividade 01

# bonus 01: R$2 por venda feita
# bonus 02: 1% por valor de vendas
def calcular_bonus(lista_de_vendas):
    bonus1 = 2 * len(lista_de_vendas)
    bonus2 = 0.01 * sum(lista_de_vendas)
    return bonus1, bonus2 # AS variaveis das duas formas abaixo não precisas necessariamente ter esses nomes
                          # a forma vai saber pela sequencia um e dois não pelos nomes

vendas = [12, 34, 56 ,78]
resultado = calcular_bonus(vendas)
print(resultado)

# Duas formas de separar as tuplas 
# Forma 01
bonus1 = resultado[0]
bonus2 = resultado[1]
print("Forma 01:")
print(bonus1)
print(bonus2)

# Forma 02 sendo melhor forma
# Pode dar errado se a função retornar dois valores em um bonus só
bonus1, bonus2 = resultado # conhecido como => unpacking da tupla
print("Forma 02:")
print(bonus1)
print(bonus2)

# Poder ter tuplas dentro de listas [()]
listas_d_duplas = [(10, 10), (20, 20), (30, 30)]
for duplas in listas_d_duplas:
    print(duplas)# Retorna as duplas separadas no terminal
# Separar itens de cada dupla em mesma linha dando nomes a elas
for itens, par in listas_d_duplas:
    print(itens, "e", par)
    
# Atividade prática
def calcular_bonus(lista_de_vendas):
    bonus1 = 2 * len(lista_de_vendas)
    bonus2 = 0.01 * sum(lista_de_vendas)
    return bonus1, bonus2

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

total_bonus1 = 0
total_bonus2 = 0
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Vendedor: {vendedor}. bonus1: {bonus1}. Bonus2: {bonus2}")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2
    
print("Total de bonus1:", total_bonus1)
print("Total de bonus2:", total_bonus2)
print("Total de bonus:", total_bonus1 + total_bonus2)
