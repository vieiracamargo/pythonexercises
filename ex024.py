number_int = int(input("Digite um número de 0 até 9999: "))

if (number_int  < 0 or number_int  > 9999):
    print("Digite um valor correto")
else:
    number_str = str(number_int)

    if(len(number_str) == 4):
        print(f"Unidade: {number_str[-1]}")
        print(f"Dezena: {number_str[-2]}")
        print(f"Centena: {number_str[-3]}")
        print(f"Milhar: {number_str[-4]}")

    elif(len(number_str) == 3):
        print(f"Unidade: {number_str[-1]}")
        print(f"Dezena: {number_str[-2]}")
        print(f"Centena: {number_str[-3]}")

    elif (len(number_str) == 2):
        print(f"Unidade: {number_str[-1]}")
        print(f"Dezena: {number_str[-2]}")
    else:
        print(f"Unidade: {number_str[-1]}")



