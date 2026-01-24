                                # DICIONÁRIOS

# keys () = são os nomes 
# values() = são os valores
# prodtuos = ["keys", values]
lista_produtos = ["arroz", "feijao", "batata",]
lista_precos = [32, 17, 9]

dic_produtos = {"arroz": 32, "feijao": 17, "batata": 9}

print(lista_produtos)
print(lista_precos)

# pegar produto/item
produto = "arroz"
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(produto, preco)

print(dic_produtos["batata"])

# Editar item do dicionário
dic_produtos["arroz"] = dic_produtos["arroz"] *1.1

# Adicionar item no dicionário
dic_produtos["alface"] = 6
print(dic_produtos)

# Remover item
item_removido = dic_produtos.pop("alface")# tira do dicionario
print("item removido", item_removido) # si armazena e puxa item removido, voce ve o preço

# Verificar se existe produto
print("arroz" in dic_produtos.keys())
print(35.2 in dic_produtos.values())

produtos = list(dic_produtos.keys())
print(produtos)
precos = list(dic_produtos.values())
print(precos)

# Contagem de itens do dicionário
quantos = len(dic_produtos)
print(quantos)

# Atividade
dic_produtos = {"arroz": 32, "feijao": 17, "batata": 9}

produto_buscado = input("Digite o nome do produto:")
produto_buscado = produto_buscado.strip()
produto_buscado = produto_buscado.lower()

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print("Produto encontrado")
    print(f"produto {produto_buscado}, tendo o preço de: R${preco}")
else:
    print("Produto não encontrado")