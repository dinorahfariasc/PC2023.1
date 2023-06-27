# colecoes de dados
# ==============================================================================
# processando listas
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


# =======================================================================
# Masacarando telefones
# numeros = []
# final = []
# for x in range(10):
#     numeros.append(int(input("digite um numero: ")))
#
# for n in numeros[1:]:
#     num = n % numeros[0]
#     final.append(num)
#
# print(f"numero do cliente: {final}")

# =======================================================================
# Testando combinacoes

# def valordasenha(soma_valor, n):
#     pares = []
#
#     for i in range(len(n)):
#         for x in range(i + 1, len(n)):
#             if n[i] + n[x] == soma_valor:
#                 par = (n[i], n[x])
#                 pares.append(par)
#
#     if len(pares) == 0:
#         return None
#
#     pares.sort()
#     senha = f"{pares[0][0]}{pares[0][1]}"
#     print(senha)
#
# soma_valor = int(input("Insira a soma: "))
# n = []
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     n.append(numero)
#
# senha = valordasenha(soma_valor, n)
#
# print("Sua Senha é:", senha)


# ============================================================================
# Pedaço de senha
#
# frase = input("digite a frase: ").replace(" ","")
# teste = ""
# maior = ""
#
# for x in frase:
#     if x not in teste:
#         teste += x
#     else:
#         if len(teste) > len(maior):
#             maior = teste
#         teste = x
# if len(teste) > len(maior):
#     maior = teste
#
#
# print(maior)
