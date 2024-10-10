#equipe: Mário, João Pedro, Allan e Gabriel
#questão O:
print("Seu número é um número de armstrong? \n")

N = int(input("Digite um número de 3 dígitos: \n"))
C = N // 100
D = (N - (C * 100)) // 10
U = N - (C * 100) - (D * 10)

if N == (C**3) + (D**3) + (U**3):
  print("É um número de armstrong \n")

else:
  print("Não é um número de armstrong \n")

#questão P:
print("Estes são os números de armstrong com 3 dígitos:")
for N in range (100, 999+1):
  C = N // 100
  D = (N - (C * 100)) // 10
  U = N - (C * 100) - (D * 10)
  if N == (C**3) + (D**3) + (U**3):
    print(N)