 # Jogo da adivinhação 
# from random import randint
# number = randint(1,31)
# men = "menor"


# for i in range(5): 
#   num = int(input("adivinhe um número entre 1 e 31: "))
#   men = "menor" if (num > number) else "maior"
#   #print(number)
#   if num == number: 
#     print("você acertou") 
#     break
#   else:
#     print(f"você errou, o número era {men}")
# #--------------------------------------------------------
# adicao de cores 
# cor = []

# print("digite a presença das cores")
# ver = cor.append(int(input("vermelho: ")))
# azu = cor.append(int(input("verde: ")))
# ved = cor.append(int(input("azul: ")))

# def switch(cor):
#   if cor == [0,0,0]:
#     return print("cor preta")
#   elif cor == [1,0,0]:
#     return print("cor vermelha")
#   elif cor == [1,1,0]:
#     return print("cor amarela")
#   elif cor == [1,1,1]:
#     return print("cor branca")
#   elif cor == [1,0,1]:
#     return print("cor magenta")
#   elif cor == [0,1,0]:
#     return print("cor verde")
#   elif cor == [0,1,1]:
#     return print("cor ciano")
#   elif cor == [0,0,1]:
#     return print("cor azul")
    
# switch(cor)
#----------------------------------------------------

# jankenpo 
# from random import randint
# modo = int(input('escolha um modo de jogo \nRodada única digite 1 \nMelhor de cinco digite 2 \n:'))

# res = []
# rodadas = [1,2,3,4,5]

# if modo == 1:
#   player = int(input('escolha sua opção \nPedra - digite 1\nPapel - digite 2\nTesoura - digite 3\n:'))
#   res.append(player)
#   pc = randint(1,3)
#   res.append(pc)
   
#   #print(res)
  
#   if res[0] - res[1] == 1: 
#     print('o jogador venceu')
#   elif abs(res[0] - res[1]) == 2:
#     print('o jogador venceu')
#   elif res[0] - res[1] < 0:
#     print('o pc venceu')
#   elif abs(res[1] - res[0]) == 2:
#     print('o pc venceu')
#   elif player == pc:
#     print('deu empate')
      
    
# if modo == 2:
#   final = []
#   for i in rodadas:
#       res = []
#       player = int(input('escolha sua opção \nPedra - digite 1\nPapel - digite 2\nTesoura - digite 3\n:'))
#       res.append(player)
#       pc = randint(1,3)
#       res.append(pc)
#       print(res)
      
#       if player == pc:
#         print('deu empate')
#         rodadas.append(1)  
#       elif res[0] - res[1] == 1 : 
#         print('o jogador venceu')   
#         final.append(1)
#       elif abs(res[0] - res[1]) == 2:
#         print('o jogador venceu')
#         final.append(1)  
#       elif res[0] - res[1] < 0:
#         print('o pc venceu')
#         final.append(2)
#       elif abs(res[1] - res[0]) == 2:
#         print('o pc venceu')
#         final.append(2)
                 
#   print(final)    
#   if final.count(1) > final.count(2):
#       print('jogador ganhou')
#   elif final.count(2) > final.count(1):
#       print('pc ganhou')

#-------------------------------------------------------------
# histograma 
# intervalos = [[0,2.5],[2.5,5],[5,7.5],[7.5,10]]
# histo = [0,0,0,0]

# print('========== HISTOGRAMA ===========')
# func = int(input('escolha a funcionalidade\n1- intervalo de uma nota\n2- frequencia 30 notas\n'))

# if func == 1: 
#   histo1 = [0,0,0,0]
#   count2 = 0
#   nota = int(input('digite a nota: '))
#   for i in intervalos:
#     if nota >= i[0] and nota < i[1]:
#       histo1[count2] += 1
#     else:
#       count2 +=1
#   for i,x in zip(histo1,intervalos):
#     print(f'({x[0]} ; {x[1]}]: '+'▓'*i) 
#   print(f'({intervalos[3][0]} ; {intervalos[3][1]}): '+'▓'*histo1[3])  
    
# elif func == 2:
#   for i in range(5):
#     count = 0
#     nota = int(input('digite a nota: '))
#     for i in intervalos:
#       if nota >= i[0] and nota < i[1]:
#         histo[count] += 1
#       else:
#         count += 1
#   for i,x in zip(histo[:3],intervalos[:3]):
#     print(f'({x[0]} ; {x[1]}]: '+'▓'*i)
#   print(f'({intervalos[3][0]} ; {intervalos[3][1]}): '+'▓'*histo[3])
 
# =======================================================================================      
# choque de propagandas 

# primeirox1 = float(input("Insira a coordenada x do primeiro pop-up: "))
# primeirox2 = float(input("Insira a coordenada x2 do primeiro  pop-up: "))
# primeiroy1 = float(input("Insira a coordenada y do primeiro pop-up: "))
# primeiroy2 = float(input("Insira a coordenada y2 do primeiro  pop-up: "))
# segundox1 = float(input("Insira a coordenada x do segundo pop-up : "))
# segundox2 = float(input("Insira a coordenada x2 do segundo pop-up : "))
# segundoy1 = float(input("Insira a coordenada y do segundo pop-up : "))
# segundoy2 = float(input("Insira a coordenada y2 do segundo pop-up : "))

# if max(primeirox1, segundox1) < min(primeirox2, segundox2) and max(primeiroy1, segundoy1) < min(primeiroy2, segundoy2):
#     print("Existe uma intersecção")
# else:
#     print("Não há intersecção") 


