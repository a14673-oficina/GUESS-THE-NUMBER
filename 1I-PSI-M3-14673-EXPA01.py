"""GUESS THE NUMBER

Pedir ao utilizador para inserir o nome

IA: GERAR NÚMERO 0-20

UTILIZADOR:
6 TENTATIVAS PARA ACERTAR

IA: APENAS RESPONDE SUPERIOR OU INFERIOR
IA: NÚMERO DE TENTATIVAS RESTANTES
 ----------------
VITÓRIA
IA: MENSAGEM DE SUCESSO
IA: NÚMERO NECESSÁRIO PARA ACERTAR

-----------------
Jogar outra vez?

-----------------
Pensar em Scoreboard
Guardar a informação do Jogador Vencedor e número de tentativas utilizado"""

import random

print(f"{'GUESS THE NUMBER' :^65}")
Nome = input("Qual é o nome do Utilizador?: ")
numeros = random.randint(0,21)
tentativas = 6
while tentativas > 0:
  numerotentativas = int(input(f"Tens {tentativas} Tentativas para acertar: "))
  if numeros == numerotentativas:
    print(f"Mensagem de sucesso, {Nome}!")
    print(f"{tentativas} tentativas")
    break
  elif numeros > numerotentativas:
      print("Numero incorreto, superior")
      tentativas -= 1
  elif numeros < numerotentativas:
      print("Numero incorreto, inferior")
      tentativas -= 1
  if numerotentativas < numeros and numerotentativas > numeros:
    print(f"Acabaram as tuas tentativas o numero correto é {numeros}, {Nome}")
queres=input("Queres jogar novamente? Sim ou Não: ")
if queres == "Sim":
    print("Opeção invalida")
if queres == "Não":
    exit()