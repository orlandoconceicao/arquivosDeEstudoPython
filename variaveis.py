                                # MATERIAL DE ESTUDO - PYTHON
                                
                                # Variáveis
                                
# Criando variáveis 
faturamento = 1500 # Pode substituir o número dado pelo o nome da variável
custo = 1000 #int => número inteiro
lucro = 500
imposto = 0.15 #float => número decimal
novas_vendas = 333 
faturamento = faturamento + novas_vendas # Pode somar variáveis 

# Colocando print dentro do print separado por vírgula
print("Faturamento:", 1500) # Mais indicado  usar váriaveis
print("imposto:", imposto * faturamento)
print("Custo:",custo)
print("Lucro:", faturamento - custo - imposto)

# Puxando texto da variável
mensagem = "O lucro foi de 608.0" # String => texto
print(mensagem)

teve_lucro = True # Boolean => True or False

                                # OPERADORES

# Criando peradores 
dois = 2
cinco = 5 
dez = 10
treze = 13

adição = dois + dez 
print("Adição", adição)

subtração = cinco - dois
print("Subtração:", subtração)

multiplicação = dois * cinco 
print("multiplicação:", multiplicação)

# Mod => sobra da divisão
mod = cinco / dois 
print("Mod:", mod)

mod_inteiro = int(cinco / dois)
print("Mod_inteiro:", mod_inteiro)

mod_arredondado = round(treze / cinco)
print("Mod_arredondado:", mod_arredondado)

# Floor division => parte inteira da divisão
divisão_um = cinco // dois
print("Divisão 01:", divisão_um)

divisão_dois = dez // cinco
print("Divisão 02:", divisão_dois)

                                # TEXTOS E STRINGS

Produto = 300
Ganho = 900
salário = 2100
extra = 400

# Formas de textos - O f faz que as palavras que tem variavel não fazer parte do texto e sim da o resultado da variavel
texto01 = "O valor do produto e de " + str(Produto) + " e o ganho da empresa foi de " + str(Ganho)
print(texto01)

texto02 = f"Esse mês meu salário foi de {salário} e tive {extra} de hora extra" # Melhor forma
print(texto02)

# Tornar texto em letra minúscula         .lower => deixa tudo minúsculo
gmail = "LETRA_MINUSCULA@gmail.com"
print(gmail.lower())

# Remover espaço de texto / começo fim e espaço duplicado
gmail2 = "tirar_espaços@gmail.com "
print(gmail2.strip())

# Pegar posição de texto