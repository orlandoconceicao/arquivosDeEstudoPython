                                # LISTAS
                                
# Listas são feitas entre colchetes[]
# Lista de números não precisa de aspas
lista_vendas = [10, 30, 50, 20, 40]

# Para puxar o ultimo da lista utiliza [-1] => que conta de traz para frente
# começa a contar do 0 
# Selecionar item da lista
print("Posição da lista 02:", lista_vendas[2])

# Mostrar o tamanho da lista

# Len vem de length => comprimento/tamanho
# Não e interessante usar mesma variavel varias vezes em lugares diferente =
# Crie sempre que for usar mais de uma vez
print("Quantas vendas:", len(lista_vendas))
quantas_vendas = len(lista_vendas)
print("Quantas vendas:", quantas_vendas)

# Somar vendas se utiliza sum()
total_vendas = sum(lista_vendas)# Forma 01
print("Total de vendas:", total_vendas) # Forma 01 armazena na variavel

print("Soma das vendas:", sum(lista_vendas))# Forma 02

# Máximo, minimo e media
print("Maximo de vendas:", max(lista_vendas))
print("Minimo de vendas:", min(lista_vendas))
print("Media de vendas:", total_vendas / quantas_vendas)

# Encotrar um elemento se usa in => existe
lista_produtos = ["arroz", "feijão", "picanha", "alface", "tomate"]
# Não pode escrever errado / importante padronizar textos
print("arroz" in lista_produtos)

# Buscar posição do elemento
posicao = lista_produtos.index("alface")
print("Pocição do alface:", posicao)

# Pegar tudo depois de algum produto
pedaco_lista = lista_produtos[posicao: ]
print(pedaco_lista)

# Editar item dentro da lista
lista_precos = [1000, 2000, 3000, 4000]
novo_preco = lista_precos[0] * 1.1 # => 10%
lista_precos[0] = novo_preco
print(lista_precos)

# Remover intem da lista tipo 01 = .remove() você passa o nome para remover
# .remove() não precisa fazer x = x.remove porque ele muda direto na fonte so o x.remove ja basta
lista_produtos.remove("picanha")
print(lista_produtos)

# Remover item da lista tipo 02 = .pop() você passa a posição do item para remover
item_removido = lista_produtos.pop(-1) # Armazena item removido. Mas so assim ja funciona 
lista_produtos.pop(-1) # Mas so assim ja funciona 
print(lista_produtos)
print("Item removido foi o:", item_removido)
# Mostra que removeu dois item porque tem dois -1

# Adicionar item na lista se usa .append() => sempre adiciona na frente mesmo que ja existe
lista_produtos.append("picanha")
print(lista_produtos)

# Adicionar lista em uma lista mas deixando uma continua da outra sem ser lisat dentro de lista
# Usa-se .extend
lista2_produtos = ["farinha", "ovo", "limão"]
lista_produtos.extend(lista2_produtos)
print(lista_produtos)

# Adicionar/inserir item em um aposição específica se usa .insert()
lista_produtos.insert(0, "coca-cola")
print(lista_produtos)

# Contar quantas vezes um item esta na lista se usa .count()
lista_produtos.append("arroz")
print(lista_produtos)
print(lista_produtos.count("arroz"))

# Ordenar uma lista se usa .sort() => sort = ordenar 
lista_produtos.sort()
print(lista_produtos)

# Exemplo com números
lista_vendas.sort()
print(lista_vendas)

# Ordenar de traz para frente
lista_number = [100, 50, 20, 90, 40]
lista_number.sort(reverse=True)# Si não coloca True vai dar como falso
print(lista_number)