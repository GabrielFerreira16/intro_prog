LisNum = []
ACERTOS = 0
ERROS = 0
from random import randint
print("Bem vindo ao quiz dos números, nós faremos 10 perguntas, e a resposta de cada uma é um número entre 1 e 10, elas aparecerão em ordem aleatória.")
print("Equipe I Love ~Davis - Mário, Gabriel, João Pedro e Allan.")

for X in range(1,101):
  X = randint(1,10)

  if 1 not in LisNum:
    if X == 1:
      A = int(input("\ntodo número dividido por mim é igual a ele mesmo"))
      if A == 1: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(1)  

  if 2 not in LisNum: 
    if X == 2: 
      A = int(input("\nqual o número cujo seu dobro é igual seu quadrado?"))
      if A == 2: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(2)  

  if 3 not in LisNum:  
    if X == 3: 
      A = int(input("\nqual o segundo número primo?"))
      if A == 3: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(3)

  if 4 not in LisNum: 
    if X == 4: 
      A = int(input("\nmeu dobro é igual ao cubo da minha metade"))
      if A == 4: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(4)  

  if 5 not in LisNum:  
    if X == 5: 
      A = int(input("\nas minhas multiplicações sempre acabam com 0 ou com 5"))
      if A == 5: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(5)  

  if 6 not in LisNum:      
    if X == 6: 
      A = int(input("\neu sou a soma dos dois primeiros números pares, tirando o 0"))
      if A == 6: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(6)  

  if 7 not in LisNum:    
    if X == 7: 
      A = int(input("\neu sou o dobro de 2, mais 3"))
      if A == 7: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(7)

  if 8 not in LisNum:   
    if X == 8: 
      A = int(input("\ndivido duas vezes por 2, ainda permaneço par"))
      if A == 8: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(8)  

  if 9 not in LisNum:  
    if X == 9: 
      A = int(input("\nme vire de cabeça pra baixo e eu viro par"))
      if A == 9: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else: 
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(9)  

  if 10 not in LisNum:  
    if X == 10: 
      A = int(input("\nqual é o primeiro número de dois dígitos?"))
      if A == 10: 
        print("correto")
        ACERTOS = ACERTOS + 1
      else:
        print("incorreto")
        ERROS = ERROS + 1
      LisNum.append(10) 

print("\nO número de acertos foi: ", ACERTOS)
print("O número de erros foi: ", ERROS)

if ACERTOS > ERROS: 
    print("\nParabéns, você ganhou!")
if ERROS > ACERTOS: 
    print("\nVocê perdeu, tente de novo!")
if ERROS == ACERTOS: 
    print("\nEMPATE!")

print("respostas em ordem: ", LisNum)