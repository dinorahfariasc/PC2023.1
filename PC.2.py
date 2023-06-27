# propriedade dos numeros

# multiplos de 6
# esc = int(input("digite uma opcao:"))
# if esc == 1:
#     num = int(input("digite um numero: "))
#     multiplos = []
#     c = 0
#     for x in range(1, num):
#         if x % 6 == 0 and x < num:
#             multiplos.append(x)
#
#     while c == 0:
#         num += 1
#         if num % 6 == 0:
#             multiplos.append(num)
#             c = 1
#             break
#     print(f"multiplos de 6 menores que {num}: {multiplos[0:-1]}\nproximo numero multiplo de 6: {multiplos[-1]}")
#
# # primo ou composto
# elif esc == 2:
#     num = int(input("digite um numero: "))
#     count = 0
#     for x in range(1, num + 1):
#         if num % x == 0:
#             count += 1
#     print(f"o numero {num} é primo") if count == 2 else print(f"o numero {num} é composto")

# =========================================================================================

# # Márveu versus Cápicon
#
# entradas = []
# for x in range(10):
#     entradas.append(int(input("digite um número: ")))
#
# # min e maximo
# print("\nmenor e maior entrada")
# print(f"Marveu: menor entrada = {min(entradas)}")
# print(f"capicon: maior entrada = {max(entradas)}\n")
#
# print("index minimo e maximo")
# print(f"Marveu: minimo foi o {entradas.index(min(entradas)) + 1}° numero informado")
# print(f"capicon: maximo foi o {entradas.index(max(entradas)) + 1}° numero informado\n")
#
# print("soma e produto")
# print(f"Marveu: soma das entrada = {sum(entradas)}")
# produto = 1
# for x in entradas:
#     produto *= x
# print(f"capicon: produto das entradas = {produto}\n")
#
# print("media e mediana")
# print(f"Marveu: media das entradas = {sum(entradas) / (len(entradas))}")
# mediana = 0
# if len(entradas) % 2 == 0:
#     ind = int((len(entradas) + 1) / 2)
#     mediana = round(entradas[ind] + entradas[ind + 1] / 2)
# else:
#     ind = int(len(entradas) / 2)
#     mediana = entradas[ind]
#
# print(f"capicon: mediana das entradas = {mediana}\n")

# ==================================================================================
# # lançe os dados
# from random import randint
#
# tab = int(input("digite a quantidade de casas do tabuleiro: "))
# passos1 = 0
# passos2 = 0
#
# for x in range(tab):
#     fabio = randint(1, 6)
#     print(f'fabio pode andar {fabio} casas')
#     passos1 += fabio
#     isa = randint(1, 6)
#     print(f'isa pode andar {isa} casas')
#     passos2 += isa
#     if passos1 >= tab:
#         print("fabio ganhou !")
#         break
#     elif passos2 >= tab:
#         print("isa ganhou!!")
#         break
#
# # print(passos1,passos2)

# ==================================================================================
# tres consecutivos
# soma = int(input("digite a soma: "))
# meio = soma // 2
# count = 1
# resultado = ""
# for x in range(meio):
#     if count % 2 == 0:
#         if count + (count +2) + (count + 4) == soma:
#             resultado = "SP"
#     elif count % 2 != 0:
#         if count + (count + 2) + (count + 4) == soma:
#             resultado = "SI"
#     count += 1
#
# if resultado == "":
#     resultado = "N"
# print(resultado)

# ===========================
#
# def verifica_soma(S):
#     if S % 2 != 0:
#         print("N")
#
#     n = S // 2
#     if n % 2 == 0:
#         print("SP")
#     else:
#         print("SI")
#
# S = int(input("Insira o valor de S: "))
# resposta = verifica_soma(S)
# print(resposta)