 # Jogo da adivinhação 
from random import randint
number = randint(1,31)
men = "menor"


for i in range(5): 
  num = int(input("adivinhe um número entre 1 e 31: "))
  men = "menor" if (num > number) else "maior"
  print(number)
  
  if num == number: 
    print("você acertou") 
    break
  else:
    print(f"você errou, o número era {men}")
#--------------------------------------------------------
# adicao de cores 
cor = []

print("digite a presença das cores")
ver = cor.append(int(input("vermelho: ")))
azu = cor.append(int(input("verde: ")))
ved = cor.append(int(input("azul: ")))

def switch(cor):
  if cor == [0,0,0]:
    return print("cor preta")
  elif cor == [1,0,0]:
    return print("cor vermelha")
  elif cor == [1,1,0]:
    return print("cor amarela")
  elif cor == [1,1,1]:
    return print("cor branca")
  elif cor == [1,0,1]:
    return print("cor magenta")
  elif cor == [0,1,0]:
    return print("cor verde")
  elif cor == [0,1,1]:
    return print("cor ciano")
  elif cor == [0,0,1]:
    return print("cor azul")
    
switch(cor)
#----------------------------------------------------
