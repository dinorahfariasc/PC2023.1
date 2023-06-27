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


# ================================================

# pedaço de senha
# repeticoes = []
#
# frase = input("digite a frase: ").replace(" ","")
# senha = [0 for x in range(len(frase))]
# c = 0
# for x in frase:
#     repeticoes.append(frase.count(x))
#
# for l in repeticoes:
#     if repeticoes[repeticoes.index(l)] == 1:
#         if repeticoes[repeticoes.index(l) + 1] == 1:
#             senha[c] += 1
#     else:
#         c += 1
#
# comeco = senha.index(max(senha))
#
# final = frase[comeco:max(senha)]
# print(repeticoes)
# print(senha)
# print(final)


