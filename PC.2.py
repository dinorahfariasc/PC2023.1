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
