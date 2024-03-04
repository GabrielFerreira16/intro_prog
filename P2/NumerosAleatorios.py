qtd1 = qtd2 = qtd3 = 0

QTD_NUMEROS = int (input ("Quantos números Vc deseja gerar? "))

NumAle = []
from random import randint
for X in range(1,QTD_NUMEROS+1):
  N = randint(1,3)
  NumAle.append(N)
  if N ==1: qtd1 = qtd1 + 1
  if N ==2: qtd2 = qtd2 + 1
  if N ==3: qtd3 = qtd3 + 1
  print(NumAle)

print("O total de 1s gerados foi = ",NumAle.count(1))
print("O total de 2s gerados foi = ",NumAle.count(2))
print("O total de 3s gerados foi = ",NumAle.count(3))

print("Média = ",sum(NumAle)/len(NumAle))
