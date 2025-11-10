print("Buenos dias mis amigos")

#Descrição
print("Jogo das Palavras")
print("Responda as Perguntas Corretamente")
print("A Cada Resposta Correta Você Ganha 1 Ponto")
print("Boa Sorte!")

#Perguntas
pontos=0
nome=input("Qual é seu nome?")
idade=input("Qual a sua idade?")
print("Meu nome é", nome,"e minha idade é", idade,"anos")
pontos+=1
#If e else
Brasilia=locals
capital=input("Qual é a capital do Brasil?")
if capital == "Brasilia":
    print("Correto!")
    pontos+=1
else:
    print("A Resposta Está Errada!")

idade=int(input("Qual é a sua idade?"))
if idade >= 18:
    print("Você é maior de idade")
    pontos+=1
else:
    print("Você não é maior de idade")

pi=input("Qual é o valor de pi?")
if pi == "3,14":
    print("Correto!")
    pontos+=1
else:
    print("A Resposta Está Errada!")

tom=input("Qual é o nome do ator do Homen Aranha?")
if tom == "Tom Holland" or tom == "Tobey Maguairi" or tom == "Andrew Garfield":
    print("Correto!")
    pontos+=1
else:
    print("A Resposta Está Errada!")

enzo=input("Qual é o nome do fundador da Ferrari?")
if enzo == "Enzo Ferrari":
    print("Correto!")
    pontos+=1
else:
    print("A Resposta Está Errada!")
#Jogo de Perguntas
print("Fim de jogo!", nome, "você ganhou", pontos, "pontos")
