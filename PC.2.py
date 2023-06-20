# propriedade dos numeros

# multiplos de 6
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
