# propriedade dos numeros

# multiplos de 6
esc = int(input("digite uma opcao:"))
if esc == 1:
    num = int(input("digite um numero: "))
    multiplos = []
    c = 0
    for x in range(1,num):
        if x % 6 ==0 and x < num:
            multiplos.append(x)

    while c == 0:
        num += 1
        if num % 6 ==0:
            multiplos.append(num)
            c = 1
            break
    print(f"multiplos de 6 menores que {num}: {multiplos[0:-1]}\nproximo numero multiplo de 6: {multiplos[-1]}")

# primo ou composto
elif esc == 2:
    num = int(input("digite um numero: "))
    count = 0
    for x in range(1, num+1):
        if num % x == 0:
            count += 1
    print(f"o numero {num} é primo") if count == 2 else print(f"o numero {num} é composto")
    
#=========================================================================================

# Márveu versus Cápicon
from math import floor, ceil

entradas = []
for x in range(5):
    entradas.append(int(input("digite um número: ")))

# min e maximo
print(f"Marveu: menor entrada = {min(entradas)}")
print(f"capicon: maior entrada ={ max(entradas)}\n")

print("index minimo e maximo")
print(f"Marveu: minimo foi o {entradas.index(min(entradas)) +1}° numero informado")
print(f"capicon: maximo foi o {entradas.index(max(entradas))+1}° numero informado\n")

print("soma e produto")
print(f"Marveu: soma das entrada = {sum(entradas)}")
produto = 1
for x in entradas:
    produto *= x
print(f"capicon: produto das entradas = {produto}\n")

print("media e mediana")
print(f"Marveu: menor entrada = {sum(entradas)/(len(entradas)+1)}")
mediana = 0
if len(entradas) % 2 == 0:
    ind = int((len(entradas)+1)/2)
    mediana = round(entradas[ind] + entradas[ind+1]/2)
else:
    ind = int(len(entradas)/2)
    mediana = entradas[ind]

print(f"capicon: maior entrada ={mediana}\n")

print(entradas)
