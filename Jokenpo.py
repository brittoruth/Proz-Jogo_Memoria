"""" RASCUNHO DAS REGRAS (PRA FACILITAR A CODAGEM, DEPOIS EXCLUIMOS NO FINAL ;) )
- Pedra ganha da tesoura (amassando-a ou quebrando-a).
- Tesoura ganha do papel (cortando-o).
- Papel ganha da pedra (embrulhando-a).

A pedra é simbolizada por um punho fechado; 
a tesoura, por dois dedos esticados; 
e o papel, pela mão aberta. 
Caso dois jogadores façam o mesmo gesto, ocorre um empate, 
e geralmente se joga de novo até desempatar. 
*Este jogo possui uma única regra: não é permitido mostrar pedra duas vezes seguidas*.
"""

import random
import time

print("--------- Bem vindo ao Jokenpô --------- \n!!!(じゃんけんぽん いらっしゃいませ)!!!")
#print() >>> explicar as regras básicas (um resumo do arquivo de regras do jogo)

scoreJogador = 0
scoreBot = 0
partidaFinalizada = False

#while partidaFinalizada == False:
configuracaoMao = {
    0 : "Pedra",
    1 : "Papel",
    2 : "Tesoura" 
}

botRandom = random.randint(0,2)
#jogadorBotMao = configuracaoMao[botRandom]
print(type(botRandom))
#print(type(jogadorBotMao))


escolhaJogador = int(input("Informe sua configuração de mão: \n[0] Pedra \n[1] Papel \n[2] Tesoura \n>>> "))
print(type(escolhaJogador))

time.sleep(1)
print("Jan")
time.sleep(1)
print("Ken")
time.sleep(1)
print("Pô!\n")
print("Você jogou: "+ configuracaoMao[escolhaJogador])
print("Seu oponente jogou "+ configuracaoMao[botRandom])

if botRandom == escolhaJogador: # se impatou repete round (mesma configuração)
    print("Empate. Vamos de novo!")

#Quem ganho a mão Acrua +1
# precisa construir as condicionais
    

# se input atual máquina ou jogador  == input máquina ou jogador anterior não permitir jogada
# *Este jogo possui uma única regra: não é permitido mostrar pedra duas vezes seguidas*


#Daqui pra baixo tá em contrução - parte de cima tá 100% funcionando
# repetir jogo até vitorioso +3 placar
