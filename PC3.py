# colecoes de dados

# processando listas
# tinha feito com listas ja!

# =============================================

# masacarando telefones

# numeros = []
# final = []
# for x in range(5):
#     numeros.append(int(input("digite um numero: ")))
#
# for n in numeros[1:]:
#     num = n % numeros[0]
#     final.append(num)
#
# print(f"numero do cliente: {final}")

# ================================================
# testando combinacoes
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


# ==========================================================

# pedaço de senha
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
#
