print ("Seja bem vindo a tabuada online")
print ("* para ver a tabuada de multiplicação")
print ("+ para ver a tabuada de adição")
tabuada = input("\nQual tabuada você deseja saber? ")
if tabuada == "+":
  tabuada=int(input("Tabuada do número: "))
  for count in range(10):
    print("%d + %d = %d" %(tabuada,count+1,tabuada+(count+1)))
elif tabuada == "*":
  tabuada=int(input("Tabuada do número: "))
  for count in range(10):
    print("%d x %d = %d" %(tabuada,count+1,tabuada*(count+1)))
