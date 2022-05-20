
number = int(input("Digite um número: "))
tfactors = []

if number > 1:
    for i in range(1, number + 1):
        if number % i == 0:
            tfactors.append(i)

    if len(tfactors) == 2:
        if 1 in tfactors and number in tfactors:
            print(f"O número {number} é primo")
    else:
        print(f"O número {number} NÃO é primo")

    print(f"Ele tem um total de {len(tfactors)} divisores")
    print(f"Os divisores são : {tfactors}")

else:
    print("Digite um número maior que 1")