                                # TEXTOS E STRINGS
                                
# and = so executa se a primeira condição for verdadeira e a segunda tambem
# or = executa se uma das condições for verdadeira

Produto = 300
Ganho = 900
salário = 2100
extra = 400

# Formas de textos - O f faz que as palavras que tem variavel não fazer parte do texto e sim da o resultado da variavel
# srt() transforma palavra em variavel se existir
texto01 = "O valor do produto e de " + str(Produto) + " e o ganho da empresa foi de " + str(Ganho)
print(texto01)

# Se quiser separar por centena e so colocar : depois da variável {salário:,}
# ja par acolocar casa decimal coloca .2f {extra:.2f} numero: quantas casas e f: float = decimal
# Para colocar percentual => % se usa {margem:.1%} e se deixa .0% vai apenas deixa o numero inteiro
texto02 = f"Esse mês meu salário foi de {salário} e tive {extra} de hora extra" # Melhor forma
print(texto02)

# Tornar texto em letra minúscula se usa .lower => deixa tudo minúsculo
minusculo = "TUDO MINÚSCULO"
print(minusculo.lower())

# Tornar texto em letra maiúscula se usa .upper()
maiusculo = "tudo maiúsculo"
print(maiusculo.upper())

# DEixar primeira letra maiúscula se usa .capitalize()
meu_nome = "orlando conceicao"
meu_nome = meu_nome.capitalize()
print(meu_nome)

# DEixar cada letra inicial de um nome completo seu usa .title() | tira os comentarios para ver
#meu_nome = meu_nome.title()
#print(meu_nome)

# Remover espaço de texto / começo fim e espaço duplicado se usa .strip
espaçosx = " espaços desnecessarios "
print(espaçosx.strip())


# Ver quantos caracteres tem no texto se usa len() vem de lenght => comprimento/tamanho
texto03 = "um texto para ser contado."
print(len(texto03))

# Pegar posição de texto se usa .fin
texto04 = "Que posição esta o x" 
posição = texto04.find("x")
print("O x esta na posição:", posição)

# Pegar primeiro nome
meu_nome2 = "orlando conceicao"
primeiro = meu_nome2.find(" ")
meu_nome2 = meu_nome2[:primeiro]
meu_nome2 = meu_nome2.capitalize()
print(meu_nome2) 

# Pegar pedaços do texto  se usa .find depois variavel[]
# eu pedi o 44 mas o 44 não sera enviado tem que pedir um a mais
# Si for pega de um ponto ate o final não precisa coloca nada depois dos : e viceversa
# Para deixar automatico coloca a posição que foi puxada antes dos :
# Tambem pode colocar +1 dps dos numeros/variaveis
texto05 = "Pegar pedaços do textos, estara sendo puxada."
position = texto05.find(",")
print("Pocição da virgula:", position)
print("Depois da vírgula:", texto05[24:44])

# Trocar um pedaço do texto se usa replace()
texto06 = "um dois tres quatro seis"
print(texto06.replace("seis", "cinco"))

# Como contar letras de uma frase, se usa .count
texto = "Aprendendo a contar letras"
quantidade = texto.lower().count("a")
print(quantidade)

                                # Atividade

# Crie uma mensagem com o texto "bem-vindo ao curso de python!"
    # Substitua "python" por "FastAPI".
texto07 = "bem-vindo ao curso de python"
print(texto07.replace("python", "Feastapi"))

#Combine as duas frases em uma só, usando f-string
frase1 = "Python é incrível"
frase2 = "estou começando FastAPI"
juntas = f"{frase1}, {frase2}"
print(juntas)

# Tire os espaços estras da frase 
frase = " hoje eu fui na praia "
frase = frase.strip()
print(frase)

# Crie uma frase e uma variavel com seu nome frase"Olá, bem-vindo ao curso de Python, [SEU NOME]!"
    # Coloque seu nome no [SEU NOME] com .replace()
frase1 = "Olá, bem-vindo ao curso de Python, [SEU NOME]!"
nome1 = "Orlando"
frase1 = frase1.replace("[SEU NOME]", nome1)
print(frase1)

# Conte quantas letras que masi tem no seu nome 
nome2 = "Orlando Conceicão"
quantos_o = nome2.lower().count("o")
print(quantos_o)
